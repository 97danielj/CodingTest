import re

s = "[403]James"


def solution(rooms, target):
    # 이미 지정 자리가 있는 직원은 제외
    pattern = r"\[(\d+)\]"
    employees = [room for room in rooms if int(re.search(pattern, room).group(1)) != target]

    #for i in range()

    # 지정 자리 수가 가정 적은 직원 순으로 정렬



rooms1 = ["[403]James", "[404]Azad, Louis, Andy", "[101]Azad, Guard"]

solution(rooms1, 403)
