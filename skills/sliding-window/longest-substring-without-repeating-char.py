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
    dict = {}
    left = 0
    right = 0
    maxlength = 0
    while right < len(s):
        if s[right] not in dict:
            dict[s[right]] = right
        else:
            left = max(left, dict[s[right]] + 1)
            dict[s[right]] = right
        maxlength = max(maxlength, right - left +1)
        right +=1

    return maxlength



if __name__ == '__main__':
    # if(lengthOfLongestSubstring("abcabcbb") != 3):
    #     print('failed')
    # else:
    #     print('pass')
    # if(lengthOfLongestSubstring("bbbbb") != 1):
    #     print('failed')
    # else:
    #     print('pass')
    # if(lengthOfLongestSubstring("pwwkew") != 3):
    #     print('failed')
    # else:
    #     print('pass')

    # if(lengthOfLongestSubstring("") != 0):
    #     print('failed')
    # else:
    #     print('pass')

    if(lengthOfLongestSubstring("abba") != 2):
        print('failed')
    else:
        print('pass')
