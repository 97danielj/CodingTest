
# 요구 사항 : 여행을 떠날 수 있는 그룹의 최댓값
# 제한 사항 :
# 요구조건 : 1. 공포도가 X 인 모험가는 반드시 X명 이상 으로 구성한 모험가 그룹 참여
# 입력 : N명의 길드원
# 출력 : 여행을 떠날 수 있는 그룹의 최댓값

T = input()
fear_list = input().split()




# 여행을 떠날 수 있는 그룹의 최댓값 출력
#그리드 방식? => 항상 그룹은 최소한의 모험가의 수만 포함하여 그룹을 결성

# 아이디어 : 1. 그리드 방식 / 2. 오름차순 정렬 / 3. '현재 그룹의 모험가의 수'가 '현재 확인하고 있는 공포도'보다 크거나 같다면 결성

def solution(fear_list):
    fear_list = list(map(int, fear_list))
    fear_list.sort()
    print(fear_list)
    group_member = 0
    group_count = 0
    for fear in fear_list:
         group_member += 1
         if group_member >= fear:
             group_count += 1
             group_member = 0

    return group_count



print(solution(fear_list))



