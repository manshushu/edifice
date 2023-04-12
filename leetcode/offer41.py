from heapq import *


class MedianFinder:
    def __init__(self) -> None:
        self.A = []
        self.B = []

    def addNum(self, num: "int") -> None:
        if len(self.A) != len(self.B):
            heappush(self.B, -heappop(self.A, num))
        else:
            heappush(self.A, -heappop(self.B, num))

    def findMedian(self) -> float:
        return (
            self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
        )
