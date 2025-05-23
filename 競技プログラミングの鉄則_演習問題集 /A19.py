from sys import stdin

input = stdin.readline

N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (W + 1)

for w, v in items:
  for j in range(W, w - 1, -1):
    dp[j] = max(dp[j], dp[j - w] + v)
    
print(max(dp))