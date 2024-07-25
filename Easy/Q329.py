# 392. Is Subsequence

def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if s == "":
        return False
    index = 0
    for letter in t:
        if letter == s[index]:
            index += 1
            if index >= len(s):
                return True

    return False

print(isSubsequence("abc", "ahbgdc"))
