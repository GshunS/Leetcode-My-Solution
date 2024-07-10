# 134. Gas Station
def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    left = []
    for i in range(len(gas)):
        left.append(gas[i] - cost[i])

    if sum(left) < 0:
        return -1

    current_index = 0
    begin_index = current_index
    total_amount = 0
    while True:
        total_amount += left[current_index % len(gas)]
        current_index += 1
        if total_amount < 0:
            begin_index = current_index
            total_amount = 0

        if (current_index != begin_index) & (current_index % len(gas) == begin_index):
            break

    return begin_index


gas = [5, 8, 2, 8]
cost = [6, 5, 6, 6]
print(canCompleteCircuit(gas, cost))
