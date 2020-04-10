class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.min_at_index = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        if self.min is None or self.min > x:
            self.min = x
            self.min_at_index.append(x)
            
        else:
            self.min_at_index.append(self.min_at_index[-1])
        

    def pop(self) -> None:
        if len(self.stack) > 1:
            self.stack.pop()
            self.min_at_index.pop()
            self.min = self.min_at_index[-1]
        
        elif len(self.stack) == 1:
            self.stack.pop()
            self.min_at_index.pop()
            self.min = None

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.min