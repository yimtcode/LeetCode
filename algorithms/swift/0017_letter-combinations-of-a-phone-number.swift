import Foundation

class Solution {
    let table: [String: [String]]

    init() {
        self.table = [
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        ]
    }

    func letterCombinations(_ digits: String) -> [String] {
        var arrStr: [String] = []
        var strIndex = digits.startIndex

        while strIndex < digits.endIndex {
            let c = digits[strIndex]
            let old = arrStr
            let values = self.table[String(c)]

            arrStr = []
            if old.count == 0 {
                for value in values ?? [] {
                    arrStr.append(value)
                }
            } else {
                for str in old {
                    for value in values ?? [] {
                        arrStr.append(str + value)
                    }
                }
            }

            strIndex = digits.index(strIndex, offsetBy: 1)
        }
        return arrStr
    }
}

let digits = "2"
let solution = Solution()
let result = solution.letterCombinations(digits)
print(result)
