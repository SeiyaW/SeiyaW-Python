# 挿入ソート
# データ列をソート済みとそうでない部分に分け、
# 未ソート部分から要素を1つずつソート済みの部分の適切な位置に挿入する操作を繰り返す、
def insertion_sort(my_list):
    for i in range(1, len(my_list)):

        # i番目の要素をソート対象として取り出す
        target = my_list[i]

        # 捜査対象の要素より小さい値を持つ要素が見つかるまでひとつ右側にずらす
        j = i - 1
        while 0 <= j and target < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1
        
        # ずらし終わったら空いたところに捜査対象要素を設定
        my_list[j + 1] = target

        # 途中結果の確認のためダンプ
        print(my_list)


data = [6,1,4,3,2,9,8,5,10,7]
print(data)
insertion_sort(data)
print(data)