X = int(input())

line = 1
while X>line:
    X-=line #줄 n일 때 대각선에 존재하는 분수를 빼주면 된다.

    line += 1

if line%2 ==0: #'현재 줄이 짝수번째' -> 분자 오름차순, 분모 내림차순
    a = X #
    b = line-X+1
else:
    a = line-X+1
    b = X


print(a, '/', b, sep='')