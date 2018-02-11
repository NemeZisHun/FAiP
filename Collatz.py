def collatz(number):
    try:
        number=int(number)
        if number%2==0:
          even=number//2
          print(str(even))
          return even
        else:
           odd=number*3+1
           print(str(odd))
           return odd
    except ValueError:
        print("Thats not an integer you dumb fuck!")

print("Oy, gimme an integer and let me show you where the collatz series lead you")
inputNum=input()
while inputNum!=1:
    inputNum=collatz(inputNum)
print('Congrats, you arrived to the end!')
