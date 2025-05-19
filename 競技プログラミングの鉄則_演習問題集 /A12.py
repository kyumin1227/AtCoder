n, k = map(int, input().split())
printers = list(map(int, input().split()))

left = 0
right = 10 ** 9
answer = right

while left <= right:
  mid = (left + right) // 2
  total = sum(mid // num for num in printers)
  
  if total >= k:
    answer = mid
    right = mid - 1
  else:
    left = mid + 1
    
print(answer)