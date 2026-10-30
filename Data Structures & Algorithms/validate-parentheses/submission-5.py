class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        open_paren = "({["
        closed_paren = ")}]"
        for character in s:
            if character in open_paren: # If its an open bracket, append it to stack
                stack.append(character)
            else:
                if len(stack) == 0: return False # Edge case for when we start with a closed bracket
                if closed_paren.index(character) == open_paren.index(stack[-1]): # If the top of the stack is a open bracket, we check if it matches
                    stack.pop() # If match, we remove the open bracket from stack
                else: # Else, its not valid
                    return False
        return len(stack) == 0
        