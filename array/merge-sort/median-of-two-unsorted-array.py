from typing import List


def mergeSort(m1, m2, m):
    i = j = 0
    total = len(m1)+len(m2)
    print('in', m1, m2)
    while i+j < total:
        if j == len(m2) or (i < len(m1) and m1[i] < m2[j]):
            m[i+j] = m1[i]
            i += 1
        else:
            m[i+j] = m2[j]
            j += 1
    print('out', m)


def mergeSortArrays(arr: List) -> List:
    if len(arr) < 2:
        return

    l = len(arr)
    mid = l//2
    m1 = arr[0:mid]
    m2 = arr[mid:l]

    mergeSortArrays(m1)
    mergeSortArrays(m2)
    print('m1->',  m1, 'm2->', m2)

    # mergeSort(m1, m2, arr)


def findMedianUnsortedArrays(nums1: List, nums2: List) -> float:
    nums1.extend(nums2)
    mergeSortArrays(nums1)
    print(nums1)
    return 0.0

    # if len(result) % 2 == 0:
    #     return (result[int(len(result)/2-1)] + result[int(len(result)/2)])/2
    # else:
    #     return result[len(result)//2]


if __name__ == "__main__":
    # print(mergeSort([1, 4], None))
    if findMedianUnsortedArrays([2, 1], [3, 4, 5]) == 2.0000:
        print('pass')

    # if findMedianUnsortedArrays([2, 1], [3, 4]) == 2.5000:
    #     print('pass')

    # if findMedianUnsortedArrays([1], [3, 4]) == 3.0:
    #     print('pass')

    # if findMedianUnsortedArrays([1], []) == 1.0:
    #     print('pass')
