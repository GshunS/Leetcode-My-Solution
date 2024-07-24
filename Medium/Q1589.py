# 1589. Maximum Sum Obtained of Any Permutation
from operator import itemgetter


class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        sorted_num = sorted(nums, reverse=True)
        repeat_dict = {}
        # temp_dict = {}
        times = []
        for list_range in requests:
            times.append((list_range[0], True))
            times.append((list_range[1], False))

        times.sort()
        times.append((float('inf'), False))
        true_count = false_count = 0

        for i in range(len(times) - 1):
            if (times[i][0], times[i][0]) in repeat_dict:
                if times[i][1] + times[i-1][1] != 0:
                    repeat_dict[(times[i][0], times[i][0])] += 1

            if times[i + 1][0] - times[i][0] == 1:
                if times[i][1]:
                    true_count += 1
                    if (times[i][0], times[i][0]) not in repeat_dict:
                        repeat_dict[(times[i][0], times[i][0])] = true_count - false_count
                else:
                    if (times[i][0], times[i][0]) not in repeat_dict:
                        repeat_dict[(times[i][0], times[i][0])] = true_count - false_count
                    false_count += 1

            elif times[i + 1][0] - times[i][0] > 1:
                if times[i][1]:
                    true_count += 1
                    if (times[i][0], times[i][0]) not in repeat_dict:
                        repeat_dict[(times[i][0], times[i][0])] = true_count - false_count
                    if times[i + 1][0] == float('inf'):
                        break
                    repeat_dict[(times[i][0] + 1, times[i + 1][0] - 1)] = true_count - false_count
                else:
                    if (times[i][0], times[i][0]) not in repeat_dict:
                        repeat_dict[(times[i][0], times[i][0])] = true_count - false_count
                    if times[i + 1][0] == float('inf'):
                        break
                    false_count += 1
                    repeat_dict[(times[i][0] + 1, times[i + 1][0] - 1)] = true_count - false_count

            else:
                if not times[i][1]:
                    if (times[i][0], times[i][0]) not in repeat_dict:
                        repeat_dict[(times[i][0], times[i][0])] = true_count - false_count
                    false_count += 1
                else:
                    true_count += 1
                    if (times[i][0], times[i][0]) not in repeat_dict:
                        repeat_dict[(times[i][0], times[i][0])] = true_count - false_count

        total = 0
        sorted_list = sorted(repeat_dict.items(), key=itemgetter(1), reverse=True)

        start_point = 0
        for element in sorted_list:
            start = element[0][0]
            end = element[0][1]
            repeat_times = element[1]
            duration = end - start + 1
            if duration == 1:
                total += sorted_num[start_point] * repeat_times
            else:
                total += sum(sorted_num[start_point: start_point + duration]) * repeat_times
            start_point += duration

        return total % (10 ** 9 + 7)

# Test cases
soln = Solution()
cases = [([1, 8, 5, 5, 2], [[4, 4], [3, 4], [4, 4], [2, 4], [0, 0]]),
         ([1, 2, 3, 4, 5], [[1, 3], [0, 1]]),
         ([1, 2, 3, 4, 5, 6], [[0, 1]]),
         ([1, 2, 3, 4, 5, 10], [[0, 2], [1, 3], [1, 1]])]

for case in cases:
    print(soln.maxSumRangeQuery(nums=case[0], requests=case[1]))
