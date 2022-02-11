class Solution {
    func generateParenthesis(_ n: Int) -> [String] {
        if n == 0 {
            return []
        }

        var result: [String] = []
        self.generate(n, 0, 0, "", &result)
        return result
    }

    func generate(_ n: Int, _ left: Int, _ right: Int, _ str: String, _ result: inout [String]) {
        if left > n || right > n {
            return
        }

        if left == n && right == n {
            result.append(str)
            return
        }

        if left >= right {
            generate(n, left + 1, right, str + "(", &result)
            generate(n, left, right + 1, str + ")", &result)
        }
    }
}

// example 1
let n = 3
let solution = Solution()
let result = solution.generateParenthesis(n)
print(result)
