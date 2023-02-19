# 세준이의 성적 조작
# 최댓값 : M
# 수식 : 점수/M*100

N = input()
score_list = list(map(int, input().split()))

M = max(score_list)

for i in range(len(score_list)):
    new_score = score_list[i]/M*100
    score_list[i] = new_score

print(sum(score_list) / len(score_list))
