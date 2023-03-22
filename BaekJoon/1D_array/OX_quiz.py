
# OX 퀴즈는 X는 0점, O는 연속점수를 반영
# 연속점수
# 축적치를 검색하여 현재 점수 1에 더해준다.
# 반례 : O가 마지막 원소에 존재 한다면
N = int(input())

for test_case in range(N):
    sequence_score = 0
    total_score = 0
    target = input()
    for i in target:
        if i == 'X':
            sequence_score = 0
        else:
            total_score += (1 + sequence_score)
            sequence_score += 1

    print(total_score)
