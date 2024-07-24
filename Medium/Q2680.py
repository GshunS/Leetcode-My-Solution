# 2680. Maximum OR

class Solution(object):
    def maximumOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_binary_length = len(format(max(nums), 'b'))

        no_duplicate_dict = {}
        max_prefix = ''
        for num in nums:
            if max_binary_length - len(format(num, 'b')) > 0:
                continue
            else:
                prefix = format(num << k, 'b')[:k]
                if prefix > max_prefix:
                    max_prefix = prefix
                if prefix in no_duplicate_dict:
                    no_duplicate_dict[prefix].append(num)
                else:
                    no_duplicate_dict[prefix] = [num]

        max_num_list = no_duplicate_dict[max_prefix]
        max_total = 0
        for max_num in max_num_list:
            total = 0
            flag = True
            for num in nums:
                if (max_num == num) & flag:
                    flag = False
                    total = total | (num << k)
                else:
                    total = total | num
            if total > max_total:
                max_total = total

        return max_total

    def maximumOr2(self, nums, k):
        res, left, n = 0, 0, len(nums)
        right = [0] * n
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] | nums[i + 1]

        for i in range(n):
            print(left)
            print(nums[i] << k)
            print(right[i])
            res = max(res, left | (nums[i] << k) | right[i])
            left |= nums[i]
        return res

soln = Solution()
cases = [([88, 43, 61, 72, 13], 6),
         ([8, 1, 2], 2)
         ]
cases = [([12, 9], 1)]

for case in cases:
    print(soln.maximumOr2(nums=case[0], k=case[1]))
