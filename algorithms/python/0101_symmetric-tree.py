from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # recursion
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

    # iteration
    def isSymmetric2(self, root):
        q = deque([root.left, root.right])
        while len(q) > 0:
            a, b = q.popleft(), q.popleft()
            if not a and not b:
                continue

            if not a or not b:
                return False

            if a.val != b.val:
                return False

            q.append(a.left)
            q.append(b.right)
            q.append(a.right)
            q.append(b.left)

        return True


if __name__ == '__main__':
    root = TreeNode(1,
                    TreeNode(2,
                             TreeNode(3), TreeNode(4)),
                    TreeNode(2,
                             TreeNode(4), TreeNode(3)))
    s = Solution()
    b = s.isSymmetric(root)
    print(b)
    b2 = s.isSymmetric(root)
    print(b2)
