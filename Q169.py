# 169. Majority Element

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    temp_dict = {}
    length = len(nums)
    for n in nums:
        if n not in temp_dict:
            temp_dict[n] = 1
        else:
            temp_dict[n] += 1
            if temp_dict[n] > int(length / 2):
                return n
    for k in temp_dict:
        if temp_dict[k] > int(length / 2):
            return k


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
