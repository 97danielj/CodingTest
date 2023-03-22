

def solver(M,  N):
    decimal_list = []

    for target in range(M, N+1):
        if target == 1:
            continue

        else:
            for i in range(2, target):
                if target % i == 0:
                    break
            else:
                decimal_list.append(target)

    if len(decimal_list) != 0:
        return sum(decimal_list), decimal_list[0]

    else:
        return -1

M = int(input())
N = int(input())

try:
    sum_decimal, min_decimal = solver(M , N)
    print(sum_decimal, min_decimal,  sep='\n')
except:
    none_decimal = solver(M,N)
    print(none_decimal)
