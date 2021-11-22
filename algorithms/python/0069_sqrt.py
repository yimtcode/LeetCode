class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x

        # binary search
        min = 0
        max = x
        while max - min > 1:
            mid = int((min + max) / 2)
            if mid * mid > x:
                max = mid
            else:
                min = mid

        return min


if __name__ == "__main__":
    x = 8
    solution = Solution()
    r = solution.mySqrt(x)
    print(r)
