class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
                stack.append(int(token))
            elif token == "*":
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(first_num * second_num)
            elif token == "+":
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(first_num + second_num)
            elif token == "/":
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(int(first_num / second_num))
            elif token == "-":
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(first_num - second_num)
        return stack.pop()