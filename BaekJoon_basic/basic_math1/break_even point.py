

def calc_break_even(A, B, C):

    if B >= C :
        return -1

    profit_per_product = C - B
    break_even = A // profit_per_product + 1
    return break_even





A, B, C = list(map(int,input().split()))
print(calc_break_even(A, B, C))




