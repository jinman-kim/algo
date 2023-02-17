def solution(cards1, cards2, goal):
    for i in goal[:]:
        if cards1 and i == cards1[0]:
            cards1.remove(i)
            goal.remove(i)
        elif cards2 and i == cards2[0]:
            cards2.remove(i)
            goal.remove(i)
    return 'Yes' if not goal else 'No'

cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
