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
    pattern = re.compile('[\w_]+')  # 정규 표현식
    return pattern.sub(' ', str_data).lower()  # 소문자로 바꿔


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


print_all(
    sort(
        frequencies(
            remove_stop_words(
                scan(
                    filter_chars_and_normalize(
                        read_file(sys.argv[1])
                    )
                )
            )
        )
    )[0:25])

# 해설
# - 파이프 라인 형식은 공장 파이프라인 모델을 본뜬 것으로 각 위치 또는 상자에서 그것을 지나는 데이터를 맡아 특정 작업을 수행한다
# - 가장 순수한 형태 면에서 파이프라인 형식은 수학적 함수 이론을 충실히 반영한 것이다
# - 입력으로 함수를 취하거나 함수를 출력하는 함수를 고차 함수(High-order function) 라고 한다
# - 파이프 라인 프로그래밍 형식에서는 모든 것을 입력 집합 하나를 출력 집합 하나에 매핍하는 연관 관계로 바라봄으로써
#   이러한 수학적 순수성을 당성하려 한다
# - 파이프라인에서는 시작할 때 계산에 대한 입력원과 마지막에 출력을 받는 곳 외에 상자화된 함수 외부의 세계는 존재하지 않는다
#   프로그램은 상자화된 함수와 함수 합성으로 표현한다
# - 멱등성이 보장된다
# - 예제 프로그램에서는 모든 함수가 인자가 단 하나만 있지만 일반적으로 함수에는 여러 인자가 있을 수 있다
#   그러나 인자가 여러 개인 함수는 모두 커링(Currying)이라는 기법을 통해 일련의 단일 값 고차 함수로 변형 할 수 있다
def f1(x, y, z):  # 커링 미적용
    return x * y + z


f1(2, 3, 4)


def f(x):  # 커링 적용
    def g(y):
        def h(z):
            return x * y + z

        return h

    return g


f(2)(3)(4)

# 시스템 설계 관점에서 본 이러한 형식
# - 파이프 라인 형식은 특히 해당 문제의 특성이 파이프라인으로 모델링할 수 있는 문제에 적합하다
#   그래프 검색과 같은 인공지능 알고리즘인 A* 등은 이 범주에 속한다
#   컴파일러 및 다른 언어 처리기에도 적합한데 그래프와 트리 구조를 바탕으로 한 기능으로 구성하는 경향이 있기 때문이다
# - 문제에 대한 적합성 외에도 이 형식을 사용하는 것이 좋은 이유는 단위 테스트와 병행성이다
#   이 형식을 활용한 프로그램은 단위 테스트하기가 매우 쉽다
#   테스트 할 수 있는 상자화된 함수 외부에 어떤 상태도 보관하지 않으므로 해당 테스트를 한번 또는 여러 번 다른 순서로 실행 하더라도
#   항상 같은 결과가 만들어지기 때문이다
#   문제를 파이프라인 형식으로 적절히 표현할 수 있다면 그렇게 하는 것이 좋다

# 역사적
# -












































