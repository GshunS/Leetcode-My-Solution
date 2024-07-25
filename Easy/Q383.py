# 383. Ransom Note
def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    a_dict = {}
    for letter in magazine:
        if letter not in a_dict:
            a_dict[letter] = 1
        else:
            a_dict[letter] += 1

    for letter in ransomNote:
        if letter in a_dict:
            if a_dict[letter] == 0:
                return False
            else:
                a_dict[letter] -= 1
        else:
            return False
    return True

ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))