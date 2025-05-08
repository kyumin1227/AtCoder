n, x = map(int, input().split())

num_list = list(map(int, input().split()))

is_exist = False

for num in num_list:
  if num == x:
    is_exist = True
    
print("Yes" if is_exist else "No")
