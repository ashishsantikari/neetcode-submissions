class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        max_len = 0
        seen = set()
        
        for n in nums:

            # finding smallest chain
            i = n
            l = 1
            while (i-1) in hs:
                i -= 1
                l += 1

            # check end of the chain
            i = n
            while i+1 in hs:
                i += 1
                l += 1

            max_len = max(l, max_len)

        return max_len

        