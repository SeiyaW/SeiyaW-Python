# 選択ソート
def selection_sort(my_list):
    n = len(my_list)
    for i in range(n):

        # i～末尾までで最小のものを探し、そのindexを格納
        target_idx = i
        for j in range(i + 1, n):
            if my_list[j] < my_list[target_idx]:
                target_idx = j
        
        # i～末尾までで最小のものをi番目のものと交換する
        my_list[i], my_list[target_idx] = \
            my_list[target_idx], my_list[i]
        
        # 途中結果の確認のためダンプ
        print(my_list)

data = [6,4,7,2,10,8,1,3,9,5]
print(data)
selection_sort(data)
print(data)

# 実行結果
# [6, 1, 4, 3, 2, 9, 8, 5, 10, 7]
# [1, 6, 4, 3, 2, 9, 8, 5, 10, 7]
# [1, 4, 6, 3, 2, 9, 8, 5, 10, 7]
# [1, 3, 4, 6, 2, 9, 8, 5, 10, 7]
# [1, 2, 3, 4, 6, 9, 8, 5, 10, 7]
# [1, 2, 3, 4, 6, 9, 8, 5, 10, 7]
# [1, 2, 3, 4, 6, 8, 9, 5, 10, 7]
# [1, 2, 3, 4, 5, 6, 8, 9, 10, 7]
# [1, 2, 3, 4, 5, 6, 8, 9, 10, 7]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]