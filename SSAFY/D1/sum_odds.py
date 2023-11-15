
T = int(input())
sum_list = list()
for test_case in range(1,T+1):
    tmp = list()
    line_number = input().split()
    line_number = list(map(int,line_number))
    for i in line_number:
        if i%2 == 1:
            tmp.append(i)
    sum_list.append(sum(tmp))
    if test_case == T:
        for i in range(T):
            print(f'#{i+1}', sum_list[i])
