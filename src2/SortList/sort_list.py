'''
Sort a linked list in O(n log n) time using constant space complexity.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        p = head
        last = head
        while p.next != None::
            q = p.next
            if q.val > p.val:
                q.val, p.val = p.val, q.val
            
        return head


if __name__ == '__main__':
         Solution().sortList()     