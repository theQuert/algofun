class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = []
        if (not nums or length < 3):
            return []
        # Sorting
        nums.sort()
        res = []

        for i in range(length):
            # Since the list has been sorted before, if nums[i]>0, there is no possible for adding other 2 element == 0.
            if(nums[i] > 0):
                return res
            # Processing with duplicates.
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            # Create L, R
            L = i + 1
            R = length - 1
            while(L < R):
                if(nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    # Remove duplicates
                    while(L < R and nums[L]==nums[L+1]):
                        L = L + 1
                    while(L < R and nums[R]==nums[R-1]):
                        R = R - 1
                    # Move L, R to find the next possible ans
                    L = L + 1
                    R = R - 1
                elif(nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res
