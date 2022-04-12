from typing import List
def isMonotonic(nums: List[int]) -> bool:
    if len(nums) < 2:
        return True
    isInc = None
    i =0
    while(i < len(nums)-1):
        if isInc is None and nums[i] != nums[i+1]:
            isInc = nums[i] < nums[i+1]
        if isInc and  nums[i] > nums[i+1]:
            return False
        if not isInc and  nums[i] < nums[i+1]:
            return False
        i += 1

    return True
            
if __name__ == "__main__":
    i = 1
    
    print (i//10)
    
    # if isMonotonic([1,1,0,1]):
    #     print('pass')
    # if isMonotonic([1,1,2]):
    #     print('pass')
    # if isMonotonic([1,2,3]):
    #     print('pass')
    # if isMonotonic([1,3,2]):
    #     print('pass')
    # if isMonotonic([5,3,2,4,1]):
    #     print('pass')
            
