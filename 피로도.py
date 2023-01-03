def solution(k,dungeons):
    from itertools import permutations
    num = [0]*len(list(permutations(dungeons,len(dungeons))))
    route = list(permutations(dungeons,len(dungeons)))
    for i in range(len(route)):
        tmp=k
        for j in route[i]:
            if j[0] > tmp:
                break
            else:
                tmp -= j[1]
                num[i] += 1
    answer = max(num)
    return answer
k=80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k,dungeons))