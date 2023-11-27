# 비트마스크: 모든 경우의 수를 이진수로 변환하여 비트 연산을 통해 모든 경우의 수 를 탐색

# 장점: 하나의 변수에 여러개의 상태정보(집합, 권한, 상태)를 표현할 수 있음.
# 장점2:
# 단점: 이진수 변환

# 1. 권한 관리: 각 권한을 비트로 표현
PERMISSION_READ = 0b0001 << 0; # 0001
PERMISSION_WRITE = 0b0001 << 1; # 0010
PERMISSION_DELETE = 0b0001 << 2; # 0100
PERMISSION_EXECUTE = 0b0001 << 3; # 1000

print(PERMISSION_EXECUTE)
userPermission = PERMISSION_READ | PERMISSION_WRITE
print(userPermission)
groupPermission = PERMISSION_READ | PERMISSION_EXECUTE

hasReadPermission = (userPermission & PERMISSION_READ) != 0
print(hasReadPermission)
hasDeletePermission = groupPermission & PERMISSION_DELETE != 0
print(hasDeletePermission)
#출력문
#8
#3
#True
#False


# 2. 집합 관리: 집합을 비트로 표현
set = (1 << 3) | (1 << 5) | (1 << 7) #0010 1010 1000
hasElement5 = (set & (1 << 5)) != 0; #True
hasElement6 = (set & (1 << 6)) != 0; #False


# 3. 상태 플래그 관리: 여러 상태들을 하나의 정수값으로 나타내어 관리
# 2의 제곱과 음수를 확인 판단
FLAG_POWER_OF_TWO = 1 << 0; #0001
FLAG_NEGATIVE = 1 << 1; #0010

number = 8; # 2의 거듭제곱
flags = 0;

if number & (number-1) == 0 :
    flags |= FLAG_POWER_OF_TWO


if (number < 0):
    flags |= FLAG_NEGATIVE
    print(flags)


if ((flags & FLAG_POWER_OF_TWO) != 0):
    print(number, " is power of two") #1

if ((flags & FLAG_NEGATIVE != 0)):
    print(number, "is negaive") # 2




