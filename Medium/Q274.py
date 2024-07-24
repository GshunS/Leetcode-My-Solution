# 274. H-Index
def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    a_list = [0] * (max(citations)+2)
    for n in citations:
        a_list[0] += 1
        a_list[n+1] -= 1

    add = a_list[0]
    for i in range(1, len(a_list)):
        a_list[i] += add
        add = a_list[i]

    for i in range(len(a_list)):
        if a_list[i] < i:
            return i - 1

citations = [3]
print(hIndex(citations))
