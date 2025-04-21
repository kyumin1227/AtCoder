from sys import stdin

input = stdin.readline

n, a, b = map(int, input().split())

answer = 0

for num in range(n + 1):

    string_num = str(num)
    sum_num = 0

    for c in string_num:
        sum_num += int(c)
    
    if sum_num >= a and sum_num <= b:
        answer += num

print(answer)