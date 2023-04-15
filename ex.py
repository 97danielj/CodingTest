
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
print(s1.volume)