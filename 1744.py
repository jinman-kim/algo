n = int(input())
if n == 1:
    print(int(input()))
else:
    answer = 0
    p, m = [], []
    zzatoori = []
    for _ in range(n):
        a = int(input())
        if a > 1:
            p.append(a)
        elif a == 1:
            zzatoori.append(a)
        elif a == 0:
            zzatoori.append(a)
        else:
            m.append(a)

    p.sort(reverse=True); m.sort()

    while p:#큰 양수부터
        a = p.pop(0)
        if not p:
            zzatoori.append(a)
            break
        b = p.pop(0)
        answer += max((a+b), a*b)

    while m:
        a = m.pop(0)
        if not m:
            zzatoori.append(a)
            break
        b = m.pop(0)
        answer += max((a+b), a*b)
    zzatoori.sort()
    if len(zzatoori) == 4:
        answer += zzatoori[0] * zzatoori[1] + zzatoori[2] + zzatoori[3]
    elif len(zzatoori) == 1:
        answer += zzatoori[0]
    elif len(zzatoori) == 2:
        answer += max(zzatoori[0]+zzatoori[1], zzatoori[0]*zzatoori[1])
    elif len(zzatoori) == 3:
        answer += max(zzatoori[0]+zzatoori[1]+zzatoori[2], zzatoori[0]*zzatoori[1]+zzatoori[2],zzatoori[0]+zzatoori[1]*zzatoori[2])
    print(answer)




# 2000 1000 5 -5 -100
