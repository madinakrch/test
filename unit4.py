# def task1():
#     return '''\"Don't let the noise of others' opinions
#     drown out your own inner voice.\"
#                                            Steve Jobs '''
#
# print(task1())

# def task2(a, b):
#     return [int(x) for x in range(a+1, b) if int(x) % 2 != 0]
#
# print(task2(4, 12))

# def task3(length, diraction, symbol):
#     for i in range(length):
#         if diraction == 'row':
#             print(symbol, end='\t')
#         elif diraction == 'column':
#             print(symbol, end='\n')
#     print('\n')
#
#
# task3(7, 'column', '*')
# task3(7, 'row', '*')


# def task4(a, b, c, d):
#     return max(a, b, c, d)
# print(task4(4, 15, 9, 7))

# def task5(a, b):
#     print(list(range(a, b)))
#     return sum(range(a, b))
# print(task5(1, 10))

# def task6(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return num != 1
#
# print(task6(7))
# print(task6(54))


# def task7(num):
#     if int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5]):
#         return True
#     else:
#         return False
#
# print(task7('123420')) #happy number
# print(task7('723422')) #unhappy number


# a = '1234554321'
# mid = len(a)  // 2
# print(a[0:mid])
# print(a[len(a):mid-1: -1])

# lst = [1, 5, 8, 7, 12]

# for i in range(0, len(lst)):
#     print(lst[i])
lst = [1, 5, 8, 7, 12]
# def foo(nums):
#     if len(nums) == 0:
#         return 0
#     elif len(nums) == 1:
#         return nums[0]
#     else:
#         print(nums[0], nums[1:])
#         return foo(nums[1:])
#
# print(foo(lst))

# def step(a, b, s=0):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     else:
#         return a * step(a, b - 1)
#
#
# print(step(2, 3))
#2 
# def numsum(a, b):
#     if a == b:
#         return a
#     else:
#         return a + numsum(a + 1, b)
#
# print(numsum(3, 10))

# 3
# def star(n):
#     if n == 1:
#         return '*'
#     else:
#         return '*' + star(n - 1)
#
# print(star(5))

# 5
import random
lst = [random.randint(0, 100) for _ in range(30)]
#
# def foo(nums, i=0, a={}, pos=0, min_sum=0):
#     if len(nums) <= 10:
#         pos = nums[0]
#         a[sum(nums)] = pos
#         min_sum = min(a.keys())
#         print(nums, a, pos, min_sum)
#         return a[min_sum]
#     else:
#         pos = nums[0]
#         a[sum(nums[i:10])] = pos
#         min_sum = min(a.keys())
#         print(nums, a, pos, min_sum)
#         return foo(nums[i+1:len(nums)], i, a, pos, min_sum)
#
# print(foo(lst))

def foo(nums):
    sums_lst = []
    acc = {}
    for i in range(len(nums)):
        if i == (len(nums) - 9):
            break
        sum_10 = sum(nums[i: len(nums)][:10])
        sums_lst.append(sum_10)
        acc[sum_10] = nums[i]
    return acc[min(acc.keys())]

print(foo(lst))