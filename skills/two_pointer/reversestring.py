from typing import List
def reverseWords(s: str) -> str:
    def reverseString(s: str) -> str:
        n = len(s)
        x = ""
        for i in range(n-1,-1,-1):
           x += s[i]
        return x
    words = s.split(" ")
    result = ""
    for w in words:
        result += reverseString(w) + " "

    result =  result.strip()
    return result

if __name__ == "__main__":
    if reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc":
        print('pass')
    else:
        print('fail')
