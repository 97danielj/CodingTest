'''def solution(participant, completion):
    answer = None
    part_dict = dict()

    for i in participant:
        if i in part_dict.keys():
            part_dict[i] += 1
        else:
            part_dict[i] = 1

    for i in completion:
        part_dict[i] -= 1

    for k, i in part_dict.items():
        if i != 0:
            return k


print(solution(["leo", "kiki", "eden"],["eden", "kiki"] ))'''



