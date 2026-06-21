class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break;
            
            p = (l + r) // 2
            res = min(res, nums[p])
            if nums[l] <= nums[p]:
                l = p + 1
            else:
                r = p - 1
        
        return res
