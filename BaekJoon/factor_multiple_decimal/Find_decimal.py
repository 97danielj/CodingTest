# N개의 수 중 소수의 개수를 출력
# 소수는 약수로 1과 자기 자신을 가진다.
def solver(num_list):
    decimal_list  = []
    for target in num_list:
        if target == 1:
            continue

        else:
            for i in range(2, target):
                if target % i == 0: #한번이라도 1, target제외 약수가 존재하면
                    break
            else:
                decimal_list.append(target)

    return len(decimal_list)




N = input()

num_list = list(map(int, input().split()))

print(solver(num_list))
