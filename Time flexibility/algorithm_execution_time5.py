'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''


# 출력 : 1. 코드 1의 수행 횟수, 2. 다항식 촤고차항 차수

n = int(input())
print(n**3)
print(3)