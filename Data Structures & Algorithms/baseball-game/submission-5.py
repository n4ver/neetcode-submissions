class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        final_score = 0
        for op in operations:
            if op.isdigit() or (op[0] == "-" and op[1:].isdigit()): # Is a new score of x
                stack.append(int(op))
                final_score += int(op)
            elif op == "+":
                score2 = stack[-1]
                score1 = stack[-2]
                total = score1 + score2
                stack.append(total)
                final_score += total
            elif op == "D":
                score1 = stack[-1]
                final_score += score1 * 2
                stack.append(score1 * 2)
            elif op == "C":
                score1 = stack.pop()
                final_score -= score1
            
        return final_score