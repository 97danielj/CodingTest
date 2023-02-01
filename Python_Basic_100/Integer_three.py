a, b, c = map(int,input().split())

total_sum = sum((a,b,c))
avg = total_sum / 3

print(total_sum, "{0:.2f}".format(avg))
