from itertools import product
def solution(word):
    words = []
    for i in range(1,6):
        for char in product('AEIOU',repeat=i):
            words.append(''.join(list(char)))
    words.sort()
    return words.index(word)+1
print(solution("AAAE"))