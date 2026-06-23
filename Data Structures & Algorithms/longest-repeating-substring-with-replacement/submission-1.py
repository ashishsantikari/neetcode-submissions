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

            print("len", right - left + 1, " max freq  ", maxFreq, " max freq count ", count.get(maxFreq))
            if (right - left + 1) - count.get(maxFreq, 0) <= k:
                print("pre res", res, " len s[l:r] ", right - left + 1)
                res = max(res, right - left + 1)
                print("res", res)
            else:
                count[s[left]] = count.get(s[left]) - 1
                left += 1
            
            right += 1

        return res