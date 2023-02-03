# 재귀 함수

natural_num = set(range(1,10001))
generated_num = set() #생성자 집합

for i in range(1, 10001): # i = 650 #모든 수에 대하여
    for j in str(i): # j = "6", "5", "0"
        i += int(j) # 650 + 6 + 5 + 0, i = 661
    generated_num.add(i) #생성자 집합에 추가 # 정수 n에 대하여 d(n)을 구하면 d(n)을 생성자에 넣는다.

self_num_list=list(sorted(natural_num - generated_num))
for i in self_num_list:
    print(i)
