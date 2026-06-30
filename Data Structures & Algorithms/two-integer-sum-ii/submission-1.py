from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) - 1
        while numbers[lp] + numbers[rp] != target:
            summed = numbers[lp] + numbers[rp]

            if summed > target:
                rp -= 1
            elif summed < target:
                lp += 1
            
        return [lp + 1, rp + 1]