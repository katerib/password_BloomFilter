
def binary_search(search, target, length):
    """
    performs a binary search on passed data
    :param search: haystack
    :param target: needle
    :param length: length of data to search (ie. haystack)
    :return: found target ('middle') OR bool (False)
    """
    first = 0
    last = length - 1
    while first <= last:
        mid = (first + last) // 2
        middle = search[mid]
        if middle < target:
            first = mid + 1
        elif middle > target:
            last = mid - 1
        else:
            return middle
    return False
