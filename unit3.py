# 2
# nums = [int(x) for x in input('Enter nums = ').split()]
# n = int(input('Enter a number = '))
# print(nums.count(n))

# 3
# nums = [int(x) for x in input('Enter nums = ').split()]
# nums_sum = sum(nums)
# print(f'Sum = {nums_sum}')
# print(f'Avg = {nums_sum / len(nums)}')


# 1
# nums = [int(x) for x in input('Enter nums = ').split()]

# nums_sum = sum(x for x in nums if x < 0)  #Sum of negatives
#
# nums_sum = sum(x for x in nums if x % 2 == 0)  #Sum of evens
# nums_sum = sum(x for x in nums if x % 2 != 0)  #Sum of odds

# Произведение элементов с индексами кратными 3;
# k = 1
# for i in range(len(nums)):
#     if i % 3 == 0:
#         print(i)
#         k *= nums[i]
# print(k)

# Произведение элементов между минимальным и максимальным элементом;
# max_el = max(nums)
# min_el = min(nums)
# k = 1
# lim1 = nums.index(min_el)
# lim2 = nums.index(max_el)
# print(lim1, lim2)
# for i in range(min(lim1, lim2) + 1, max(lim1, lim2)):
#     print(nums[i])
#     k *= nums[i]
# print('Multi... = ', k)

# Сумму элементов, находящихся между первым и
# последним положительными элементами.
# indx = []
# for i in range(len(nums)):
#     if nums[i] > 0:
#         indx = [*indx, nums.index(nums[i])]
# print(indx)
# print('Sum = ', sum(nums[indx[0]: indx[-1]+1]))

# Есть список целых, заполненный случайными числами. # На основании данных этого массива нужно: # ■ Создать список целых,
# содержащий только четные # числа из первого списка;
nums_even = [int(x) for x in input('Enter nums = ').split() if int(x) % 2 == 0]
print(nums_even)

# Создать список целых, содержащий только нечетные
# числа из первого списка;
# nums_odds = [int(x) for x in input('Enter nums = ').split() if int(x) % 2 != 0]
# print(nums_odds)

# Создать список целых, содержащий только отрицательные числа из первого списка;
# nums_pos = [int(x) for x in input('Enter nums = ').split() if int(x) > 0]
# print(nums_pos)

# # Создать список целых, содержащий только положительные числа из первого списка.
# nums_neg = [int(x) for x in input('Enter nums = ').split() if int(x) < 0]
# print(nums_neg)

