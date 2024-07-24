# 58. Length of Last Word

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    return len(s.strip().split()[-1].strip())

print(lengthOfLastWord("   fly me   to   the moon  "))