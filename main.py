# Task1

try:
    num = input('Enter a number')
    if len(num) < 0 or len(num) > 6:
        raise Exception('Enter number length from 0 to 6')
    if int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5]):
        print('Happy number')
    else:
        print('Unhappy number')
except:
    print('We have troubles')
finally:
    print('The END')


# Task2
try:
    num = input('Enter a number')
    if len(num) < 0 or len(num) > 6:
        raise Exception('Enter number length from 0 to 6')
    first = num[0]
    second = num[1]
    fifth = num[4]
    sixth = num[5]
    print(sixth+fifth+num[2:4]+second+first)
except Exception as e:
    print('We have troubles', e)
finally:
    print('The END')








