class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_index = 0
        s_length = len(s)

        p_index = 0
        p_length = len(p)

        while s_index < s_length and p_index < p_length:
            p_c = p[p_index]
            s_c = s[s_index]
            p_next_c = p[p_index + 1] if p_index + 1 < p_length else None

            if p_next_c == '*':
                if p_c == '.' or p_c == s_c:
                    if self.isMatch(s[s_index:], p[p_index + 2:]):
                        # 剩余数据可匹配
                        p_index += 2
                        continue
                else:
                    p_index += 2
                    continue
            else:
                if p_c == '.' or p_c == s_c:
                    p_index += 1
                else:
                    return False
            s_index += 1

        # 还有剩余数据未匹配
        if s_index != s_length:
            return False

        if p_index < p_length:
            # 不是a*b*这样整对
            if (p_length - p_index) % 2 != 0:
                return False

            while p_index < p_length:
                p_next_c = p[p_index + 1] if p_index + 1 < p_length else None
                if p_next_c != '*':
                    return False
                else:
                    p_index += 2

        return True


if __name__ == '__main__':
    solution = Solution()
    # example1
    s = 'aab'
    p = 'c*a*b'
    # example2
    # s = 'caab'
    # p = 'c*a*b'
    # example3
    # s = 'mississippi'
    # p = 'mis*is*p*.'
    # example4
    # s = 'aa'
    # p = 'a*'
    # example5
    # s = 'aaa'
    # p = 'a*a'
    # example6
    # s = 'aaa'
    # p = 'ab*a*c*a'
    b = solution.isMatch(s, p)
    print(b)
