def is_prime(num):
    if num == 1 or num == 0:
        return 0
    else:
        cnt = 2
        for i in range(2,num):
            if num % i == 0:
                break
            else:
                cnt += 1
        if cnt == num:
            return num


def solution(nums):
    answer = 0
    from itertools import combinations
    for num in combinations(nums,3):
        if is_prime(sum(num)):
            answer+=1
    return answer


nums = [1,2,7,6,4]
print(solution(nums))