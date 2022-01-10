class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_height = 0
        left = 0
        right = len(height) - 1

        while left < right:
            left_height = height[left]
            right_height = height[right]

            t_height = min(left_height, right_height) * (right - left)
            if t_height > max_height:
                max_height = t_height

            if left_height > right_height:
                right -= 1
            else:
                left += 1

        return max_height


if __name__ == '__main__':
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = solution.maxArea(height)
    print(result)
