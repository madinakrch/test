# def bubble_sort(lst):
#     for i in range(len(lst) - 1):
#         for j in range(len(lst) - i - 1):
#             print(i, j)
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     return lst
#
# print(bubble_sort([1, 5, 8, 20, 0, 10, 45, 2, 3]))

#
# def merge(left, right):
#     new_list = []
#     while len(right) and len(left):
#         if left[0] < right[0]:
#             new_list.append(left.pop(0))
#         else:
#             new_list.append(right.pop(0))
#     return [*new_list, *left, *right]
#
# def merge_sort(nums):
#     if len(nums) < 2:
#         return nums
#     else:
#         left = nums[:len(nums) // 2]
#         right = nums[len(nums) // 2:]
#
#         return merge(merge_sort(left), merge_sort(right))


# def shell_sort(nums):
#     mid = len(nums) // 2
#     while mid > 0:
#         for i in range(mid, len(nums)):
#             current_value = nums[i]
#             pos = i
#             while pos >= mid and nums[pos - mid] > current_value:
#                 nums[pos] = nums[pos - mid]
#                 pos -= mid
#                 nums[pos] = current_value
#
#         mid //= 2
#     return nums
#
# print(shell_sort([1, 5, 0, 2, 7, 5]))
import random
#
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = random.choice(arr)
        less = list(filter(lambda el: el < pivot, arr))
        greater = list(filter(lambda el: el > pivot, arr))
        return [*quick_sort(less), pivot, *quick_sort(greater)]

print(quick_sort([1, 5, 0, 2, 7, 5]))

#
# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]
#
# def shift_down(arr, i, upper):
#     while True:
#         l, r = i*2+1, i*2+2
#         if max(l, r) < upper:
#             if arr[i] >= max(arr[l], arr[r]): break
#             elif arr[l] > arr[r]:
#                 swap(arr, i, l)
#                 i = l
#             else:
#                 swap(arr, i, r)
#                 i = r
#         elif l < upper:
#             if arr[l] > arr[i]:
#                 swap(arr, i, l)
#                 i = l
#             else: break
#         elif r < upper:
#             if arr[r] > arr[i]:
#                 swap(arr, i, r)
#                 i = r
#             else: break
#         else: break
#
# def heap_sort(arr):
#     for j in range((len(arr) - 2) // 2, -1, -1):
#         shift_down(arr, j, len(arr))
#
#     for end in range(len(arr) - 1, 0, -1):
#         swap(arr, 0, end)
#         shift_down(arr, 0, end)
#     return arr
#
# print(heap_sort([5, 7, 9, 1, 0, 4, 3]))
