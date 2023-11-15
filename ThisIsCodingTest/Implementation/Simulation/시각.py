# 입력 : 첫재 줄에 정수 N이 입력
# 출력 : 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력하비낟.



def solver(n):
    count = 0
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                # 매시각 안에 '3'이 포함되어 있다면 카운트 증가
                if '3' in str(i)+str(j)+str(k): #우리가 보는 시각
                    count += 1
    return count

n = int(input())

print(solver(n))