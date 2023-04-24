def solution(s):
    lengths = [] # 구간 길이 리스트
    count = 1 # 연속해서 나타나는 구간 길이
    for i in range(1, len(s)):
        if s[i] == s[i-1]: # 연속하면
            count += 1
        else:
            lengths.append(count)
            count = 1
    lengths.append(count)

    # 처음과 끝을 처리
    if len(lengths) != 1:
        if s[0] == s[-1]:
            lengths[0] += lengths.pop()

    return sorted(lengths)
