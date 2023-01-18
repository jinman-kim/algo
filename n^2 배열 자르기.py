def two_dim_array(n, left, right): #시간초과
    answer = [[i+1 if j<i else j+1 for j in range(n)] for i in range(n)]
    slice = []
    for i in answer:
        slice += i
    return slice[left:right+1]

def div_mod(n ,left, right):
    answer = []
    for i in range(left,right+1):
        a = i//n
        b = i % n
        if b > a:
            b,a = a,b
        answer.append(a+1)
    return answer

n = 4
left,right = 7,14
print(div_mod(n,left,right))