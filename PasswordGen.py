#Ask user how many chars in password
#...
#Generater and print password

import random

lowerCaseLetters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
upperCaseLetters = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
numbers = ('1','2','3','4','5','6','7','8','9','0')
specialChars = ('!','@','$','%','#','^','&','*','(',')','?')

numOfChars = int(input('How many characters in password: '))
password = ''

for x in range(numOfChars):
    rand1 = random.randint(1,4)
    if rand1 == 1:
        password += random.choice(lowerCaseLetters)
    if rand1 == 2:
        password += random.choice(upperCaseLetters)
    if rand1 == 3:
        password += random.choice(numbers)
    if rand1 == 4:
        password += random.choice(specialChars)

print('Password is : ' + password)
        



