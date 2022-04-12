class badVersion:
    def __init__(self, bad):
        self._badversion = bad

    def isBadVersion(self, n):
        return n >= self._badversion

    def firstBadVersion(self, n):
        low = 0
        high = found = n

        while(low < high):
            lb = self.isBadVersion(low)

            if lb:
                return low

            mid = (low + high) // 2
            if self.isBadVersion(low):
                found = min(found, low)
            if self.isBadVersion(high):
                found = min(found, high)
            if self.isBadVersion(mid):
                found = min(found, mid)
                high = mid - 1
            else:
                low = mid + 1
        return found


if __name__ == "__main__":
    b = 1702766719
    c = badVersion(b)
    if c.firstBadVersion(2126753390) == b:
        print('pass')
    else:
        print('fail')

    # b = 5
    # c = badVersion(b)
    # r = c.firstBadVersion(12)
    # print('r', r)
    # if r == b:
    #     print('pass')
    # else:
    #     print('fail')
