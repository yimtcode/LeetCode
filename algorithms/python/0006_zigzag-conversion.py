class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        rows = {}
        cur_row = 0
        going_down = False
        for c in s:
            if rows.get(cur_row) is None:
                rows[cur_row] = ""
            rows[cur_row] += c
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down

            cur_row += 1 if going_down else -1

        r = ""
        for v in rows.values():
            r += v

        return r


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    solution = Solution()
    r = solution.convert(s, 3)
    print(r)
