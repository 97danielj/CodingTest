'''
class Stock:
    market = "kospi"

s1 = Stock()
s2 = Stock()

print(dir())
print(Stock.__dict__) #해당객체의 네임스페이 내 변수: 값 형태
print(dir(Stock)) #해당 객체의 네임스페이스 이름만
print(s1.__dict__)

s1.market = "kosdaq"
print(s1.__dict__)
print(s1.market)
print(s2.market)


s1 = "bitcoinisgood"
s2 = "bitcoin"
def stringCompare(s1, s2):
    length_s1 = len(s1)
    length_s2 = len(s2)

    small_length = min(length_s1, length_s2)

    for i in range(small_length):
        if s1[i] != s2[i]:
            return ord(s1[i]) - ord(s2[i])

    if (length_s1 == length_s2):
        return 0
    elif length_s1 > length_s2:
        return s1[small_length]
    else:
        return s2[small_length]
'''


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