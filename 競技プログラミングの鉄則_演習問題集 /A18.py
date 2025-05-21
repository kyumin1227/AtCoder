n, s = map(int, input().split())

cards = list(map(int, input().split()))

now = []

def bruteforce(index, sum_now):
  if sum_now == s:
    print("Yes")
    exit(0)
  
  elif sum_now > s:
    return
  
  for i in range(index, n):
    sum_now += cards[i]
    now.append(i)
    bruteforce(i + 1, sum_now)
    now.pop()
    sum_now -= cards[i]
    
bruteforce(0, 0)
print("No")