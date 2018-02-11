#Preamble declarations
import random

#Function definitions
def guesser(number):
    global count
    try:
        if isinstance(number,float)==True:
            print('Your guess will be rounded down, just so you know...')

        number=int(number)
        if number == secretNumber:
            print('Congratulations, you gueessed my number, which is '+str(secretNumber)+', and you did it in '+str(count)+' guesses, well done boi')
            return True
        elif number > secretNumber:
            count+=1
            print('Your guess is too high, keep going.')
        elif number < secretNumber:
            count+=1
            print('Your guess is too low, keep going.')
    except ValueError:
        print('This is not a natural number')
        return True

#Start of global code
low=1
high=100
secretNumber=random.randint(low,high)
count=1
goodGuess=False

print('I have a number in mind, it is between '+str(low)+' and '+str(high)+' and is a natural number, can you guess it?')

while goodGuess!=True:
    guessNumber=input()
    goodGuess=guesser(guessNumber)