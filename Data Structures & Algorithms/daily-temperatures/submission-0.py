class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = deque()
        i_stack = deque()
        stack.append(temperatures[0])
        i_stack.append(0)
        for i in range(1, len(temperatures)):
            if len(stack) > 0: # If there are previous days 
                if stack[-1] >= temperatures[i]: # If the current day is less than all previously recorded days
                    stack.append(temperatures[i])
                    i_stack.append(i)
                else: # If it is warmer than a previous day
                    while len(stack) > 0 and stack[-1] < temperatures[i]:
                        stack.pop()
                        last_index = i_stack.pop()
                        result[last_index] = i - last_index
                    stack.append(temperatures[i])
                    i_stack.append(i)
            #else: # No previous days
                
        return result

            
