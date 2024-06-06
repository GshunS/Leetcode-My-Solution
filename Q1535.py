# 1535. Find the Winner of an Array Game

class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        length = len(arr)
        count = 0
        first_index = 0
        second_index = 1
        winner = 0

        if k == 1:
            return max(arr[first_index], arr[second_index])

        while count < k:
            max_one = max(arr[first_index], arr[second_index])
            if winner != max_one:
                count = 0
            else:
                if count == 0:
                    count = 1
            if arr[first_index] > arr[second_index]:
                arr.append(arr[second_index])
                count += 1
                if count >= length:
                    return winner
            else:
                arr.append(arr[first_index])
                first_index = second_index

            winner = max_one
            second_index += 1

        return winner

# Test cases
soln = Solution()
cases = [([2, 1, 3, 5, 4, 6, 7], 2),
         ([3, 2, 1], 10)]

cases = [([1,11,22,33,44,55,66,77,88,99], 1000000000)]
for case in cases:
    print(soln.getWinner(arr=case[0], k=case[1]))
