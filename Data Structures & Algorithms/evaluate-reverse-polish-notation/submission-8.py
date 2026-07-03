class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        res = int(tokens[0])
        
        for c in tokens:
            if c not in operators:
                stack.append(c)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                
                if c == '+':
                    res = a + b
                elif c == '-':
                    res = b - a
                elif c == '*':
                    res = a * b
                else:
                    res = b / a
                stack.append(res)
        
        return res