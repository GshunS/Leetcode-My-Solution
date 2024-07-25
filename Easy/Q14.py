# 14. Longest Common Prefix

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    longest = ""
    temp_str = strs.pop()
    index = 0
    for letter in temp_str:
        for s in strs:
            if s.strip() == "" or index >= len(s):
                return longest
            if s[index] != letter:
                return longest
        longest += letter
        index += 1
    return longest

print(longestCommonPrefix(['aaa', 'aa', 'aaa']))
