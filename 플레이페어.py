import string
import numpy as np

a = 'HELLOWORLD'
b = 'PLAYFAIRCIPHERKEY'
# a = input()
# b = input()
#1st
alpha = dict.fromkeys(string.ascii_uppercase,0)
del alpha['J']
arr = []
for i in b:
    if alpha[i]==0:
        alpha[i] = 1
        arr.append(i)
for i,j in alpha.items():
    if j == 0:
        arr.append(i)
array = []
array.append(arr[0:5])
array.append(arr[5:10])
array.append(arr[10:15])
array.append(arr[15:20])
array.append(arr[20:25])

#2nd
#1. 같은행에서 밀기
#2. 같은열에서 밀기
#3. 다른행, 다른열
#4. HE LX LO WO RL DX
#5. EI YV RV VQ BR GW
new_a = ''
a = list(a)
while a:
    if len(a) == 1:
        new_a += a[0]
        new_a += 'X'
        break
    if a[0] == 'X' and a[1] == 'X':
        a.insert(1,'Q')
    else:
        if a[0] == a[1]:
            a.insert(1,'X')
        if a[0] != a[1]:
            new_a += a[0]
            a.pop(0)
            new_a += a[0]
            a.pop(0)
            new_a += ' '
key = []
for i in new_a.split():
    key.append(i)
# print(key)

location_alpha = {}
for i,j in alpha.items():
    location_alpha[i] = (0,0)
for i in range(5):
    for j in range(5):
        location_alpha[array[i][j]]=(i,j)
# print(location_alpha)
ans = []
for two in key:
    a=two[0]
    b=two[1]
    a_idx = location_alpha[a]
    b_idx = location_alpha[b]
    #1
    if(a_idx[0]==b_idx[0]):
        if(a_idx[1]+1==5):
            ans.append(array[a_idx[0]][0])
        else:
            ans.append(array[a_idx[0]][a_idx[1]+1])
        if(b_idx[1]+1==5):
            ans.append(array[b_idx[0]][0])
        else:
            ans.append(array[b_idx[0]][b_idx[1]+1])
    #2
    elif(a_idx[1]==b_idx[1]):
        if(a_idx[0]+1==5):
            ans.append(array[0][a_idx[1]])
        else:
            ans.append(array[a_idx[0]+1][a_idx[1]])
        if(b_idx[0]+1==5):
            ans.append(array[0][b_idx[1]])
        else:
            ans.append(array[b_idx[0]+1][b_idx[1]])
    #3
    else:
        ans.append(array[a_idx[0]][b_idx[1]])
        ans.append(array[b_idx[0]][a_idx[1]])
print(array)
res =''
for c in ans:
    res += c

print(res)