import PySimpleGUI as sg
import random

from PySimpleGUI.PySimpleGUI import theme_text_color


def clueGenerator(number):
    clue = 'The number... \n'
    for x in range(2, 10):
        if number % x == 0:
            clue = clue + 'is divisible by ' + str(x)+'\n'
    return clue


'''

while(guess != number):
    if(guess > number):
        print('Lower')
        guess = int(input('Enter guess: '))
    else: 
        print('higher')
        guess = int(input('Enter guess: '))
    attempts += 1
    

print('You guessed '+ str(number) + ' correctly in ' +str(attempts)+ ' attempt(s)!\n')
'''


# Define the window's contents
layout = [[sg.Button('Generate Number')],
          [sg.Text("Clues for the number")],
          [sg.Text(size=(40, 10), key='-OUTPUT-')],
          [sg.Text("Enter Guess: ")],
          [sg.Input(size=(3, 1), key='-Guess-'), sg.Button('Try Guess')],
          [sg.Text(size=(50, 1), key='-PROMPT-')],
          [sg.Button('Quit')]
          ]

# Create the window
window = sg.Window('Number guessing game', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'Generate Number':
        number = random.randint(1, 10)
        attempts = 0
        window['-OUTPUT-'].update(str(clueGenerator(number)))
    if event == 'Try Guess':
        guess = int(values['-Guess-'])
        attempts += 1
        if guess > number:
            window['-PROMPT-'].update('Lower')
        elif guess < number:
            window['-PROMPT-'].update('Higher')
        else:
            #window['-PROMPT-'].update(f"You guessed {values['-Guess-']} correctly in {attempts} attempt(s)", text_color='green')
            sg.popup(f"You guessed {values['-Guess-']} correctly in {attempts} attempt(s)", text_color='pink')
# Finish up by removing from the screen
window.close()
