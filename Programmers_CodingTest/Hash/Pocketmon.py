# 나는 많은 포켓몬을 가지길 원한다.
# 입력 : N마리 폰켓몬의 종류 번호가 담긴 배열 nums
# 출력 : N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 그때의 폰켓몬 종류 번호의 개수를 return

# 즉. 최대 출력 가능한 폿켓몬 종류의 수
# 제한 사항



def solution(nums):
    pocket_count = len(nums) // 2
    pocket_dict = dict()
    for i in nums:
        if i not in pocket_dict.keys():
            pocket_dict[i] = 1
        else:
            pocket_dict[i] += 1

    pocket_dict = dict(sorted(pocket_dict.items(), key= lambda x:x[1]))
    count = 0

    for i in pocket_dict.keys():
        count += 1
        if count == pocket_count:
            break
    return count

print(solution([3,3,3,2,2,2]))