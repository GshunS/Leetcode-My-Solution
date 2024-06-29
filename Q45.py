# 45. Jump Game II
# DP O(n^2)
def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums) - 1
    a_dict = {}

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= n:
            a_dict[(i, n)] = 1
        else:
            min_num = float('inf')
            for j in range(i + 1, i + nums[i] + 1):
                min_num = min(1 + a_dict[(j, n)], min_num)
            a_dict[(i, n)] = min_num

    return a_dict[(0, n)]


# BFS Like O(n)

def jump2(nums) -> int:
    ans = 0
    end = 0
    farthest = 0

    # Implicit BFS
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if farthest >= len(nums) - 1:
            ans += 1
            break
        if i == end:  # Visited all the items on the current level
            ans += 1  # Increment the level
            end = farthest  # Make the queue size for the next level

    return ans


nums = [2, 3, 1, 1, 4]
print(jump2(nums))
