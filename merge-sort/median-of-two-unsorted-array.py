def findMedianSortedArrays(nums1, nums2):
    result = []

    while(len(nums1) > 0 and len(nums2) > 0):
        if nums1[0] < nums2[0]:
            result.append(nums1.pop(0))
        else:
            result.append(nums2.pop(0))

    if len(nums1) > 0:
        result.extend(nums1)
    if len(nums2) > 0:
        result.extend(nums2)

    if len(result) % 2 == 0:
        return (result[int(len(result)/2-1)] + result[int(len(result)/2)])/2
    else:
        return result[len(result)//2]



if __name__ == "__main__":
    # a = [1, 2, 3, 4, 5, 6, 7]
    # b = [1, 2, 3, 4, 5, 6]
    # print(len(a) % 2, (len(a)//2))
    # print(len(b) % 2, len(b)/2-1, len(b)/2)
    # print(b//2)
    if findMedianSortedArrays([1, 3], [2]) == 2.0000:
        print('pass')

    if findMedianSortedArrays([1, 2], [3, 4]) == 2.5000:
        print('pass')

    if findMedianSortedArrays([1], [3, 4]) == 3.0:
        print('pass')

    if findMedianSortedArrays([1], []) == 1.0:
        print('pass')
