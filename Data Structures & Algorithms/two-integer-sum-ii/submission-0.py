from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        data = defaultdict(list)
        for i, n in enumerate(numbers):
            data[n].append(i)
        
        for i, n in enumerate(numbers):
            comp = target - n
            if comp == n:
                return data[comp].map(lambda x: x + 1)
            if comp in data:
                return [i + 1, data[comp][0] + 1]
        