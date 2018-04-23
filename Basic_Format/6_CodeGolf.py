# 코드골프 (Code Golf)

# 제약조건
# 코드줄 수를 가능한 한 적게 한다

import re, sys, collections

stops = open('/Users/hyun/Desktop/BackgroundInfo/Book/Programing_Pattern/stop_words.txt').read().split(',')
words = re.findall('[a-z]{2,}', open(sys.argv[1]).read().lower())
counts = collections.Counter(w for w in words if w not in stops)
for (w, c) in counts.most_common(25):
    print(w, '-', c)


# 해설
# - 이 형식의 주된 관심사는 간결함이다
# - 간결함이 유일한 목표라면 이 형식으로 작성된 코드가 결과적으로 이해해기 어려운 명령이 나열된 매우 긴 몇줄의 코드가 되는 것이 이상하지 않다
# - 하지만 간결함을 적절히 활용하면 작은 크기로 인해 꽤 우아하고 읽기 쉬운 프로그램을 만들어 낼 수도 있다
# - 코드 줄 수 측면에서 간결함은 이미 다른 누군가각 만들어 둔 강력한 추상화를 사용하는 것과 관련돼있다


# 시스템 설계 관점에서 본 이러한 형식
# - 소프트웨어 업계에서 사용하는 가장 인기 있는 측정 지표 중 하나는 소스코드 줄 수(Source Lines fo Code:SLOC)이다
#   좋든 나쁘든 SLOC는 비용 산정 개발자 생산성 유지보수성 및 다른 여러 관리적인 측면의 관심사에 대한 간접적인 지표로 널리 사용된다
# - 가능한 한 가장 짧은 프로그램을 다양한 프로그래밍 언어로 만드는 기술에는 심지어 '코드 골프라는 이름도 있다
