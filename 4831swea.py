t = int(input())
for tc in range(1,t+1):
    # 이동거리:k , 0~n번 : n, 충전기 m개 정류장번호
    k, n, m = map(int, input().split())
    stops = list(map(int, input().split()))
    answer = 0
    tmp = 0
    cur = 0
    stop_dict = dict.fromkeys(range(101),0)
    for i in stops:
        stop_dict[i] = 1
    while cur + k < n:
        cur += k
        cnt = 0
        for i in range(k):
            cnt += 1
            if stop_dict[cur-i] == 1:
                answer += 1
                cur = cur - i
                cnt = 0
                break
        if cnt == k:
            answer = 0
            break

    print(f'#{tc}', answer)
