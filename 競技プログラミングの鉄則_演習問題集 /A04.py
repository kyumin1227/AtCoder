n = int(input())

binary_list = [False for _ in range(10)]

for i in range(9, -1, -1):
  if n % 2 == 1:
    binary_list[i] = True
    
  n //= 2
  
for b in binary_list:
  print("1" if b else "0", end="")