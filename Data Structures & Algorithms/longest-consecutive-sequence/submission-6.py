class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        max_len = 0
        
        for num in nums:
            if num - 1 not in hs:
                curr = num
                seq_len = 1

                while (curr + 1) in hs:
                    seq_len +=1
                    curr += 1

                max_len = max(max_len, seq_len)
        
        return max_len


        