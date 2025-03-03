from sys import stdin

input = stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

for i in range(1, n):
    if numbers[i - 1] >= numbers[i]:
        print("No")
        exit()

print("Yes")