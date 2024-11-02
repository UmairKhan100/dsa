def binary_search(li, target):
    left, right = 0, len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        # check if the target is at mid
        if li[mid] == target:
            return mid
        elif target > li[mid]:
            left = mid + 1 # ignore the left half
        else:
            right = mid - 1 # ignore the right half
    return -1 # return -1 if the target is not found

if __name__ == '__main__':
    li = [11,33,44,77,109,200,333,511,788,943] # sorted list
    target = 788 # target to search for in the list
    index = binary_search(li, target)

    if index == -1:
        print(f'target {target} not found in the list')
    else:
        print(f'target {target} found at index {index}')