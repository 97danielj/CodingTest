# 단어 공부


def solver(str):
    str = str.lower()
    alpha_set = set()

    # set()함수로 무슨 문자가 있는지 안다.
    for i in str:
        alpha_set.add(i)

    # 1개일 경우 바로 문자 반환
    if len(alpha_set) == 1:
        return str[0].upper()


    # 문자가 2개 이상이면
    # dict생성하여 각 문자가 str에 몇 개존재하는 지 안다.
    alpha_dict = {}
    for char in alpha_set:
        alpha_dict[char] = str.count(char)

    alpha_dict = dict(sorted(alpha_dict.items(), key=lambda x : x[1], reverse=True))
    count_list = list(alpha_dict.values())
    if count_list[0] == count_list[1]:
        return "?"

    else:
        return list(alpha_dict.keys())[0].upper()



print(solver(input()))
