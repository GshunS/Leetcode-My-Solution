# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    if sum(A) != (len(A) * 10):
        return -1

    move = 0
    correct = 0
    index = 0
    still_need = 0
    while correct < len(A):
        if index == len(A) - 1:
            if A[index] == 10:
                correct += 1
            index = 0

        if A[index] > 10:
            A[index + 1] += (A[index] - 10)
            correct += 1
            move += A[index] - 10
            A[index] = 10

        elif A[index] < 10:
            diff = 10 + still_need - A[index]
            if diff <= A[index + 1]:
                A[index] = 10 + still_need
                A[index + 1] -= diff
                move += diff
                correct += 1
            else:
                move += A[index + 1]
                A[index] += A[index + 1]
                A[index + 1] = 0
                still_need = 10 - A[index]

        else:
            correct += 1
        index += 1
        index %= len(A) - 1
        print(A)

    return move

print(solution([11, 10, 8, 12, 8, 10, 11]))