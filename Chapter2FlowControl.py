#This script explore the basic syntax for flow control objects and statements
import time, random, sys, os, math


i=1
while i<10:
    #staller=input('Please press enter to continue...')
    timeConstant=0.3
    time.sleep(timeConstant)
    if i==7:
        print('Gotcha, lucky one')
        break
    elif i==5:
        print('Just a few more, I promise')
        i+=1
    else:
        i+=1
        print('Almost...')
print('Finally, the counter is at numero 7 :3 now lets go backwards')
for i in range(7,-1,-1):
    time.sleep(timeConstant)
    if i<1:
        print('BOOOOM!')
    else:
        print('Counting back like a badass, we are at: '+str(i)+', but also look at this random number: '+str(random.randint(-100,100))) 
#print(str(range(7,0,-1)))


