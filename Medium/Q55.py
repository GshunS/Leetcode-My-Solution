# 55. Jump Game

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 1:
        return True
    count = 0
    for i in range(len(nums) - 2, -1, -1):
        count += 1
        if nums[i] >= count:
            count = 0

    if count == 0:
        return True
    return False


nums = [1, 0, 1, 0]
print(canJump(nums))
