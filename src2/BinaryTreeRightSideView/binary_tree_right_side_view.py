import sys
sys.path.append('../../test_framework')
#from test_framework.binary_tree import *
from test_framework import *

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        stack = []
        p = root
        result = []
        currentLevel = 0

        while p != None:
            # p is a most right node never traversed.
            if currentLevel == len(result):
                result.append(p.val)

            if p.right != None:
                stack.append(p)
                p = p.right
                currentLevel += 1
            elif p.left != None:
                stack.append(p)
                p = p.left
                currentLevel += 1
            else:
                while stack
                parent = stack[-1]
                while p == parent.left:
                    p = parent
                    currentLevel -= 1
                    stack.pop()
                    parent = stack[-1]
                p = parent.left
        return result


if __name__ == '__main__':
    root = binary_tree.BinaryTree().build([1])
    Solution().rightSideView(root)