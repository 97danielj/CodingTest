numbers = list(map(int,input().split()))

A = numbers[0]
B = numbers[1]

def gcd(A, B):
    if A%B ==0:
        return B
    else:
        return gcd(B, A % B)


print(gcd(192,162))