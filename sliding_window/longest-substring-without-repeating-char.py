# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
    if s == None or len(s) == 0:
        return 0
    m = t = maxLen = 0
    mem = []
    while(m < len(s)):
        mItem = s[m]
        if mItem in mem:
            mem.pop(0)
            t += 1
            if len(mem) > 0 and mem[0] == mItem:
                mem.pop(0)
                t += 1
        else:
            mem.append(mItem)
            print(mem)
            m += 1
            maxLen = max(maxLen, len(mem))

    return maxLen


if __name__ == '__main__':
    if(lengthOfLongestSubstring("abcabcbb") != 3):
        print('failed')
    else:
        print('pass')
    if(lengthOfLongestSubstring("bbbbb") != 1):
        print('failed')
    else:
        print('pass')
    if(lengthOfLongestSubstring("pwwkew") != 3):
        print('failed')
    else:
        print('pass')

    if(lengthOfLongestSubstring("") != 0):
        print('failed')
    else:
        print('pass')
