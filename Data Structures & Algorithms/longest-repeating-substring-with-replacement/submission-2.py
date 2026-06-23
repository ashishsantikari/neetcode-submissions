class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = {}
        maxFreq = None
        res = 0

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            print("str", s[right])

            # setting the max frequency character
            maxFreq = s[right] if count.get(s[right], 0) > count.get(maxFreq, 0) else maxFreq

            if (right - left + 1) - count.get(maxFreq, 0) <= k:
                res = max(res, right - left + 1)
            else:
                count[s[left]] = count.get(s[left]) - 1
                left += 1
            
            right += 1

        return res