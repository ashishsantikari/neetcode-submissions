class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack) > 0:
            # move the current val to the minStack in right order
            # ideally we need to pop the values until we find number which is barely decreasing from current value
            # then we push the val, then sequentially push the remaining popped values
            tmp = []
            while len(self.minStack) > 0 and val > self.minStack[-1]:
                tmp.append(self.minStack.pop())
            self.minStack.append(val)
            while len(tmp) != 0:
                self.minStack.append(tmp.pop())
        else:
            self.minStack.append(val)

        # print("stack", self.stack)
        # print("min-stack", self.minStack)

    def pop(self) -> None:

        elem = self.stack.pop()
        tmp = []
        while len(self.minStack) > 0 and self.minStack[-1] != elem:
            tmp.append(self.minStack.pop())

        # remove the element
        self.minStack.pop() 

        # add back
        while len(tmp) != 0:
            self.minStack.append(tmp.pop())   

        return elem

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # print("stack", self.stack)
        # print("min-stack", self.minStack)
        return self.minStack[-1]
