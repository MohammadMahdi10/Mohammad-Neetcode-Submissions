class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sMap = {}
        tMap = {}

        for i in range(len(t)):
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        
        have, need = 0, len(tMap)

        l = 0
        res = float("infinity")
        resList = [-1, -1]

        for r in range(len(s)):
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            if s[r] in tMap:
                have += 1

            while have == need:
                if res > (r - l + 1):
                    res = r - l + 1
                    resList = [l, r]
                
                sMap[s[l]] = sMap.get(s[l]) - 1
                
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1

        l, r = resList
        return s[l : r + 1]