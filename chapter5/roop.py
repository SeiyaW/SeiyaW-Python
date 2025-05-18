my_list = [1,3,5,6,4,2]
N = len(my_list)
idx = N - 1
while idx >= 0 and my_list[idx] <= 4:
    idx -= 2
print(idx)