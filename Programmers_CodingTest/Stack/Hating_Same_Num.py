#입력 : 배열
#리턴 : 배열

def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    current_value = arr[0]
    answer.append(current_value)
    for i in range(1, len(arr)):
        if current_value != arr[i]:
            answer.append(arr[i])
        current_value = arr[i]
    return answer


print(solution([1,1,3,3,0,1,1]))

