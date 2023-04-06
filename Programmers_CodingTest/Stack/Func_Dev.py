# 조건 : 진도 100일 떄 서비스 반영
# 입력 : 배열
# 리턴 : 배열

# progresses : 작업 진도 배열
# speeds : 개발 속도 배열
# return : 각 배포 마다 몇섹의 기능이 배포
# 배포는 하루의 끝

def solution(progresses, speeds):
    answer = []
    release = 0
    # 첫 번재 기능을 위한 릴리스 데이 계산
    rest_progresses = 100-progresses[0]
    past_days = rest_progresses // speeds[0]
    if rest_progresses % speeds[0] != 0:
        past_days += 1
    release += 1

    # 나머지 기능 들을 위한 릴리스 데이 계산
    for i in range(1, len(progresses)):
        if past_days*speeds[i] + progresses[i] >= 100:
            release += 1

        else: # 주어진 progress의 예상 일자 계산
            answer.append(release)
            release = 0
            rest_progresses = 100 - progresses[i]
            past_days = rest_progresses // speeds[i]
            if rest_progresses % speeds[i] != 0:
                past_days += 1
            release += 1

    else:
        answer.append(release)

    return answer

def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1

    print(Q)
    return [q[1] for q in Q]



print(solution2([93, 30, 55], [1, 30, 5]))



