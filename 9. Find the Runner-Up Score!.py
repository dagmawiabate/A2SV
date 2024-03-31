n = int(input())
scores = list(map(int, input().split()))

# Sort the scores in descending order
scores.sort(reverse=True)

# Find the runner-up score
runner_up_score = None
for score in scores:
    if score < scores[0]:
        runner_up_score = score
        break

print(runner_up_score)
