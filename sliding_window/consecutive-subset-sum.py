# sliding window pattern for consecutive subset sum

def maxConsecutiveSubsetSum(arr, n):
    if len(arr) == 0:
        return None

    maxSum = tempVal = sum(arr[0:n])
    p1 = 0
    p2 = n
    while(p2 < len(arr)):
        tempVal = tempVal - arr[p1] + arr[p2]
        if(tempVal > maxSum):
            maxSum = tempVal
        p1 += 1
        p2 += 1

    return maxSum


if __name__ == '__main__':
    if(maxConsecutiveSubsetSum([7, 9, 20, 4, 9, 3, 11, 4, 3], 2) != 29):
        print('failed')
    else:
        print('pass')
    if(maxConsecutiveSubsetSum([4, 5, 7, 9, 20, 4, 9, 3, 11, 4, 3], 3) != 36):
        print('failed')
    else:
        print('pass')
    if(maxConsecutiveSubsetSum([1, 1, 1], 3) != 3):
        print('failed')
    else:
        print('pass')
    if(maxConsecutiveSubsetSum([], 3) != None):
        print('failed')
    else:
        print('pass')
