
def transfer_credit_to_score(subject_credit_list):
    for i in range(len(subject_credit_list)):
        if subject_credit_list[i] == 'A+':
            subject_credit_list[i] = 4.5
        elif subject_credit_list[i] == 'A0':
            subject_credit_list[i] = 4.0
        elif subject_credit_list[i] == 'B+':
            subject_credit_list[i] = 3.5
        elif subject_credit_list[i] == 'B0':
            subject_credit_list[i] = 3.0
        elif subject_credit_list[i] == 'C+':
            subject_credit_list[i] = 2.5
        elif subject_credit_list[i] == 'C0':
            subject_credit_list[i] = 2.0
        elif subject_credit_list[i] == 'D+':
            subject_credit_list[i] = 1.5
        elif subject_credit_list[i] == 'D0':
            subject_credit_list[i] = 1.0
        elif subject_credit_list[i] == 'F':
            subject_credit_list[i] = 0.0


subject_grade_list = []
subject_credit_list = []
for i in range(20):
    current_subject = input().split()
    if current_subject[2] != 'P':
        subject_grade_list.append(float(current_subject[1]))
        subject_credit_list.append(current_subject[2])

transfer_credit_to_score(subject_credit_list) #등급 점수로 변환 과정

total_sum = 0
for i in range(len((subject_credit_list))):
    total_sum += (float(subject_grade_list[i]) * subject_credit_list[i])


mean_credit = total_sum / sum(subject_grade_list)
print("{:.6f}".format(mean_credit))




