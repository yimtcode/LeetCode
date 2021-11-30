class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_index = m - 1
        nums2_index = n - 1
        real_index = m + n - 1
        while nums1_index >= 0 or nums2_index >= 0:
            if nums1_index >= 0 and nums2_index >= 0:
                if nums1[nums1_index] > nums2[nums2_index]:
                    nums1[real_index] = nums1[nums1_index]
                    nums1_index -= 1
                else:
                    nums1[real_index] = nums2[nums2_index]
                    nums2_index -= 1
            elif nums1_index >= 0:
                break
            else:
                nums1[real_index] = nums2[nums2_index]
                nums2_index -= 1
            real_index -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    # nums1 = [4, 5, 6, 0, 0, 0]
    # m = 3
    # nums2 = [1, 2, 3]
    # n = 3

    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)
