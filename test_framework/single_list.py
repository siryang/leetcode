
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # @return next node
    def addNext(self, sum):
        self.next = ListNode(sum)
        return self.next

    # @param [in] list
    def show(self):
        p = self
        while p != None:
            print p.val
            p = p.next

    def toArray(self):
        node = self
        r = list()
        while node != None:
            r.append(node.val)
            node = node.next
        return r

# @param [in] list
# @return header ListNode
def makeList(array):
    if array == None:
        return None

    p = head = ListNode(array[0])
    for i in range(1, len(array)):
        p = p.addNext(array[i])
    return head

def test():
    print "this is the test of ListNode."

if __name__ == '__main__':
    test()