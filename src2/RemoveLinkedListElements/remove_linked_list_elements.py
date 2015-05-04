import sys
sys.path.append('../../test_framework')
from test_framework import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        p = head;
        while p != None:
            pNext = p.next;
            while pNext != None and pNext.val == val:
                pNext = pNext.next
            p.next = pNext
            p = pNext
        if head.val == val:
            head = head.next
        return head;


if __name__ == '__main__':
    # head = makeList([1,2,3,4])
    # Solution().removeElements(head, 3).show()

    head = makeList([3,3,1])
    Solution().removeElements(head, 3).show()
