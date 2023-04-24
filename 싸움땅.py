n, m, k = map(int, input().split())
guns = [list(map(int,input().split())) for _ in range(n)]
players = [list(map(int,input().split())) for _ in range(m)]
for i in guns:
    print(i)
#플레이어의 정보
#한칸씩 움직임
#플레이어를 만나면 이긴사람이 공격력 차이만큼 포인트 얻음
#근데 공격력 같으면 초기공격력이 센애가 이김김for i in players:
    print(i)