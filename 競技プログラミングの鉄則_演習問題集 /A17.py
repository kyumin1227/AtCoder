from sys import stdin

input = stdin.readline

n = int(input())

one = list(map(int, input().split()))
two = list(map(int, input().split()))

dp = [0] * n

dp[1] = one[0]

for i in range(2, n):
  dp[i] = min(dp[i - 1] + one[i - 1], dp[i - 2] + two[i - 2])


route = []

def append_route(arg_room):
  route.append(arg_room + 1)
  if arg_room == 0:
    return
  
  if arg_room > 1 and dp[arg_room - 1] + one[arg_room - 1] >= dp[arg_room - 2] + two[arg_room - 2]:
    return append_route(arg_room - 2)
  else:
    return append_route(arg_room - 1)
  
append_route(n - 1)

print(len(route))
print(*route[::-1])