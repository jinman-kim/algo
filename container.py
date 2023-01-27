#이분탐색, two pointer O(n)
def solution(height):
    start = 0
    end = len(height)-1
    water = 0
    while start < end:
        temp_water = min(height[start], height[end])*abs(end-start)
        water = max(temp_water,water)

        if height[start] < height[end]:
            start +=1
        else:
            end -= 1

    return water


height = [1,8,6,2,5,4,8,3,7]
print(solution(height))