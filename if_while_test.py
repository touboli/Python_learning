score = [100,79,65,87,97,65,87,97,67]
for i in range(len(score)-1,-1,-1):
    if score[i] > 80:
        score.pop(i)
print(score)