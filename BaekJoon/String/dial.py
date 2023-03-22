# 할머니가 단어를 이용하여 전화를 걸기위해 다이얼을 돌리는데 소요 시간

alpha_to_dial = {'a' : 2, 'b': 2, 'c': 2, 'd': 3, 'e':3, 'f':3,\
                 'g':4, 'h' : 4, 'i' : 4, 'j' : 5, 'k' : 5, 'l' : 5, 'm' : 6, 'n' : 6, 'o': 6,\
                 'p': 7, 'q' : 7, 'r' : 7, 's' : 7, 't' : 8,'u': 8,'v' : 8,
                 'w' : 9,'x' : 9,'y' : 9,'z' :9
                 }

text = input()
text = text.lower()

total_time = 0
for i in text:
    dial = alpha_to_dial[i]
    total_time += (dial + 1)

print(total_time)




