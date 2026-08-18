
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        n = len(self.arr)
        self.arr.sort()
        if n == 1:
            median = self.arr[0]
        elif n%2 == 0:
            mid = n//2
            median = (self.arr[mid] + self.arr[mid-1])/2
        else:
            mid = n//2
            median = self.arr[mid]
        return median
