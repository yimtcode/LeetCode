class Solution {
    // 热门评论解法
    func divide(_ dividend: Int, _ divisor: Int) -> Int {
        // Int32.min = -2147483648
        // Int32.max = 2147483647
        // -2147483648 / -1 = 2147483648会出现越界，需要特殊处理
        if dividend == Int32.min && divisor == -1 {
            return Int(Int32.max)
        }

        // 异或: 相同为0，不同为1
        // 符号位: 相同为正，不同为负，刚好匹配
        let isNegative = (dividend ^ divisor) < 0
        var absDividend = abs(dividend)
        let absDivisor = abs(divisor)
        var result: Int = 0
        for n in stride(from: 31, through: 0, by: -1){
            if (absDividend >> n) >= absDivisor { // absDividend/2^n >= absDivisor
                result += 1 << n // 将计算的倍数2^n累加到最终结果上
                absDividend -= absDivisor << n // 减去已添加倍数
            }
        }

        return isNegative ? -result : result
    }
}

var solution = Solution()
var result = solution.divide(-2147483648, -1)
print(result)