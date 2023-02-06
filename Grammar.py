def num_to_base(num, base):
    answer = 0
    for idx, number in enumerate(num[::-1]):
        answer += int(number) * (base**idx)
    return answer
print(num_to_base('4331',5))

def str_sort(s, n):
    print(s.ljust(n))
    print(s.center(n))
    print(s.rjust(n))
    return
print(str_sort('abc',7))