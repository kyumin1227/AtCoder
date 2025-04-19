from sys import stdin

input = stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

count = 0

while True:
    for i in range(n):
        if numbers[i] % 2 == 0:
            numbers[i] /= 2
        else:
            print(count)
            exit()
    
    count += 1