class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        start = 3
        a, b = 1, 2
        while start <= n:
            a, b = b, a + b
            start += 1

        return b


if __name__ == '__main__':
    s = Solution()
    result = s.climbStairs(5)
    print(result)
