import Foundation

class Solution {
    func isPalindrome(_ s: String) -> Bool {
        if s.count <= 1 {
            return true
        }

        let newS = s.uppercased().trimmingCharacters(in: NSCharacterSet.whitespaces)
        var (lowIndex, highIndex) = (newS.startIndex, newS.index(newS.endIndex, offsetBy: -1))
        
        while lowIndex < highIndex {
            let low = newS[lowIndex]
            if !low.isNumber && !low.isLetter {
                lowIndex = newS.index(lowIndex, offsetBy: 1)
                continue
            }
            let high = newS[highIndex]
            if !high.isNumber && !high.isLetter {
                highIndex = newS.index(highIndex, offsetBy: -1)
                continue
            }
            
            lowIndex = newS.index(lowIndex, offsetBy: 1)
            highIndex = newS.index(highIndex, offsetBy: -1)
            if low != high {
                return false
            }
        }
        return true
    }
}

var solution = Solution()
//let s = "A man, a plan, a canal: Panama"
//let s =  "race a car"
let s = " "
let b = solution.isPalindrome(s)
print(b)
