'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''
class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.m_nums = list()
        self.m_minValue = 0x8fffffff
        self.m_minIndex = 0

    def push(self, x):
        self.m_nums.append(x)
        if self.m_minValue > x:
            self.m_minValue, self.m_minIndex = x, len(self.m_nums)

    # @return nothing
    def pop(self):
        if self.m_minIndex == len(self.m_nums):
            self.m_minValue = min(self.m_nums)
            self.m_minIndex = self.m_nums.index(self.m_minValue)

        self.m_nums.pop()

    # @return an integer
    def top(self):
    	if len(self.m_nums) == 0:
    		return None
        return self.m_nums[0]

    # @return an integer
    def getMin(self):
        return self.m_minValue
        #return min(self.m_nums)