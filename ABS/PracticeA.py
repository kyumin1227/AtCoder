from sys import stdin

input = stdin.readline

a = int(input())
b, c = map(int, input().split())
s = input().strip()

print(a + b + c, s)