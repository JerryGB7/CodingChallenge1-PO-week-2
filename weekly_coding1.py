user_list = list(int(num) for num in input().strip().split())
user_list.sort()
largest_gap = []

for i in range(len(user_list)):
    if i == len(user_list) - 1:
        break
    largest_gap.append(user_list[i+1] - user_list[i])
print(max(largest_gap))