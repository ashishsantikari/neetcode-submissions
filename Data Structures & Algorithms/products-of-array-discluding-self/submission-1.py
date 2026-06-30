class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = set()
        for i, n in enumerate(nums):
            if n != 0:
                prod *= n
            else:
                zeros.add(i)
        res = [0] * len(nums)

        for i, n in enumerate(nums):
            if i in zeros:
                if len(zeros) == 1:
                    res[i] = int(prod)
                else:
                    res[i] = 0
            else:
                if len(zeros) == 0:
                    res[i] = int(prod/n)
                else:
                    res[i] = 0
        
        return res
