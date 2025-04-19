from sys import stdin

input = stdin.readline

s = input().strip()

answer = 0

for c in s:
    if c == '1':
        answer += 1

print(answer)
