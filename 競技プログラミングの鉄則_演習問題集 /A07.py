from sys import stdin

input = stdin.readline

d = int(input())
n = int(input())

days = [0 for _ in range(d + 1)]

for _ in range(n):
  start_day, end_day = map(int, input().split())
  
  days[start_day - 1] += 1
  days[end_day] -= 1
    
# 出力
answer = 0
for i in range(d):
  answer += days[i]
  print(answer)