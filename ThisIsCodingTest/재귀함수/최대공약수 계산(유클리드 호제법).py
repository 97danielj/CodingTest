
def gcd(A, B):
    while B > 0:
        A, B = B, A % B
    return A

def lcm(A,B):
    return A * B / gcd(A, B)

numbers = list(map(int,input().split()))

A = numbers[0]
B = numbers[1]

print(f"gcd : {gcd(A, B)}")
print(f"lcm : {int(lcm(A, B)) }")
