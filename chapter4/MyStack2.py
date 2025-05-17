class MyStack2:
    def __init__(self, N):
        self.N = N
        self.stack = [None] * N
        self.pointer = 0

    def push(self, value):
        if self.N <= self.pointer:
            #スタックがいっぱいの場合はpush失敗
            print("スタックがいっぱいなのでpushできません。")
            return 
        
        self.stack[self.pointer] = value
        self.pointer += 1

    def pop(self):
        #スタックに要素がない場合はpop失敗
        if self.pointer == 0:
            print("スタックに要素がないのでpop出来ません。")
            return
        
        value = self.stack[self.pointer - 1]
        self.stack[self.pointer - 1] = None
        self.pointer -= 1
        return value

    def __str__(self):
        return str(self.stack)
    
my_stack2 = MyStack2(4)
my_stack2.push("a")
print(my_stack2)