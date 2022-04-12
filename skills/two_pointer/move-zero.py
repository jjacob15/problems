from typing import List


def moveZeroes(nums: List[int]) -> None:
    left = 0
    right = len(nums)
    while(left < right):
        if nums[left] == 0:
            nums.pop(left)
            nums.append(0)
            # left = 0
            right -= 1
        else:
            left +=1        
        
    return nums


if __name__ == "__main__":
    if moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]:
        print('pass')
    else:
        print('fail')

    if moveZeroes([0, 0, 1, 2]) == [1, 2, 0, 0]:
        print('pass')
    else:
        print('fail')
