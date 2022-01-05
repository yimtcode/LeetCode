class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        s = s.strip()

        num = 0
        # 符号
        sign = None
        for i, c in enumerate(s):

            if c == '+' or c == '-':
                # 特殊情况：123-123
                if i > 0:
                    break

                # 特殊情况：123-+123
                if sign is not None:
                    break

                # 记录符号位
                if c == '+':
                    sign = 1
                    continue
                elif c == '-':
                    sign = -1
                    continue

            r = dic.get(c)
            if r is None:
                break
            num = num * 10 + r

            # 检查越界（注意：如果num是int32类型，会发生越界，不能这样写）
            if (sign is None or sign == 1) and num > 2147483647:
                num = 2147483647
                break
            elif sign == -1 and num > 2147483648:
                num = 2147483648
                break

        # 添加符号
        if sign is not None:
            num = num * sign

        return num


if __name__ == '__main__':
    solution = Solution()
    # s = "42"
    # s = "   -42"
    # s = "4193 with words"
    s = "-91283472332"
    n = solution.myAtoi(s)
    print(n)
