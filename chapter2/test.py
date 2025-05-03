# 時間計算量　素数の判定
import math

def is_prime(N):
    if N == 1:
        return False
    
    # 素数は数学的には√N以下まで計算すればよい
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
        
        return True

result = is_prime(257)
print(result)