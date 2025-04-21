from sys import stdin

input = stdin.readline

def cal(arg_a, arg_b, arg_c):
    """計算して目標の金額が作れるかどうか確認"""
    
    money = arg_a * 500 + arg_b * 100 + arg_c * 50

    return 1 if money == target else 0

a = int(input())
b = int(input())
c = int(input())
target = int(input())

answer = 0

for indexA in range(a + 1):
    for indexB in range(b + 1):
        for indexC in range(c + 1):
            answer += cal(indexA, indexB, indexC)

print(answer)
