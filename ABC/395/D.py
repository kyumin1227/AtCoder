from sys import stdin

# 種類１
def type1(a, b):
    for i in range(n):
        if a in board[i]:
            board[i].remove(a)
            break
    
    board[b].add(a)
    
# 種類２
def type2(a, b):
    temp = board[a]
    board[a] = board[b]
    board[b] = temp

# 種類３
def type3(a):
    for i in range(n):
        if a in board[i]:
            print(i + 1)
            break

input = stdin.readline

n, q = map(int, input().split())

board = [{i} for i in range(n)]

for _ in range(q):
    t, num1, *num2 = map(int, input().split())

    if t == 1:
        type1(num1 - 1, num2[0] - 1)
    elif t == 2:
        type2(num1 - 1, num2[0] - 1)
    else:
        type3(num1 - 1)
