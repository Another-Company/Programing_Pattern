# Cookbook
# 먼 분기(long jump)가 없다
# 절차적 추상화를 이용해 규모가 큰 문제를 더 작은 단위로 분할함으로써 제어 흐름 복잡도를 완화한다
# 프로시저는 상태를 전역 변수 형태로 공유할 수 있다
# 규모가 큰 문제는 공유한 상태를 변경하거나 그 상태를 더 추가하는 프로시저를 차례로 적용해 해결한다

import sys, string

data = []
words = []
word_freqs = []

# 파일을 읽어서 한글자씩 리스트에 담는다
def read_file(path_to_file):
    global data
    with open(path_to_file) as f:
        data = data + list(f.read())


# 한글자씩 담아논 리스트에서 글자가 아닌건 공백으로 바꾼다
def filter_chars_and_normalize():
    global data
    for i in range(len(data)):
        if not data[i].isalnum():
            data[i] = ' '
        else:
            data[i] = data[i].lower()


# 한글짜식 표준화된 글자들을 단어로 만들어 준다
def scan():
    global data
    global words
    data_str = ''.join(data)
    words = words + data_str.split()

# 단어로 만들어 놓은것에서 필요없는 단어를 삭제한다
def remove_stop_words():
    global words
    with open('/Users/hyun/Desktop/BackgroundInfo/Book/Programing_Pattern/stop_words.txt') as f:
        stop_wrods = f.read().split(',')

    stop_wrods.extend(list(string.ascii_lowercase))
    indexes = []
    # 단어 집합중에 필요없는 단어의 인덱스를 저장
    for i in range(len(words)):
        if words[i] in stop_wrods:
            indexes.append(i)

    # 단어 집합에서 필요없는 단어를 뽑아 버린다
    for i in reversed(indexes):
        words.pop(i)



def frequencies():
    global words
    global word_freqs

    for w in words:
        keys = [wd[0] for wd in word_freqs]
        if w in keys:
            word_freqs[keys.index(w)][1] += 1
        else:
            word_freqs.append([w, 1])


def sort():
    global word_freqs
    # word_freqs.sort(lambda x, y: cmp(y[1], x[1]))


read_file(sys.argv[1])
filter_chars_and_normalize()
scan()
remove_stop_words()
frequencies()
sort()

for tf in word_freqs[0:25]:
    print(tf[0], ' - ', tf[1])


# - 규모가 큰 문제를 각각 한 가지 일을 하는 하위 유닛 다른 말로 프로시저로 분할한다
# - 최종 목표를 달성하는 방법으로 프로시저 사이에 데이터를 공유하는 것이 일반적이다
# - 공유 데이터에 부수 효과를 일으킨다
#   -> 계산은 풀(Pool)에 존재하는 어떤 데이터를 처리하고 다음 프로시저를 위한 데이터를 준비하는 프로시저 하나에서 시작한다
#      프로시저에서는 데이터를 반환하지 않으며 공유 데이터를 처리하기만 한다


# 이 방식의 특징
# - 어떤 큰 문제를 더 작은 하위 문제로 깔끔하게 분할하고 각각을 면명한 프로시저로 다루며 주 프로그램에서는
#   그 프로시저 각각에 해당하는 명령을 순차적으로 호출하는데 이는 복잡한 요리법을 따를 때 하는 것과 비슷하다
#   프로시저 각각에서는 차례로, 우리가 요리법에 따라 재료의 상태를 변경하는 것과 마찬가지로 공유 변수의 상태를 변경한다
# - 연산을 여러번 반목하면 결과가 달라진다 -> 멱등성이 없다 -> 프로그래밍 오류의 원인중 많은 부분을 차지한다
# - 외부 데이터를 내내 누적하며 데이터에 따라 그러한 행위가 달라지는 계산 작업에 적합하다
# - 서로 다른 시점에 여러입력을 요청하여 프로그램 출력 내용이 사용자가 입력한 모든 데이터에 의존하는 사용자 상호 작용에서
#   내내 상태를 유지하고 변경하는 것은 이 형식의 절절한 예이다
# - 시스템 규모 면에서는 데이터베이스에 저장된 것과 같은 외부 상태를 공유하고 변경하는 구성 요소를 사용하는 등 실제로 요리책
#   구조 형식이 널리 사용된다













































