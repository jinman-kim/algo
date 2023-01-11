def solution(board, moves):
    cart = []
    for m in moves:     # 카트에 담기
        for b in board:
            if b[m-1] == 0:
                pass
            elif b[m-1] != 0:
                cart.append(b[m-1])
                b[m-1] = 0
                break
    tmp = len(cart)     # 카트 길이 기억
    import time
    start = time.time()     # 시작 시간 기억
    while True:         # 같으면 팡팡 터뜨리기
        for i in range(len(cart)-1):    # 인덱스 꼬일까 봐 range(len( ))
            if cart[i] == cart[i+1]:
                cart[i] = 0     # 0으로 치환 idx
                cart[i+1] = 0   # 0으로 치환 idx+1
        for _ in cart:      # 카트에 0제거 
            if 0 in cart:
                cart.remove(0)
        if time.time()-start > 0.01:    # 0.01초 이상 돌면 끝
            break
    return tmp - len(cart)


board = [[1,0,0,0,3],
         [0,0,1,0,3],
         [0,2,5,0,3],
         [4,2,4,4,3],
         [3,5,1,3,0]]

moves = [5,5,5,5,5]
print(solution(board,moves))