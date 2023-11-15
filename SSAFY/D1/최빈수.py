T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    i = int(input())
    #테스트 케이스마다 max value의 size+1 크기의 리스트를 만들어서 해당 인덱스를 올림
    arr = list(map(int, input().split())) #1000개의 입력값 리스트 변경
    cnt_arr = [0]*(max(arr)+1) #가장큰값 +1로 카운트 배열 생성 / value 가 인덱스
    for j in arr:
        cnt_arr[j] += 1

    tmp = [idx for idx, value in enumerate(cnt_arr) if max(cnt_arr) == cnt_arr[idx]] #근데 두개 일 수 도 있다.
    #상관 없는게 점수가 오름차순으로 cnt_arr가 정렬되어있다.
    print('#{}'.format(i),tmp[-1])

    # ///////////////////////////////////////////////////////////////////////////////////
