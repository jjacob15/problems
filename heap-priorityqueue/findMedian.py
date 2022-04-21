"""
The technique is to have two heap queues and check its length. If the length is the same, pushpop from large into small. This pushes the values into 
the large heap, and pops the minimum of that out. That is then pushed into the small queue. This technique will ensure whatever value goes in, the minimum
comes out.
The other trick is the have negative values goes into the small queue, as heapq from python is a minimum priority queue, 
so the largest values becomes the smallest value when popped, which is what is needed

if you change the order of a list, add it with a negative sign,
"""
from heapq import *

class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num: int) -> None:
        print('adding', num)
        if len(self.small) == len(self.large):
            print('if b',self.small,self.large)
            heappush(self.large, -heappushpop(self.small, -num))
            print('if a',self.small,self.large)
        else:
            print('else b', self.small, self.large)
            heappush(self.small, -heappushpop(self.large, num))
            print('else a', self.small, self.large)

    def findMedian(self) -> float:
        print(self.small[0],self.large[0])
        if len(self.small) == len(self.large):
            return (self.large[0]-self.small[0])/2
        else:
            return float(self.large[0])


def CaseOne():
    a = MedianFinder()
    a.addNum(10)
    a.addNum(2)
    a.addNum(18)
    a.addNum(1)
    a.addNum(12)
    a.addNum(3)
    if a.findMedian() == 6.5:
        print("pass")

def CaseTwo():
    a = MedianFinder()
    a.addNum(1)
    a.addNum(2)
    a.addNum(3)
    a.addNum(4)
    a.addNum(5)
    a.addNum(6)
    if a.findMedian() == 3.5:
        print("pass")


def CaseThree():
    a = MedianFinder()
    a.addNum(-1)
    a.addNum(-2)
    a.addNum(-3)
    a.addNum(-4)
    a.addNum(-5)
    if a.findMedian() == -3:
        print("pass")



if __name__ == "__main__":
    CaseOne()
    CaseTwo()
    CaseThree()
