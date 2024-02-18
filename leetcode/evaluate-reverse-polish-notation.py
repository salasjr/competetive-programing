class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])

        for a in range(len(tokens)):
            if tokens[a] not in operators:
                stack.append(int(tokens[a]))
            else:
                if len(stack) < 2:
                    return None
                operand2 = stack.pop()
                operand1 = stack.pop()
                if tokens[a] == "+":
                    result = operand1 + operand2
                elif tokens[a] == "-":
                    result = operand1 - operand2
                elif tokens[a] == "*":
                    result = operand1 * operand2
                elif tokens[a] == "/":
                    result = int(operand1 / operand2)
                stack.append(result)

        return stack[0]

