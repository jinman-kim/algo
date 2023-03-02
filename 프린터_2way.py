from collections import deque
def solution(priorities, location):
    loc = [[idx,priority] for idx,priority in enumerate(priorities)]
    answer = []
    while loc:
        tmp = loc.pop(0)
        len_loc = len(loc)
        for i in loc:
            if i[1] > tmp[1]:
                loc.append(tmp)
                break
        if len_loc == len(loc):
            answer.append(tmp)
    result = 0
    for i in answer:
        result += 1
        if i[0] == location:
            break
    return result


priorities = [1,1,9,1,1,1]
location = 0
print(solution(priorities,location))