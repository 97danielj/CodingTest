

T = int(input())
for i in range(1,T+1):
    participants = int(input())
    locations = input().split()
    locations = list(map(int,locations))
    for i in range(len(locations)):
        if locations[i] < 0:
            locations[i] = -locations[i]
    min_value = min(locations)
    min_count = locations.count(min_value)

    print("#{}".format(i), min_value, min_count)