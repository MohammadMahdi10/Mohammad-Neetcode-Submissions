class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []

        total = int(tokens[0])
        for c in tokens:
            if c in operators:
                if len(stack) != 0:
                    if c == '+':
                        total = int(stack.pop()) + int(stack.pop())
                    elif c == '-':
                        a = int(stack.pop())
                        b = int(stack.pop())
                        total = b - a
                    elif c == '*':
                        total = int(stack.pop()) * int(stack.pop())
                    else:
                        a = int(stack.pop())
                        b = int(stack.pop())
                        total = b / a
                stack.append(total)
            else:
                stack.append(c)
        
        return total