from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

count = 0
check = [[i == j for i in range(n + 1)] for j in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())

    if u == v:
        count += 1
        continue

    if (check[min(u, v)][max(u, v)]):
        count += 1

    check[min(u, v)][max(u, v)] = True

print(count)