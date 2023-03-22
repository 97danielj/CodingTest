'''
#알고리즘
# 1. 소수를 찾는다
# 2. 작은 소수 부터 나누어 본다.
def solver(N):
    # 소인수 찾기
    if N == 1:
        return
    else:
        factor_list = []
        for i in range(2, N+1):
            #인수이가?
            if N % i != 0:
                continue
            else:
                # 소수인가?
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    factor_list.append(i)

    idx = 0

    while True:
        if N % factor_list[idx] == 0:
            print(factor_list[idx])
            N = N //factor_list[idx]
        else:
            idx+=1
        if N == 1:
            break

solver(int(input()))'''


N = int(input())
m = 2
while N!=1:  # N과m을 나눴을때 몫이 1이 되면 멈춤.
  if N%m==0:
    print(m)
    N = N//m
  else:
    m += 1



