class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l_s1 = len(s1)
        l_s2 = len(s2)

        l, r = 0, l_s1

        count = {}
        for s in s1:
            count[s] = count.get(s, 0) + 1

        
        while r <= l_s2:
            tmp_count = {}
            ts = s2[l:r]
            print("tm str window: ", ts);
            for s in ts:
                tmp_count[s] = tmp_count.get(s, 0) + 1
            
            if tmp_count == count:
                return True
            
            l += 1
            r += 1
        
        return False