from sys import stdin

input = stdin.readline

n = int(input())

board = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    j = n - i - 1

    if (i > j):
        break

    for x in range(i, j + 1):
        for y in range(i, j + 1):
            board[x][y] = False if i % 2 == 0 else True 

for i in range(n):
    for j in range(n):
        print("." if board[i][j] else "#", end="")
    print()
