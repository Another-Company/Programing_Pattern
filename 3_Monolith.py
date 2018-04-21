import sys, string


# 일체식(Monolith)

# 제약조건
# - 명명된 추상화가 없다
# - 라이브러리를 전혀 또는 거의 사용하지 않는다

word_freqs = []
with open('/Users/hyun/Desktop/BackgroundInfo/Book/Programing_Pattern/stop_words.txt') as f:
    stop_words = f.read().split(',')
stop_words.extend(list(string.ascii_lowercase))  # 의미 없는 단어들을 묶어 놓는다
for line in open(sys.argv[1]):
    start_char = None
    i = 0
    for c in line:  # 글자 하나씩 넘긴다
        if start_char == None:
            if c.isalnum():
                start_char = i  # 단어 시작을 찾는다
        else:
            if not c.isalnum():
                found = False  # 단어 끝을 찾았으므로 처리한다
                word = line[start_char:i].lower()  # 단어 시작과 끝을 찾았으므로 한 단어를 만든다
                # 의미 없는 단어를 무시
                if word not in stop_words:
                    pair_index = 0
                    # 빈도표에 이미 존재하는 경우
                    for pair in word_freqs:
                        if word == pair[0]:
                            pair[1] += 1  # 단여별 빈도수 증가
                            found = True
                            found_at = pair_index  # 단어별 빈도수 리스트에서 몇번째 단어인지
                            break
                        pair_index += 1
                    # 빈도표에 존재 하지 않는 경우
                    if not found:
                        word_freqs.append([word, 1])
                    elif len(word_freqs) > 1:
                        for n in reversed(range(pair_index)):  # 빈도수가 가장 적은것 부터 하나씩
                            print(n)
                            if word_freqs[pair_index][1] > word_freqs[n][1]:
                                # 빈도수 25개 순위 정
                                word_freqs[n], word_freqs[pair_index]\
                                    = word_freqs[pair_index], word_freqs[n]
                                pair_index = n
                start_char = None  # 초기화
        i += 1

for tf in word_freqs[0:25]:
    print(tf[0], ' - ', tf[1])

# - 거의 '그리운 옛날' 형식으로 문제를 푼 수준
# - 처음부터 끝까지 새로운 추상화를 추가하지 않고 라이브러리에서 제공하는 것도 별로 사용하지 않으면서 코드를 하나로 구성했다
# - 설계 관점에서 주된 관심사는 문제를 분할하거나 기존 코드의 이점을 어떻게 취할지 별로 생각하지 않고 원하는 출력을 얻는 방식
# - 일체식 프로그램은 이해하기가 힘들다
# - 순환 복잡도
    # 프로그램 본문을 방향 그래프(Directd graph)로 생각하는 빙식
    # CC = E - N + 2P
    # E = 변(edge)수, N = 노드수, P = 출구 노드수
# - 보통 시스템 규모에 관계 없이 좋지 않은 사례이
