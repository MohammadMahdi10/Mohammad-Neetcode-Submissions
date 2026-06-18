class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        sMap, tMap = {}, {}

        for c in t:
            tMap[c] = tMap.get(c, 0) + 1

        have, need = 0, len(tMap)

        l = 0
        res = float("infinity")
        resInd = [-1, -1]

        for r in range(len(s)):
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < res:
                    res = r - l + 1
                    resInd = [l, r]
                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        
        if res == float("infinity"):
            return ""
        else:
            l, r = resInd
            return s[l:r+1]
