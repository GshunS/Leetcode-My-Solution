# 125. Valid Palindrome

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.lower()
    left = ''
    for c in s:
        if c.isalnum():
            left += c

    return left == left[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
