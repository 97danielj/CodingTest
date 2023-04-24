from collections import Counter

text = "gallahad"
c = Counter(text)

print(c)
print(c['a'])

d1 = dict({'k1' : '현대', 'k2' : '한화'})
print(list(c.elements()))


c1 = Counter(cats = 8, dogs = 12)
print(c1)