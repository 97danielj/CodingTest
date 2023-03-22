
def expressing_goldbach(goldbach_n, decimal_list):
   

    a, b = goldbach_n//2, goldbach_n//2

    while a>0:
        if a in decimal_list and b in decimal_list:
            return a, b
        else :
            a -= 1
            b += 1







def find_decimals(goldbach_n):
    #goldbach_n 보다 작은 소수를 찾는다.
    decimal_list = []
    for target in range(2, goldbach_n):
        for i in range(2, target):
            if target % i == 0:
                break
        else:
            decimal_list.append(target)

    return expressing_goldbach(goldbach_n, decimal_list)




T = int(input())

for i in range(T):
    print(*find_decimals(int(input())))
