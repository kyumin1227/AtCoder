n, k = map(int, input().split())
numbers = list(map(int, input().split()))

right = 0
answer = 0

for left in range(n):
  while right < n and numbers[right] - numbers[left] <= k:
    right += 1
    
  answer += right - left - 1
  
print(answer)