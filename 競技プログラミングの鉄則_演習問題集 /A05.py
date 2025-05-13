n, k = map(int, input().split())

answer = 0

for red in range(1, min(n + 1, k - 1)):
  for blue in range(1, min(n + 1, k - red)):
    if (k - red - blue <= n):
      answer += 1
        
print(answer)