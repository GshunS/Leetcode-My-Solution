# 28. Find the Index of the First Occurrence in a String

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    a_list = haystack.split(needle)
    if len(a_list) == 1:
        if a_list[0] == needle:
            return 0
        else:
            return -1

    return len(a_list[0])

print(strStr("sadbutsad", "but"))
