class Solution:
    def isValid(self, s: str) -> bool:
        # [()]
        
        
        valid = {')' : '(',
        ']' : '[',
        '}' : '{'}

        stack = []
        
        for n in s:
            if n in valid:
                stack.pop()
            else:
                stack.append(n)
            
        return len(stack) == 0