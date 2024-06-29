def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    k %= len(nums)

    count = 0
    for n in (nums[-k:] + nums[:-k]):
        nums[count] = n
        count += 1


# space O(1) solution
# nums = [1,2,3,4, 5,6,7], k = 3
# [1,2,3,4, 5,6,7] -> [4,3,2,1, 7,6,5] -> [5,6,7, 1,2,3,4]
def reverse(nums, i, j):
    li = i
    ri = j

    while li < ri:
        nums[li], nums[ri] = nums[ri], nums[li]
        li += 1
        ri -= 1


def rotate1(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    if k < 0:
        k += len(nums)

    reverse(nums, 0, len(nums) - k - 1)
    reverse(nums, len(nums) - k, len(nums) - 1)
    reverse(nums, 0, len(nums) - 1)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate1(nums, k)
print(nums)
