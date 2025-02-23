from sys import stdin

input = stdin.readline

s1, s2 = input().split()

if s1 == "sick":
    if s2 == "sick":
        print(1)
    else:
        print(2)
elif s2 == "sick":
    print(3)
else:
    print(4)
