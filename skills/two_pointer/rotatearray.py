from typing import List


def rotateArray(nums: List[int], k: int) -> List[int]:
    k %= len(nums)
    
    def reverse(nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)
    print(nums)
    return nums


if __name__ == "__main__":
    if rotateArray([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]:
        print('pass')
    else:
        print('fail')

    if rotateArray([-1, -100, 3, 99], 2) == [3, 99, -1, -100]:
        print('pass')
    else:
        print('fail')
