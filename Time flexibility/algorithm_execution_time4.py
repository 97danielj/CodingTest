'''
MenOfPassion(A[], n) {
    sum <- 0; 1
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1 14
    return sum;
}
'''


n = int(input())

# 이중 for문
print((n-1)*(n)//2)
print(2)