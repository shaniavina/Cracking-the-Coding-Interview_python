class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.A:
            self.A.append(0)
            self.min = x
        else:
            self.A.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        x = self.A.pop()
        if x < 0:
            self.min = self.min - x

    def top(self):
        """
        :rtype: int
        """
        x = self.A[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
