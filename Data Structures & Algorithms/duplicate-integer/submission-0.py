class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ds = set()
        for n in nums:
            if n in ds:
                return True
            ds.add(n)
        return False