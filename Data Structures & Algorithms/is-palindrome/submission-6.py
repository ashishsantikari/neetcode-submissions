class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1
        s = s.lower()

        while lp < rp:
            a = s[lp]
            b = s[rp]

            if not a.isalnum():
                lp += 1
                continue
            if not b.isalnum():
                rp -= 1
                continue
            
            if a != b:
                return False
            else:
                lp += 1
                rp -= 1

        return True
