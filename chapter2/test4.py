# 空間計算量の改善例
def my_func():
    for i in range(100):
        if i % 3 == 0:
            yield i

# def main():
#     my_sum = 0
#     for i in range(100):
#         if i % 3 == 0:
#             my_sum += i

#     print(my_sum)

def main():
    numbers = my_func()
    my_sum = 0
    for num in numbers:
        my_sum += num

    print(my_sum)

main()