# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False

        targetSum = targetSum - root.val
        if targetSum == 0 and root.left is None and root.right is None:
            # targetSum equal Zero and No child nodes
            return True

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


if __name__ == '__main__':
    # example 1
    # False
    # root = TreeNode(1, TreeNode(2), TreeNode(3))
    # targetSum = 5

    # example 2
    # True
    root = TreeNode(5,
                    TreeNode(4,
                             TreeNode(11,
                                      TreeNode(7),
                                      TreeNode(2))),
                    TreeNode(8,
                             TreeNode(13),
                             TreeNode(4,
                                      left=None,
                                      right=TreeNode(1)))
                    )
    targetSum = 22

    # example 3
    # False
    # root = TreeNode(1, TreeNode(2))
    # targetSum = 1

    s = Solution()
    b = s.hasPathSum(root, targetSum)
    print(b)
