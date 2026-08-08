class MinStack:

    def __init__(self):
        self.st = []
        self.min1 = []
    def push(self, val: int) -> None:
        self.st.append(val)
        minv = min(val, self.min1[-1] if self.min1 else val)
        self.min1.append(minv)

    def pop(self) -> None:
        self.st.pop()
        self.min1.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min1[-1]
