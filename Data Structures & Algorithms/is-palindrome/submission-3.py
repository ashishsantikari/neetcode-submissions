class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1
        s = s.lower()

        while lp < rp:
            a = s[lp]
            b = s[rp]

            if a.isalnum() and b.isalnum() and a != b:
                print(f"a: {a} b:{b}")
                return False
            elif a.isalnum() and b.isalnum() and a == b:
                lp += 1
                rp -= 1

            if not a.isalnum():
                lp += 1

            if not b.isalnum():
                rp -= 1

        return True
