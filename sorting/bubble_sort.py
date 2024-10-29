def bubble_sort(li):
    n = len(li)
    # traverse through all elements in the array
    for i in range(n):
        # set a flag to optimize the algorithm
        swapped = False
        # last i elements are already in place
        for j in range(0, n - i - 1):
            # swap if the element found is greater than the next element
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j+1], li[j]
                swapped = True
        # if no elements were swapped, the array is already sorted
        if not swapped:
            break

if __name__ == '__main__':
    li = [5, 3, 1, 9, 6, 8, 2, 4, 7] # example list to sort
    print('original list:', li)
    bubble_sort(li)
    print('sorted list:', li)