def solution(plans):
    answer, hw, hw_start, process, stop = [], {}, {}, [],[]
    for i in plans:
        hw[i[0]] = int(i[2]) # 숙제 소요 시간 ,(남는시간)
        hw_start[i[0]] = int(i[1].split(':')[0]) * 60 + int(i[1].split(':')[1])
    hw_start = sorted(hw_start.items(),key=lambda x:x[1]) #먼저 해야하는 순서
    for i in range(0,100000):
        try: #시작시간이 일치하면 프로세스에 추가
            if i == hw_start[0][1]:
                tmp = hw_start.pop(0)
                process.append(tmp[0])
        except:
            pass
        try:
            hw[process[0]] -= 1
            if hw[process[0]] == 0:
                answer.append(process.pop(0))
        except:
            pass
        if len(process) == 2:
            stop.append(process.pop(0))
        if not process and stop:
            process.append(stop.pop(-1))
    return answer


plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
print(solution(plans))