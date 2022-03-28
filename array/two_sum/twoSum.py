from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dict = {}
    for i in range(len(nums)):
        dict[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dict and dict[complement] != i:
            return [i, dict[complement]]


if __name__ == "__main__":
   result = twoSum([1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1], 11)
   print(result)
