
class BinaryTree:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

    def setChild(self, leftValue, rightValue):
        if (leftValue != None):
            self.left = BinaryTree(leftValue)
        if (rightValue != None):
            self.right = BinaryTree(rightValue)

    def build(self, data):
        if len(data) == 0:
            return None
        root = BinaryTree(data[0])
        openNode = [root]
        for i in range(1, len(data), 2):
            node = openNode.pop()
            if i + 1 == len(data):
                node.setChild(data[i], None)
            else:
                node.setChild(data[i], data[i+1])
            openNode.append([node.left, node.right])
        return root

    def show(self):
        layer = [self]
        p = self
        level = 0
        while len(layer) != 0:
            values = []
            nextLayer = []
            for node in layer:
                if node == None:
                    values.append("#")
                else:
                    values.append(node.val)
                    nextLayer.append(node.left)
                    nextLayer.append(node.right)

            print "level: %d, data:" % (level),
            print values
            layer = nextLayer
            level += 1

if __name__ == '__main__':
    root = BinaryTree().build([1,2,3])
    root.show()
