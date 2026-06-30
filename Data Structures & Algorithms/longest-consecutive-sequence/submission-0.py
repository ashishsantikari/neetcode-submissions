class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set()
        max_len = 0
        seen = set()
        for n in nums:
            hs.add(n)
        
        for n in nums:
            if n in seen:
                continue;

            seen.add(n)

            # finding smallest chain
            i = n
            l = 1
            while (i-1) in hs:
                i -= 1
                l += 1
                seen.add(i)

            # check end of the chain
            i = n
            while i+1 in hs:
                i += 1
                l += 1
                seen.add(i)

            if l > max_len:
                max_len = l

        return max_len

        