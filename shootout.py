from time import sleep
from random import randint
import msvcrt
import os

os.system('cls||clear')

print ('COWBOY SHOOTOUT'
       '/n''YOU ARE BACK TO BACK'
       '/n''TAKE 10 PACES...')

W = 1
while W <= 10:
    sleep(0.2)
    print (W, '...')
    W += 1

S = randint(1,5)
sleep(S*0.2)
print ('HE DRAWS...')

X = 0
while X < S:
    if msvcrt.kbhit() == True:
        print ('BUT YOU SHOOT FIRST'
               '/n''YOU KILLED HIM')
        exit()
    else:
        sleep(0.2)
        X = X + 1

print('AND SHOOTS'
      '/n''YOU ARE DEAD')