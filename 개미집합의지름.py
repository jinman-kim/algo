n = int(input())
n_num = list(map(int, input().split()))
m = int(input())
m_num = list(map(int, input().split()))
n_dict = { i: 1 for i in n_num}
for i in m_num:
    try:
        if n_dict[i] == 1:
            print(1)
    except:
        print(0)