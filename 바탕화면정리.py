def solution(wallpaper):
    answer = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                answer.append([i,j])
    dot = []
    answer.sort(key=lambda x:x[0])
    dot.append(answer[0][0])
    dot.append(answer[-1][0]+1)
    answer.sort(key=lambda x:x[1])
    dot.insert(1,answer[0][1])
    dot.append(answer[-1][1]+1)
    return dot