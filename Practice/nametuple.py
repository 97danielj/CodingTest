# 구조체, C에서 struct랑 동일 역할

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)

print(p)

print(p[0]+p[1])