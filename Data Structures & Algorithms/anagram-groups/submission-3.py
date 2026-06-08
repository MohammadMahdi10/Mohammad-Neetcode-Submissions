class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can make an array of 26 and make that a key, value can be the store of words
        # then we return hashmap values
        # we do this approach by using the ord and alphabet array which contains indexes as characters

        contains = {}

        for word in strs:
            alphabet = [0 for _ in range(26)]
            for c in word:
                i = ord(c) - ord('a')
                alphabet[i] += 1
            
            key = tuple(alphabet)
            
            if key in contains:
                contains[key].append(word)
            else:
                contains[key] = []
                contains[key].append(word)
            
        return list(contains.values()) # use list to ensure it allows values to be surrounded by another array