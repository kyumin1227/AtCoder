from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
boxs = []

for _ in range(4):
  boxs.append(list(map(int, input().split())))

now = []

def bruteforce():
  
  if sum(now) > k:
    return
  
  if len(now) == 4:
    if sum(now) == k:
      print("Yes")
      exit(0)
    return
      
  for i in range(n):
    now.append(boxs[len(now)][i])
    bruteforce()
    now.pop()

bruteforce()

print("No")