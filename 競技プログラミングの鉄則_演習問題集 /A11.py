from sys import stdin

input = stdin.readline

n, x = map(int, input().split())
vector = list(map(int, input().split()))

left = 0
right = len(vector) - 1

while left <= right:
  mid = (left + right) // 2
  
  if (vector[mid] == x):
    print(mid + 1)
    break
  elif (vector[mid] < x):
    left = mid + 1
  else:
    right = mid - 1
