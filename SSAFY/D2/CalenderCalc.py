T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
month_date_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
#print(len(month_date_list))
for test_case in range(1, T + 1):
    date = input().split()
    date = list(map(int,date))
    first_date = date[:2]
    second_date = date[2:]

    # 두 번째 날짜를 모든 day로 변경
    # 첫 번째 날짜를 모든 day로 변경
    # 두 day의 차를 출력

    first_day_sum = 0
    for i in range(first_date[0]):
        first_day_sum += month_date_list[i]
        if i == first_date[0] - 1:
            first_day_sum += first_date[1]

    second_day_sum = 0
    for i in range(second_date[0]):
        second_day_sum += month_date_list[i]
        if i == second_date[0] - 1:
            second_day_sum += second_date[1]

    print(f'#{test_case}', second_day_sum-first_day_sum+1)

