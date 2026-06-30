from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1, hm2 = defaultdict(int), defaultdict(int)
        for c in range(len(s)):
            hm1[s[c]] += 1
        for c in range(len(t)):
            hm2[t[c]] += 1
        
        if len(hm1.keys()) != len(hm2.keys()):
            return False

        for k in hm1.keys():
            if k not in hm2 or hm2[k] != hm1[k]:
                return False

        return True

            