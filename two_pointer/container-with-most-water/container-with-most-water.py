from typing import List


def maxArea(height: List[int]) -> int:
    i = maxarea = 0
    j = len(height) - 1
    while(i < j):
      ival = height[i]
      jval = height[j]
      conservativeHeight = min(ival, jval)
      width = j-i
      maxarea = max(maxarea, conservativeHeight * width)
      if(ival < jval):
        i += 1
      else:
        j -= 1

    return maxarea


if __name__ == "__main__":
    if maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49:
        print('pass')
