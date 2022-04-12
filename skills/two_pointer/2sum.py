from typing import List


def twoSum(numbers: List[int],target:int) -> List[int]:
    left = 0
    right = len(numbers) -1
    while(left < right):
        if numbers[right] +numbers[left] > target:
            right -= 1
        elif numbers[right] +numbers[left] < target:
            left +=1        
        else:
            return [left + 1, right+1]
        


if __name__ == "__main__":
    if twoSum([2,7,11,15],9) == [1, 2]:
        print('pass')
    else:
        print('fail')

    if twoSum([2,3,4],6) == [1, 3]:
        print('pass')
    else:
        print('fail')
    if twoSum([-1,0],-1) == [1, 2]:
        print('pass')
    else:
        print('fail')
