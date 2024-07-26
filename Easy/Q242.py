# 242. Valid Anagram
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    a_dict = {}
    if len(s) != len(t):
        return False
    for char in s:
        if char in a_dict:
            a_dict[char] += 1
        else:
            a_dict[char] = 1

    for char in t:
        if char in a_dict:
            a_dict[char] -= 1
            if a_dict[char] < 0:
                return False
        else:
            return False
    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
