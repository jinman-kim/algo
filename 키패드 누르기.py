def solution(numbers, hand):
    answer = ''
    left_tmp,right_tmp = (3,0),(3,2)
    phone = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    now = [[0,0,0] for i in range(5)]
    def dfs(now, i , visited):

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            x = x + dx[i]
            y = y + dy[i]

    print(now)
    while phone:
        v,idx = phone.pop(),phone.index(1)
        if 4 in v:
            print('v')
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers,hand))