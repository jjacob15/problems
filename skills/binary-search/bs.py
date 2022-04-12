def search(nums, target):
    low = 0
    high = len(nums) - 1

    if high == low:
        return 0 if nums[0] == target else -1


    while low <= high:
        # if nums[low] == target:
        #     return low
        # if nums[high] == target:
        #     return high

        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1


if __name__ == "__main__":
    if search([1,2,3,4,5,6,7,8,9,10],5) == 4:
        print('pass')
    else:
        print('fail')

    if search([1,2,3,4,5,6,7,8,9],5) == 4:
        print('pass')
    else:
        print('fail')

    if search([-1,0,3,5,9,12],2) == -1:
        print('pass')
    else:
        print('fail')

    if search([2,5],5) == 1:
        print('pass')
    else:
        print('fail')

    if search([-1, 0, 5], 5) == 2:
        print('pass')
    else:
        print('fail')
