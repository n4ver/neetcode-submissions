class MinStack:

    def __init__(self):
        self.minimum = []
        self.values = []
        self.current_min = float("infinity")
        

    def push(self, val: int) -> None:
        self.values.append(val)
        if val < self.current_min:
            self.current_min = val
        self.minimum.append(self.current_min)
        

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
        
