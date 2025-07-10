import random
import time
# d = 100
#
# while True:
#     comand = int(input('Enter 1 or 2'))
#     if comand == 1:
#         sum = int(input('Enter amount = '))
#         print('Итог = ', d * sum)
#     elif comand == 2:
#         break


# l1 = int(input('Enter l1 = '))
# l2 = int(input('Enter l2 = '))
# num = int(input('Enter num = '))
#
# while not(l1 <= num and num <= l2):
#     num = int(input('Enter num = '))
#
# for i in range(l1, l2 + 1):
#     if num == i:
#         print(f'!{i}!')
#     else:
#         print(i)


num = random.randint(1, 5)
attempt = 0
sec = time.time()
print(num)
struct = time.localtime(sec)
print(time.strftime('%d.%m.%Y %H:%M.%S', struct))


while True:
    guess = int(input('Guess = '))
    if guess == 0:
        break
    elif guess > num:
        print('Less ...')
        attempt += 1
    elif guess < num:
        print('More...')
        attempt += 1
    else:
        print('U guessed')
        attempt += 1

struct = time.localtime(sec)
print(time.strftime('%H:%M:%S', struct))
print('Attempts = ', attempt)