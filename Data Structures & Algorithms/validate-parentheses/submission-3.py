class Solution:
    def isValid(self, s: str) -> bool:
        combinations = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        stack = []

        for c in s:
            if c not in combinations:
                stack.append(c)
            else:
                if combinations[c] == stack[-1]:
                    stack.pop()
        
        if len(stack) <= 0:
            return True
        else:
            return False