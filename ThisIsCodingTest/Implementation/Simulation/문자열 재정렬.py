
sex = input()


def solver(sex):
    result = []
    sum_n = 0
    for i in sex:
        if i.isalpha():
            result.append(i)
        else:
            sum_n += int(i)


    for i in result:
        print(i,end='')
    print(sum_n)

solver(sex)