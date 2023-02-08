n = int(input())
scores = list(map(int,input().split()))
max_score = max(scores)
new_scores = [i/max_score for i in scores]
print(100*sum(new_scores)/len(new_scores))