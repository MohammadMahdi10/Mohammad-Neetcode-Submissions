class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in duplicates:
                duplicates.remove(s[l])
                l += 1
            duplicates.add(s[r])
            longest = max(longest, r - l + 1)

        
        return longest
