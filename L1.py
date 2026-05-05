ans = int(input('enter no'))
for i in range(1+ans):
    if i%3 == 0 and i%5 == 0:
       print('fizzbuzz')
    elif i%3 == 0:
        print('fizz')
    elif i%5 == 0:
        print('buzz')
    else:
        print(i)