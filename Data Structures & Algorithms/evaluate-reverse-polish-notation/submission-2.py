class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                second = stack.pop()
                first = stack.pop()
                result = first + second
                stack.append(result)
            elif token == '-':
                second = stack.pop()
                first = stack.pop()
                result = first - second
                stack.append(result)
            elif token == '*':
                second = stack.pop()
                first = stack.pop()
                result = first * second
                stack.append(result)
            elif token == '/':
                second = stack.pop()
                first = stack.pop()
                result = int(float(first) / second)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()