# バブルソート
# バブルソートは、隣接する要素を比較して順序を入れ替えることで、リストをソートするアルゴリズムです。
def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):

        swapped = False

        for j in range(n - 1 - i):
            if my_list[j] > my_list[j + 1]:

                swapped = True
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        
        if not swapped:
            return
                
data = [6,4,7,2,10,8,1,3,9,5]
print(data)
bubble_sort(data)
print(data)

# 実行結果
# [6, 4, 7, 2, 10, 8, 1, 3, 9, 5]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# バブルソートの特徴
# 件数に依存するループが二重となっており、平均生産量、最悪計算量はともにO(n^2)となる。
# また、左側の要素＞右側の要素の場合のみ交換が発生し、同じ値の要素の入れ替えが発生しないため
# 安定なソートである。
