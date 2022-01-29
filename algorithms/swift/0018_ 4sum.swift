class Solution {
    func fourSum(_ nums: [Int], _ target: Int) -> [[Int]] {
        if nums.count < 4 {
            return []
        }

        var result: [[Int]] = []
        let soredNums = nums.sorted()
        for n1Index in 0..<soredNums.count - 3 {
            let n1 = soredNums[n1Index]
            // 过滤重复
            if n1Index != 0 && n1 == soredNums[n1Index - 1] {
                continue
            }
            for n2Index in n1Index + 1..<soredNums.count - 2 {
                let n2 = soredNums[n2Index]
                // 过滤重复
                if n2Index != n1Index + 1 && n2 == soredNums[n2Index - 1] {
                    continue
                }

                var (n3Index, n4Index) = (n2Index + 1, soredNums.count - 1)
                while n3Index < n4Index {
                    let (n3, n4) = (soredNums[n3Index], soredNums[n4Index])
                    let sum = n1 + n2 + n3 + n4
                    if sum == target {
                        result.append([n1, n2, n3, n4])
                        n3Index += 1
                        // 过滤重复n3
                        while n3Index < n4Index && n3 == soredNums[n3Index] {
                            n3Index += 1
                        }
                        n4Index -= 1
                        // 过滤重复n4
                        while n3Index < n4Index && n4 == soredNums[n4Index] {
                            n4Index -= 1
                        }

                    } else if sum < target {
                        n3Index += 1
                    } else {
                        n4Index -= 1
                    }
                }
            }
        }
        return result
    }
}


// example 1
//let nums: [Int] = [1, 0, -1, 0, -2, 2]
//let target: Int = 0

// example 2
let nums: [Int] = [2, 2, 2, 2, 2]
let target: Int = 8
let solution = Solution()
let result = solution.fourSum(nums, target)
print(result)
