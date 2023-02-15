user = []
for _ in range(int(input())):
    age, name = map(str,input().split())
    age = int(age)
    user.append((age,name))
for i in sorted(user,key=lambda x:x[0]):
    print(i[0],i[1])
