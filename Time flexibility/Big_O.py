
a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

f_n = a1*n0 + a0
g_n = c*n0


if f_n <= g_n:
    print(1)
else:
    print(0)
