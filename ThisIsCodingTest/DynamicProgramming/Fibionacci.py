

import math
import time
#DP를 사용시 작은 문제의 결과값을 저장하는 배열
# Top-down, Bottom-up 방식 별개로 생성

def fibo(x):
    if x == 0 or x == 1:
        return x
    return fibo(x-1) + fibo(x-2)

# Top-down(Memoization) - 재귀
def topdown(n): #topdwon 방식 / memo /
    #기저 상태 도달시, 0과 1로 초기화
    global topdown_memo
    if n <= 2:
        topdown_memo[n] = 1
        return topdown_memo[n]

    # memo에 계산된 값이 있으면 바로 반환
    if(topdown_memo[n] > 0):
        return topdown_memo[n]

    # memo에 값이 없다면 계산(재귀)
    topdown_memo[n] = topdown(n-1) + topdown(n-2)
    return topdown(n)

# Bottom-up(Tabulation)방식 - table-filling / 반복문
def bottomup(n):
    global bottomup_table
    bottomup_table[1] = 1
    bottomup_table[2] = 1

    for i in range(2, n+1):
        # table을 채워나감
        bottomup_table[i] = bottomup_table[i-1] + bottomup_table[i-2]

    return bottomup_table[n]


n = int(input())
startTime = time.time()
print(fibo(n))
endTime = time.time()
print(f"걸린시간 : {endTime-startTime:.5f}" )

topdown_memo = [0] * (n+1)
bottomup_table = [0]* (n+1)

startTime = time.time()
print(topdown(n))
endTime = time.time()
print(f"걸린시간 : {endTime-startTime:.5f}" )

startTime = time.time()
print(bottomup(n))
endTime = time.time()
print(f"걸린시간 : {endTime-startTime:.5f}" )






