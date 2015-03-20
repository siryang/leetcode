'''
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
342 + 465 = 807
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# optimize cause too much code.

class Solution:

    # @return carry, result
    def splitSum(self, s):
        if s >= 10:
            return 1, s-10 
        else:
            return 0, s

    # @return new node
    def addValue(self, node, sum):
        node.next = ListNode(sum)
        return node.next

    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None and l2 == None:
            return None

        headValue = 0
        if l1 != None:
            headValue += l1.val
            l1 = l1.next

        if l2 != None:
            headValue += l2.val
            l2 = l2.next

        carry, headValue = self.splitSum(headValue)
        result = head = ListNode(headValue)

        while l1 != None and l2 != None:
            carry, sum = self.splitSum(l1.val + l2.val + carry)
            result = self.addValue(result, sum)

            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            carry, sum = self.splitSum(l1.val + carry)
            result = self.addValue(result, sum)
            l1 = l1.next

        while l2 != None:
            carry, sum = self.splitSum(l2.val + carry)
            result = self.addValue(result, sum)
            l2 = l2.next

        if carry == 1:
            result = self.addValue(result, 1)
        return head

    def makeList(self, src):
        if src == None:
            return None

        p = head = ListNode(src[0])
        for i in range(1, len(src)):
            p = self.addValue(p, src[i])
        return head

makeList =  Solution().makeList

def show(l):
    p = l
    while p != None:
        print p.val
        p = p.next

def list2Array(l):
    r = list()
    while l != None:
        r.append(l.val)
        l = l.next
    return r

def test(l1, l2, expect):
    result = Solution().addTwoNumbers(makeList(l1), makeList(l2))
    result = list2Array(result)
    if expect != result:
        print "l1:", l1
        print "l2:", l2
        print "expect:", expect
        print "result:", result

if __name__ == '__main__':
    test([2, 4, 3], [5, 6, 4], [7, 0, 8])
    test([2, 4, 3], [5, 6, 4, 1], [7, 0, 8, 1])
    test([2, 4, 3, 1], [5, 6, 4], [7, 0, 8, 1])

