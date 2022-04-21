def longestPalindrome(s: str) -> str:
    p = 0
    result = ""

    if len(s) == 1:
        return s

    def lookForPalindrome(p, isEven):
        if isEven and p ==0:
            yield s[0]
        left = (p - 1) if not isEven else p
        right = p + 2  # if not isEven else 1
        while left >= 0 and right <= len(s):
            sub = s[left:right]
            print(sub)
            if sub[0] != sub[-1]:
                break
            yield(sub)
            left -= 1
            right += 1

    while p <= len(s)-1:
        for r in lookForPalindrome(p, False):
            if len(r) > len(result):
                result = r
        for r in lookForPalindrome(p, True):
            if len(r) > len(result):
                result = r
        p += 1

    return result


if __name__ == "__main__":
    for a in range(len("abcd")):
        print(a)

    # if longestPalindrome("abcdefghij") == "":
    #     print("pass1")
    # if longestPalindrome("babbab") == "babbab":
    #     print("pass2")
    # if longestPalindrome("cbbd") == "bb":
    #     print("pass3")

    # if longestPalindrome("a") == "a":
    #     print("pass3")
    # if longestPalindrome("ac") == "a":
    #     print("pass4")
    # if longestPalindrome("bb") == "bb":
    #     print("pass5")
