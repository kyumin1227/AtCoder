from sys import stdin

input = stdin.readline

n, q = map(int, input().split())

visitor_list = list(map(int, input().split()))
dp = [0, visitor_list[0]]

for i in range(1, n):
  dp.append(dp[i] + visitor_list[i])

for _ in range(q):
  start_day, end_day = map(int, input().split())
  
  print(dp[end_day] - dp[start_day - 1])