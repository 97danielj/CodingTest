def solver(A, B):
    if B % A == 0:
        return "factor"
    elif A % B == 0:
        return "multiple"
    else:
        return "neither"

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(solver(A, B))


