# 変数の実態ごとにユニークなidが割り当てられている。
x = [1,2,3]
y = x
print(id(x))
print(id(y))