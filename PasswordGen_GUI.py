import PySimpleGUI as sg, random

def passwordGen(numOfChars, bool_1, bool_2, bool_3, bool_4):
    lowerCaseLetters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    upperCaseLetters = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    numbers = ('1','2','3','4','5','6','7','8','9','0')
    specialChars = ('!','@','$','%','#','^','&','*','(',')','?')

    password = ''

    #Bad solution - can technically run forever
    while len(password) != int(numOfChars):
        rand1 = random.randint(1,4)
        if rand1 == 1 and bool_1 == True:
            password += random.choice(lowerCaseLetters)
        elif rand1 == 2 and bool_2 == True:
            password += random.choice(upperCaseLetters)
        elif rand1 == 3 and bool_3 == True:
            password += random.choice(numbers)
        elif rand1 == 4 and bool_4 == True:
            password += random.choice(specialChars)
    return password

# Define the window's contents
layout = [[sg.Text("How many characters in password?: ")],
          [sg.Input(size=(2,1),key='reply')],
          [sg.Text("Select your options ")],
          [sg.Checkbox('Lowercase Letters', default=False, key='lower')],
          [sg.Checkbox('Uppercase Letters', default=False, key='upper')],
          [sg.Checkbox('Numbers', default=False, key='nums')],
          [sg.Checkbox('Special Characters', default=False, key='specChars')],
            [sg.Button('Ok'), sg.Button('Quit')],
          [sg.Text(size=(40,1), key='-OUTPUT-')]
          ]

# Create the window
window = sg.Window('Password Generator', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    
    password = passwordGen(
                values['reply'], 
                values['lower'], 
                values['upper'], 
                values['nums'], 
                values['specChars']
                )
    # Output a message to the window
    window['-OUTPUT-'].update('Your password is '+password)

# Finish up by removing from the screen
window.close()

