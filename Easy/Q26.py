# 26. Remove Duplicates from Sorted Array

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a_dict = {}
    k = 0
    for n in nums:
        if n not in a_dict:
            a_dict[n] = 0
            nums[k] = n
            k += 1
    return k


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
print(nums)
