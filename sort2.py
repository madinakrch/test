def insert_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(i+1, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums


print(insert_sort([1, 5, 8, 20, 0, 10, 45, 2, 3]))