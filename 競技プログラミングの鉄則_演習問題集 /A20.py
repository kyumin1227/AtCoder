F = list(input())
S = list(input())

f = len(F)
s = len(S)

dp = [[0] * (s + 1) for _ in range(f + 1)]

for i in range(1, f + 1):
  for j in range(1, s + 1):
    if F[i - 1] == S[j - 1]:
      dp[i][j] = dp[i - 1][j - 1] + 1
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
      
print(dp[f][s])