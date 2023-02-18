
N = int(input())

group_word = 0
for _ in range(N):
    word = input()
    error = 0

    #알고리즘
    # 현재 문자와 다음 문자와 비교해서 다음문자가 다른 문자가 나올 때 현재 단어가 문자열 내에 존재하지 않아야 한다.

    for index in range(len(word)-1): #인덱스 범위 생성 : 0부터 단어개수 -1까지
        if word[index] != word[index+1]: #연달은 두 문자가 다른 때,
            new_word = word[index+1:]
            if new_word.count(word[index]) > 0: #남은 문자열에서 현재글자가 있었다면
                error += 1

    if error == 0:
        group_word += 1 #error가 0이면 그룹단어

print(group_word)


