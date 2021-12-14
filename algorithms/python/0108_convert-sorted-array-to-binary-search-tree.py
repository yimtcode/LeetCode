# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length == 0:
            return None

        i = int(length / 2)
        n = TreeNode(nums[i])
        n.left = self.sortedArrayToBST(nums[:i])
        n.right = self.sortedArrayToBST(nums[i + 1:])
        return n


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    s = Solution()
    root = s.sortedArrayToBST(nums)
    print(root)
