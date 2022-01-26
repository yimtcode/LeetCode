import Foundation

class Solution {
    func threeSumClosest(_ nums: [Int], _ target: Int) -> Int {
        if nums.count == 3 {
            return nums[0] + nums[1] + nums[2]
        }
        
        let numsSorted = nums.sorted()
        var nearSum = Int.max
        var distance: Int = Int.max
        for i in 0..<numsSorted.count-2 {
            let n1 = numsSorted[i]
            var (l, r) = (i+1, numsSorted.count-1)
            while l < r {
                let n2 = numsSorted[l]
                let n3 = numsSorted[r]
                let sum = n1 + n2 + n3
                let currentDistance = abs(target - sum)
                if currentDistance == 0 {
                    // 已经找到最近
                    return sum
                }else if distance > currentDistance {
                    distance = currentDistance
                    nearSum = sum
                }
                
                if sum > target {
                    r -= 1
                } else {
                    l += 1
                }
            }
        }
        
        return nearSum
    }
}

// example1
let nums: [Int] = [-1, 2, 1, -4];
let target = 1
// example2
//let nums: [Int] = [1, 1, -1, -1, 3];
//let target = -1
let solution = Solution()
let result = solution.threeSumClosest(nums, target)
print(result)
