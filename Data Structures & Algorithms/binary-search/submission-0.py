class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1   # 5

        while left <= right:
            mid = (left + right) // 2 # 2
            
            # found target
            if nums[mid] == target:
                return mid

            # target is smaller, throw away the right half
            elif nums[mid] > target:
                right = mid - 1
            else: # target is greater, throw away the left half
                left = mid + 1
        
        return -1