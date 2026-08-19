import bisect
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)

    def findMedian(self) -> float:
        n = len(self.arr)
        self.arr.sort()
        if n%2 == 0:
            mid = n//2
            median = (self.arr[mid] + self.arr[mid-1])/2
        else:
            mid = n//2
            median = self.arr[mid]
        return median
