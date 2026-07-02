class Solution:
    def isValid(self, s: str) -> bool:
        combinations = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        stack = []

        for c in s:
            if c in combinations:
                if stack and combinations[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) <= 0:
            return True
        else:
            return False