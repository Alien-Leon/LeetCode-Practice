class MinStack:
    # 另解 入栈时将当前最小值同时入栈，可以有较高的时间复杂度
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.o = [] # 优先队列，此处简化为数组

    def push(self, x: int) -> None:
        self.s.append(x)
        i = 0
        while i < len(self.o):
            if x >= self.o[i]:
                i += 1
            else:
                break
        self.o.insert(i, x)
        

    def pop(self) -> None:
        self.o.remove(self.s[-1])
        self.s.pop()
        
        

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        # 内部维护一个最小堆形成优先队列可以使得O(1)时间获取最小值
        return self.o[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()