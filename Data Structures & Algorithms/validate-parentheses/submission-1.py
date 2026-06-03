class Solution:
    def isValid(self, s: str) -> bool:
        # [()]
        
        
        valid = {')' : '(',
        ']' : '[',
        '}' : '{'}

        stack = []
        
        for n in s:
            if n in valid:
                # stack[-1] is the last value you added to the stack
                if stack and stack[-1] == valid[n]:
                    stack.pop()
            else:
                stack.append(n)
            
        return len(stack) == 0