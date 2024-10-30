def linear_search(li, target):
    for i in range(len(li)):
        # check if the current element matches the target
        if target == li[i]:
            return i # return the index if the target is found
    return -1 # return -1 if the target is not found

if __name__ == '__main__':
    li = [5, 3, 1, 9, 6, 8, 2, 4, 7]
    target = 8 # target to search for in the list
    index = linear_search(li, target)

    if index == -1:
        print(f'target {target} not found in the list')
    else:
        print(f'target {target} found at index {index}')