class MinStack:

    def __init__(self):
        self.minimum = []
        self.values = []
        

    def push(self, val: int) -> None:
        self.values.append(val)
        self.minimum.append(min(self.minimum[-1], val) if self.minimum else val) 
        

    def pop(self) -> None:
        self.values.pop(-1)
        self.minimum.pop(-1)
        if len(self.minimum) > 0:
            self.current_min = self.minimum[-1]
        else:
            self.current_min = float("infinity")
        

    def top(self) -> int:
        return self.values[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        
