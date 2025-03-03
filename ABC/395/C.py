from sys import stdin

input = stdin.readline

dp = dict()

n = int(input())
answer = n + 1

numbers = list(map(int, input().split()))

for i in range(n):
    if dp.get(numbers[i]) != None:
        answer = min(i - dp[numbers[i]] + 1, answer)
    dp[numbers[i]] = i

print(-1 if answer > n else answer)
