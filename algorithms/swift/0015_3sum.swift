import Foundation

class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {
        let sorted = nums.sorted()
        var result: [[Int]] = []
        
        if sorted.count < 3 {
            return result
        }
        
        for i in 0..<sorted.count-2 {
            let n1 = sorted[i]
            if n1 > 0 {
                // 因为数组从小到大有序并且n1>0，后面n2和n3一定>0，所以n1+n2+n3一定大于0
                break
            }
            
            if i > 0 && n1 == sorted[i-1] {
                // 去重
                continue
            }
            
            var (l, r) = (i+1, sorted.count-1)
            while l < r {
                let (n2, n3) = (sorted[l], sorted[r])
                let sum = n1 + n2 + n3
                if sum == 0 {
                    result.append([n1, n2, n3])
                    while l < r && sorted[l] == n2 {
                        // 防止n2重复
                        l += 1
                    }
                    while l < r && sorted[r] == n3 {
                        // 防止n1重复
                        r -= 1
                    }
                } else if sum < 0 {
                    // 因为sum<0，需要增大sum，n1固定n3只能变小，所以把l索引向右偏移
                    l += 1
                } else {
                    // 因为sum>0，需要缩小sum，n1固定n2只能变大，所以把r索引向左偏移
                    r -= 1
                }
            }
            
        }
        return result
    }
}

//var nums = [-1,0,1,2,-1,-4]
var nums: [Int] = []
let solution = Solution()
let result = solution.threeSum(nums)
print(result)
