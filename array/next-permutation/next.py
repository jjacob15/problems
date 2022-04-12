from typing import List
# the idea here is finding the break point at which the sequence is not ordered. Find that point, 
# swap it with the least from the remaining array and then sort it

def nextPermutation(nums: List[int]) -> None:
    bPoint, n = -1, len(nums)
    for i in range(n-2,-1,-1):
        if nums[i] >= nums[i+1]:
            continue
        bPoint = i
        print(bPoint, nums[i], nums[i+1])
        for j in range(n-1, i, -1):
            if nums[j] > nums[bPoint]:
                nums[j],nums[bPoint]  = nums[bPoint],nums[j]
                break
        break
    nums[bPoint+1:] = sorted(nums[bPoint+1:])
            
    

if __name__ == "__main__":
    # a = [1,2,4,3]
    # nextPermutation(a)
    # print(a)
    b = [1,2,3]
    nextPermutation(b)
    print(b)
    # if a == [1,3,2,4]:
    #     print('pass')
    # else:
    #     print('fail')
