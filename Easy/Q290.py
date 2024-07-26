# 290. Word Pattern

def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    a_dict = {}
    repeat_dict = {}
    s = s.split(" ")

    if len(s) != len(pattern):
        return False
    for i in range(len(s)):
        if pattern[i] not in a_dict:
            if s[i] not in repeat_dict:
                a_dict[pattern[i]] = s[i]
                repeat_dict[s[i]] = 0
            else:
                return False
        else:
            if a_dict[pattern[i]] != s[i]:
                return False

    return True

pattern = "abba"
s = "dog dog dog dog"
print(wordPattern(pattern, s))
