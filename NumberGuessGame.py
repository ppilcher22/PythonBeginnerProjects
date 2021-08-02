import random

def clueGenerator(number):
    clue = 'The number... \n'
    for x in range(2,10):
        if number % x == 0:
            clue = clue + 'is divisible by '+ str(x)+'\n' 
    return clue

number = random.randint(1,100)
print(clueGenerator(number))


attempts = 1
guess = int(input('Enter guess: '))


while(guess != number):
    if(guess > number):
        print('Lower')
        guess = int(input('Enter guess: '))
    else: 
        print('higher')
        guess = int(input('Enter guess: '))
    attempts += 1
    

print('You guessed '+ str(number) + ' correctly in ' +str(attempts)+ ' attempt(s)!\n')
    
