class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = deque()
        stack.append(0)
        for i in range(1, len(temperatures)):
            if len(stack) > 0: # If there are previous days 
            # If the current day is less than all previously recorded days
                while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                    last_index = stack.pop()
                    result[last_index] = i - last_index
            stack.append(i)
        return result

            
