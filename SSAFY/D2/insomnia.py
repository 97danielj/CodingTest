T = int(input())
for test_case in range(1, T + 1):
    count_list = [0]*10
    #print(len(count_list))
    N = input() #배수가 될 N
    count = 1
    while True:
        N_multiples = int(N) * count
        N_multiples = str(N_multiples)
        for i in N_multiples:
            i = int(i)
            count_list[i] += 1
        count += 1
        if count_list.count(0) == 0:
            print('#{}'.format(test_case), int(N_multiples))
            break

