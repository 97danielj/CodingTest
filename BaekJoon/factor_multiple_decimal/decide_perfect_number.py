
def solver(n):
    factor_list = []
    for i in range(1, n):
        if n % i ==0:
            factor_list.append(i)

    if sum(factor_list) == n:
        print(f'{n} =', end='')
        for i in range(len(factor_list)):
            if i == len(factor_list)-1:
                print(f' {factor_list[i]}')
            else:
                print(f' {factor_list[i]} +', end='')
    else:
        print(f'{n} is NOT perfect.')


while True:
    n = int(input())
    if n == -1:
        break
    solver(n)