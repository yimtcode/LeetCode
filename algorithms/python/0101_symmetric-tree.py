# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        return self.isMirror(root.left, root.right)

    def isMirror(self, a, b):
        if not a and not b:
            return True

        if not a or not b:
            return False

        if a.val != b.val:
            return False

        return self.isMirror(a.left, b.right) and self.isMirror(a.right, b.left)


if __name__ == '__main__':
    root = TreeNode(1,
                    TreeNode(2,
                             TreeNode(3), TreeNode(4)),
                    TreeNode(2,
                             TreeNode(4), TreeNode(3)))
    s = Solution()
    b = s.isSymmetric(root)
    print(b)
