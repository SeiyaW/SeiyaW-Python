# マージソート
def marge(my_list, start_idx, mid_idx, end_idx):
    # 右側、左側をコピーしたリストを新たに生成
    left_copy = my_list[start_idx:mid_idx + 1]
    right_copy = my_list[mid_idx + 1:end_idx + 1]

    # 元のリスト、左コピー、右コピーのそれぞれの0番目のインデックス
    idx = start_idx
    left_idx = 0
    right_idx = 0
    left_count = len(left_copy)
    right_count = len(right_copy)

    # 左コピー、右コピーそれぞれ0番目から順に比較し、小さいものを元のリストに設定
    while left_idx < left_count and right_idx < right_count:
        if left_copy[left_idx] <= right_copy[right_idx]:
            # 左側要素の要素が右側以下の場合
            # (＊ここで、不等号にイコールが入っているため安定なソートとなる)
            my_list[idx] = left_copy[left_idx]

            # インデックスを進める
            idx += 1
            left_idx += 1
        else:
            # 右側要素のほうが小さい場合
            my_list[idx] = right_copy[right_idx]
            idx += 1
            right_idx += 1
    
    # 残った要素をもとのデータ列に戻す
    while left_idx < left_count:
        my_list[idx] = left_copy[left_idx]
        idx += 1
        left_idx += 1

    while right_idx < right_count:
        my_list[idx] = right_copy[right_idx]
        idx += 1
        right_idx += 1

def margeSort(my_list, start_idx, end_idx):
    # start_idx < end_idxではない場合、部分リストの長さが1以下なので処理終了
    if not (start_idx < end_idx):
        return
    
    # 中央のインデックスを求める
    mid_idx = (start_idx + end_idx) // 2

    # 再帰的に分割する
    margeSort(my_list, start_idx, mid_idx)
    margeSort(my_list, mid_idx + 1, end_idx)

    # ソートされた二つのデータ列をソートしながらマージする
    marge(my_list, start_idx, mid_idx, end_idx)

data = [7,5,9,6,8,4,1,2,0,3]
margeSort(data, 0, len(data) - 1)
print(data)

# 実行結果
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]