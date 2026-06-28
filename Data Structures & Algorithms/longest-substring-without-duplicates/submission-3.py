class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l = 0
        maxLength = 0
        duplicates = set()

        for r in range(len(s)):
            if s[r] not in duplicates:
                duplicates.add(s[r])
                maxLength = max(maxLength, r - l + 1)
            else:
                maxLength = max(maxLength, r - l)
                while s[r] in duplicates:
                    duplicates.remove(s[l])
                    l += 1
                duplicates.add(s[r])
        
        return maxLength
