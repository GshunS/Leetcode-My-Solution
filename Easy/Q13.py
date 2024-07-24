# 13. Roman to Integer

def romanToInt(s):
    a_dict = {"I": 1,
              "V": 5,
              "X": 10,
              "L": 50,
              "C": 100,
              "D": 500,
              "M": 1000}

    total = 0
    for i in range(len(s)-1):
        if a_dict[s[i]] >= a_dict[s[i + 1]]:
            total += a_dict[s[i]]
        else:
            total -= a_dict[s[i]]

    return total + a_dict[s[-1]]

print(romanToInt('MCMXCIV'))
