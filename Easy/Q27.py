# 27. Remove Element


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    temp = [num for num in nums if num != val]
    for i in range(len(temp)):
        nums[i] = temp[i]
    return len(temp)


nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))
print(nums)
