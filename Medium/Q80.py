# 80. Remove Duplicates from Sorted Array II
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    prev = nums[0]
    count = 1
    k = 1
    for i in range(1, len(nums), 1):
        if nums[i] == prev:
            count += 1
            if count > 2:
                nums[i] = float('inf')
            else:
                k += 1
        else:
            count = 1
            prev = nums[i]
            k += 1
    nums.sort()
    return k


def removeDuplicates2(nums):
    j = 1
    for i in range(1, len(nums)):
        if (j == 1 or nums[i] != nums[j - 2]):
            nums[j] = nums[i]
            j += 1
    return j


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(removeDuplicates2(nums))
print(nums)
