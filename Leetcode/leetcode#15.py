#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        
        for main in range(n):
            if main > 0 and nums[main] == nums[main - 1]:
                continue
            third = n - 1
            target = -nums[main]
            for second in range(main + 1, n):
                if second > main + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[main], nums[second], nums[third]])
        
        return ans