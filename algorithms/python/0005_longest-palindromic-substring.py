class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length < 2:
            return s

        r = ""
        index = 0
        while index < length:
            # 中间为该字符的回文数
            left, right = index, index
            while left >= 0 and right < length:
                if s[left] == s[right]:
                    if (right - left) + 1 > len(r):
                        r = s[left:right + 1]
                else:
                    break
                left -= 1
                right += 1

            # 左边为该字符的回数数
            left, right = index, index + 1
            while left >= 0 and right < length:
                if s[left] == s[right]:
                    if (right - left) + 1 > len(r):
                        r = s[left:right + 1]
                else:
                    break
                left -= 1
                right += 1
            index += 1
        return r


if __name__ == '__main__':
    solution = Solution()
    s = "babad"
    r = solution.longestPalindrome(s)
    print(r)
