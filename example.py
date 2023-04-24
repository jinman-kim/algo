def solution(plans):
    import copy
    plans.sort(key=lambda x:x[1])
    answer = []
    starttime = []
    time = [int(i[2]) for i in plans]
    c = 0
    for i in plans:
        spl = i[1].split(':') # spl = ['12','20']
        spl[0] = int(spl[0])
        spl[1] = int(spl[1])
        starttime.append(spl)
    realtime = copy.deepcopy(starttime[0]) #시작시간
    while c < len(plans):
        if realtime[1] == 60:
            realtime[0] += 1
            realtime[1] = 0
        if realtime[0] == 24:
            realtime[0] = 0
        if time[c] == 0: #잔여 공부시간
            if plans[c][0] not in answer:
                answer.append(plans[c][0])
                c += 1
                for i in reversed(range(len(time))):
                    if time[i] != 0 and c > i:
                        c = i
                        break
                continue
        for i in range(len(starttime)):
            #분과 시간이 같으면
            if starttime[i][0] == realtime[0] and starttime[i][1] == realtime[1]:
                c = i
                break
        if c == len(plans):
            break
        if time[c] == 0 and c != len(plans)-1:
            c += 1
            continue
        if time[c] == 0 and c == len(plans)-1:
            break
        time[c] -= 1
        realtime[1] += 1
    return answer