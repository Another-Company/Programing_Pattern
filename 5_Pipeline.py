# 파이프라인 (pipeline)

# 제약조건
# - 규모가 큰 문제를 함수형 추상화를 사용해 분해한다. 함수는 입력을 취해 출력을 만들어 낸다
# - 함수는 상태를 서로 공유하지 않는다
# - 수학적 함수 합성의 결과를 신뢰할 수 있는 것처럼 규모가 큰 문제는 함수를 차례차례 파이프라인으로 합성해 해결한다

import sys, re, operator, string


def read_file(path_to_file):
    with open(path_to_file) as f:
        data = f.read()
    return data


def filter_chars_and_normalize(str_data):
    pattern = re.compile('[\w_]+')
    return pattern.sub(' ', str_data).lower()


def scan(str_data):
    return str_data.split()


def remove_stop_words(word_list):
    with open('/Users/hyun/Desktop/BackgroundInfo/Book/Programing_Pattern/stop_words.txt') as f:
        stop_words = f.read().split(',')
        stop_words.extend(list(string.ascii_lowercase))
        return [w for w in word_list if not w in stop_words]


def frequencies(word_list):
    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs


def sort(word_freq):
    return sorted(word_freq.iteritems(), key=operator.itemgetter(1), reverse=True)


def print_all(word_freqs):
    if (len(word_freqs) > 0):
        print(word_freqs[0][0], ' - ', word_freqs[0][1])
        print_all(word_freqs[1:])


print_all(sort(frequencies(remove_stop_words(scan(filter_chars_and_normalize(read_file(sys.argv[1]))))))[0:25])
