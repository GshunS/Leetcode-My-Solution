# 238. Product of Array Except Self
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    left = [1]
    right = [1]
    res = []
    count = 1
    for n in nums:
        count *= n
        left.append(count)

    count = 1
    for n in reversed(nums):
        count *= n
        right.append(count)

    for i in range(len(nums)):
        res.append(left[i] * right[-2-i])
    return res


nums = [1, 2]
print(productExceptSelf(nums))
