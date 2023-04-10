def solution(players, callings):
    answer, rank, name= [], dict(), dict()
    for i,j in enumerate(players):
        rank[i+1] = j  # 3: kai
        name[j] = i + 1 # kai : 3
    for i in callings:
        tmp = rank[name[i]-1] #3등기억
        name[i] -= 1 #4등이 3등이됨
        name[tmp] += 1 #3등이 4등이됨
        rank[name[i]] = i # 3:kai
        rank[name[i] + 1] = tmp # 4: poe
    return [i[1] for i in rank.items()]