def solution(numbers):
    answer = []
    # 1. 필요한 자릿수를 구한다.
    extended_0 = len(str(max(numbers)))
    #print(extended_0)

    # 2. 입력 배열을 문자열로 변환한다.

    numbers_int = list(map(str,numbers))
    #print(numbers_int)

    # 3. 정해진 자릿수에 맞게 각 원소 앞에 0을 삽입

    for i in range(len(numbers_int)):
        target = numbers_int[i]
        while len(target) < extended_0:
            target = "0"+target
        answer.append(target)

    return answer