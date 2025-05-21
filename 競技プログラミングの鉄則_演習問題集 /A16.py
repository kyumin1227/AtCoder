from sys import stdin

input = stdin.readline

n = int(input())
one_step = list(map(int, input().split()))
two_step = list(map(int, input().split()))

dp = [0] * n

dp[1] = one_step[0]
dp[2] = min(one_step[0] + one_step[1], two_step[0])

for i in range(2, n):
  dp[i] = min(dp[i - 1] + one_step[i - 1], dp[i - 2] + two_step[i - 2])

print(dp[n - 1])