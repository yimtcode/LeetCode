class Solution(object):
    def __init__(self):
        self.table = (
            ('I', 1),
            ('IV', 4), ('V', 5),
            ('IX', 9), ('X', 10),
            ('XL', 40), ('L', 50),
            ('XC', 90), ('C', 100),
            ('CD', 400), ('D', 500),
            ('CM', 900), ('M', 1000)
        )

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        r = ''
        i = len(self.table) - 1
        while i >= 0:
            (k, v) = self.table[i]
            while num >= v:
                num -= v
                r += k
            i -= 1

        return r


if __name__ == '__main__':
    solution = Solution()
    # example 1
    # num = 9
    # example 2
    # "LVIII"
    # num = 58
    # example 3
    # "MCMXCIV"
    num = 1994
    s = solution.intToRoman(num)
    print(s)
