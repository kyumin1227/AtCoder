from sys import stdin

input = stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

sorted_list = sorted(set(numbers))

value_to_rank = {v: i + 1 for i, v in enumerate(sorted_list)}

answer_list = [value_to_rank[number] for number in numbers]

print(*answer_list)