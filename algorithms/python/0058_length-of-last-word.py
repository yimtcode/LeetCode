class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        last_count = 0
        current_count = 0
        for v in s:
            if v == ' ':
                if current_count > 0:
                    last_count = current_count
                current_count = 0
            else:
                current_count += 1

        if current_count > 0:
            return current_count
        else:
            return last_count


if __name__ == '__main__':
    # s = "Hello World"
    s = "   fly me   to   the moon  "
    solution = Solution()
    length = solution.lengthOfLastWord(s)
    print(length)
