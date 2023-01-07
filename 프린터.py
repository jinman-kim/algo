def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
            print(queue)
        else:
            answer += 1
            if cur[0] == location:
                return answer
# 가장 앞에있는 j
# 나머지 중 j보다 중요한게있으면 j를 가장 마지막에
# 그렇지 않으면 j 인쇄

priorities = [1,1,2,4,9,5,3,10,1]
location = 0
print(solution(priorities,location))