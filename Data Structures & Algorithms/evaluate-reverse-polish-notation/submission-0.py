class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []

        total = 0
        for c in tokens:
            if c in operators:
                if len(stack) != 0:
                    if c == '+':
                        total = int(stack.pop()) + int(stack.pop())
                    elif c == '-':
                        total = int(stack.pop()) - int(stack.pop())
                    elif c == '*':
                        total = int(stack.pop()) * int(stack.pop())
                    else:
                        total = int(stack.pop()) / int(stack.pop())
                stack.append(total)
            else:
                stack.append(c)
        
        return total