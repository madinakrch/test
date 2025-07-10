import math
# import random
#
# count = 0
# for i in range(0, random.randint(1, 6)):
#     x = random.randint(1, 10)
#     y = random.randint(1, 10)
#     print(f'x = {x} * y = {y}')
#     ans = int(input('Enter an answer = '))
#     if x * y == ans:
#         count += 1
# print('счет = ', count)
from random import random

n = int(input('Enter n = '))

for i in range(0, n // 2):
    # print(math.ceil(n / 2) - i, math.ceil(n / 2) + i)
    for k in range(math.ceil(n / 2) - i, math.ceil(n / 2) + i):
        print('*' * k, end='\t')
    # for j in range(0, n):
        # print(math.ceil(n / 2) - i, math.ceil(n / 2) + i, j)

        # if math.ceil(n / 2) - i == j or math.ceil(n / 2) + i == j:
        #     for k in range(math.ceil(n / 2) - i, math.ceil(n / 2) + i):
        #         print('*', end='\t')
        # else:
        #     print('', end='\t')
    print('\n')

# for i in range(n // 2, n):


l = (('name', 'age', 'mark', 8, True), ('name', 'age', 'mark', 8, True), ('name', 'age', 'mark', 8, True), ('name', 'age', 'mark', 8, True))


