# 205. Isomorphic Strings

def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dict1 = {}
    dict2 = {}

    for i in range(len(s)):
        if s[i] not in dict1:
            dict1[s[i]] = t[i]
        else:
            if dict1[s[i]] != t[i]:
                return False

        if t[i] not in dict2:
            dict2[t[i]] = s[i]
        else:
            if dict2[t[i]] != s[i]:
                return False

    return True

s = "paper"
t = "title"
print(isIsomorphic(s, t))
