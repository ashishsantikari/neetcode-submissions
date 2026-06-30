class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = len(nums)
        prefix, suffix = [0] * s, [0] * s
        res = [0] * s

        for i, n in enumerate(nums):
            if i == 0:
                prefix[i] = 1 * n
            else:
                prefix[i] = n * prefix[i - 1]

        print("prefix:", prefix)

        for i in range(s - 1, -1, -1):
            if i == s - 1:
                suffix[i] = 1 * nums[i]
            else:
                suffix[i] = nums[i] * suffix[i + 1]

        # print("suffix:", suffix)

        for i, n in enumerate(nums):
            if i == 0:
                res[i] = suffix[i + 1]
            elif i == s - 1:
                res[i] = prefix[i - 1]
            else:
                res[i] = prefix[i - 1] * suffix[i + 1]

        return res
