'''
Sort a linked list in O(n log n) time using constant space complexity.
'''

import sys
sys.path.append('../../test_framework')
from test_framework import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def quickSortList(self, head):
        middle = head
        l = r = None

        p = head.next
        lp = rp = middle
        
        while p != None:
            pNext = p.next
            if p.val >= middle.val:
                p.next = lp
                lp = p
            else:
                rp.next = p
                rp = p
            p = pNext

        rp.next = None
        return lp

    def sortList(self, head):
        # p = head
        head = self.quickSortList(head)
        head.show()

if __name__ == '__main__':
    head = makeList([5, 4, 5, 3, 7])
    # head.show()
    Solution().sortList(head)