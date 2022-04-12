from typing import List


def searchInsert(nums: List[int], target: int):
    low = 0
    high = len(nums) - 1
    closesValUsed = nums[high]
    closestVal = nums[high]
    while(low<=high):
        mid = (low + high) //2
        if nums[mid] > target:
            high = mid -1
        elif nums[mid]  < target:
            low = mid + 1
        else:
            return mid

        if closestVal > abs(nums[mid]-target):
            closestVal = abs(nums[mid]-target)
            closesValUsed = nums[mid]     

    if target > closesValUsed:
        return nums.index(closesValUsed) + 1
    else:
        return nums.index(closesValUsed)

if __name__ == "__main__":
    a = [1,2,3,4,5]
    if searchInsert([1,3,5,6],5) == 2:
        print('pass')
    else:
        print('fail')

    if searchInsert([1,3,5,6],2) == 1:
        print('pass')
    else:
        print('fail')

    if searchInsert([1,3,5,6,8],7) == 4:
        print('pass')
    else:
        print('fail')

    if searchInsert([1,3,5,6],0) == 0:
        print('pass')
    else:
        print('fail')
