# 202. Happy Number

def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    a_dict = {n: 1}
    while n != 1:
        a_list = [int(num) for num in str(n)]
        total = 0
        for num in a_list:
            total += num ** 2
        n = total
        if n in a_dict:
            return False
        else:
            a_dict[n] = 1
    return True

print(isHappy(2))
