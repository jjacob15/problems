from lib2to3.refactor import MultiprocessingUnsupported


# musings
# two pointer array means, you have two pointer at preferrable two ends or starting at the same point, make a comparison and then only move one
#you can have a third pointer to deal with result and not have to use the two pointers.
from typing import List


def squaredSort(nums: List[int]):
    left = 0
    right = len(nums) - 1
    sorted = [0] * len(nums)
    sortedP = right

    while(left <= right):
        if (abs(nums[left]) > abs(nums[right])):
            sorted[sortedP] = nums[left] * nums[left]
            sortedP -= 1
            left += 1
        else:
            sorted[sortedP] = nums[right] * nums[right]
            sortedP -= 1
            right -= 1

    print(sorted)
    return sorted


if __name__ == "__main__":
    if squaredSort([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]:
        print('pass')
    else:
        print('fail')
    if squaredSort([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]:
        print('pass')
    else:
        print('fail')
    if squaredSort([10,11,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9,10,11]:
        print('pass')
    else:
        print('fail')
