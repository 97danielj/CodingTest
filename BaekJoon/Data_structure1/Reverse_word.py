# 문장에서 각 단어를 모두 뒤집어 출력
# 스택을 사용
# 각 단어를 뒤집어서 출력

import sys

N = int(sys.stdin.readline())

for i in range(N):
    sentence_list = sys.stdin.readline().split()
    # 2차원 리스트 생성
    for word in sentence_list:
        for j in range(len(word)-1, -1, -1):
            print(word[j], end='')
        else:
            print(' ',end='')

    print()
