class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        length = len(digits)
        carry = 0
        for index in range(length - 1, -1, -1):
            num = digits[index] + carry
            if index == length - 1:
                num += 1

            carry = int(num / 10)
            digits[index] = num % 10

        if carry > 0:
            digits = [carry] + digits

        return digits


if __name__ == "__main__":
    src = [2, 9, 9]
    s = Solution()
    l = s.plusOne(src)
    print(l)
