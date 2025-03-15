from sys import stdin

# 種類１
def type1(a, b):
    positions[a] = b

# 種類２
def type2(a, b):
    for key, value in positions.items():
        if value == a:
            positions[key] = b
        elif value == b:
            positions[key] = a

# 種類３
def type3(a):
    print(positions[a] + 1)

input = stdin.readline

n, q = map(int, input().split())

positions = {i: i for i in range(n)}

for _ in range(q):
    t, num1, *num2 = map(int, input().split())

    if t == 1:
        type1(num1 - 1, num2[0] - 1)
    elif t == 2:
        type2(num1 - 1, num2[0] - 1)
    else:
        type3(num1 - 1)
