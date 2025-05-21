# from sys import stdin

# input = stdin.readline

# n = int(input())

# one = list(map(int, input().split()))
# two = list(map(int, input().split()))

# dp = [0] * n

# dp[0] = 0
# dp[1] = one[0]

# for i in range(2, n):
#   dp[i] = min(dp[i - 1] + one[i - 1], dp[i - 2] + two[i - 2])


# route = []

# def append_route(arg_room):
#   route.append(arg_room + 1)
#   if arg_room == 0:
#     return
  
#   if dp[arg_room - 1] + one[arg_room - 1] == dp[arg_room]:
#     return append_route(arg_room - 1)
#   else:
#     return append_route(arg_room - 2)
  
# append_route(n - 1)

# print(len(route))
# print(*route[::-1])

n = int(input())

one = list(map(int, input().split()))
two = list(map(int, input().split()))

dp = [None] * (n + 1)

dp[1] = 0
dp[2] = one[0]

for i in range(3, n + 1):
  dp[i] = min(dp[i - 1] + one[i - 2], dp[i - 2] + two[i - 3])
  
route = []
point = n

while True:
  route.append(point)
  if point == 1:
    break
  
  if dp[point] == dp[point - 1] + one[point - 2]:
    point -= 1
  else:
    point -= 2
    
route.reverse()
print(len(route))
print(*route)