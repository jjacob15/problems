from typing import List


# def two_sum(nums: List[int], addVal: int, ans: List[List[int]]) -> List[int]:
#     dict = {}
#     for i in range(len(nums)):
#         dict[nums[i]] = i

#     for key in dict:
#         complement = -addVal - key
#         if complement in dict and dict[complement] != dict[key]:
#             found = sorted([addVal, key, complement])
#             if(found not in ans):
#                 ans.append(found)

# def three_sum(nums: List[int]) -> List[List[int]]:
#     if len(nums) > 2 and list(set(nums)) == [0]:
#         return[[0, 0, 0]]

#     ans = []
#     for i in range(len(nums)):
#         two_sum(sorted(nums[0:i]+nums[i+1:]), nums[i], ans)

#     return ans

def three_sum(nums: List[int]) -> List[List[int]]:
    ans = []
    nums = sorted(nums)
    n = len(nums)

    for i in range(n-2):
        j = i+1
        k = n-1

        if nums[i] > 0:  # end if i itself is greater than zero
            break

        if i > 0 and nums[i] == nums[i - 1]: # fast forward if next value is same as before 
            continue

        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]: #fast forward if next value is same as before
                    j += 1
                while j < k and nums[k] == nums[k+1]: #fast forward if next value is same as before
                    k -= 1
    return ans


def test1():
    result = three_sum([-1, 0, 1, 2, -1, -4])
    if len(result) != 2:
        print('fail')
        return
    for arr in result:
        if sum(arr) != 0:
            print('fail')
            return
    print('pass')


def test2():
    result = three_sum([])
    if len(result) == 0:
        print('pass')
        return
    print('fail')


def test3():
    result = three_sum([0])
    if len(result) == 0:
        print('pass')
        return
    print('fail')


def test4():
    result = three_sum([0, 0, 0])
    print(result)
    if len(result) == 1:
        print('pass')
        return
    print('fail')


def test5():
    #[[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
    result = three_sum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4])
    print(result)
    if len(result) == 9:
        print('pass')
        return
    print('fail')


def test6():
    result = three_sum(
        [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0])
    print('expected', [[-5, 1, 4], [-4, 0, 4],
          [-4, 1, 3], [-2, -2, 4], [-2, 1, 1], [0, 0, 0]])
    print(result)
    if len(result) == 6:
        print('pass')
        return
    print('fail')


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    # a =[[1,2,3]]
    # b = [1,2,3]
    # print(b in a)
    # print(list(set([(1, 2), (1, 2)])))
