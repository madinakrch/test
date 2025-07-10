from mimetypes import guess_type


def binary_search(arr, item):
    list = sorted(arr)
    print(list)
    low = 0
    height = len(list) - 1

    while low <= height:
        mid = (low + height) // 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            height = mid - 1
        else:
            low = mid + 1
    return -1

print(binary_search([5, 6, 1, 4, 10, 8, 4], 4))