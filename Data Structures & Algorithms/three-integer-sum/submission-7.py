class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        length = len(nums)

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = length - 1

            while l < r:
                if nums[l] + nums[r] == -n:
                    triplets.append([n, nums[l], nums[r]])

                    while l + 1 < length and nums[l] == nums[l + 1]:
                        l += 1

                    while r > 0 and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < -n:
                    l += 1
                else:
                    r -= 1

        return triplets
