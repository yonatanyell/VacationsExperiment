import random
import collections
import time

import PySimpleGUI as sg

def run_stroop_training(words):
    colors = {'red': '1', 'green': '2', 'blue': '3'}

    col_word = sg.Column([[sg.Text("Let's Start! Press the key as quick as possible",
                                   font="Ariel 80", justification='center', size=(1000, 1), pad=((0, 0), (300, 0)),
                                   background_color='white', text_color='black', key='word', visible=True)],
                          [sg.Button("I'm ready!", font= "Ariel 40", size=(30,1), key='button', visible=False)]], element_justification='center', background_color='white')

    layout_word = [[col_word]]
    word_window = sg.Window('Stroop', layout_word, resizable=True, size=(1000, 1000),
                            background_color='white', return_keyboard_events=True).finalize()
    word_window.maximize()

    i = 0
    time.sleep(4)
    while i < len(words):
        color, key = random.choice(list(colors.items()))
        word_window['word'].update(value=words[i], text_color=color, font="Ariel 100")
        event, values = word_window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == key:
            hold_window(word_window, "Correct!", 100, 1)
            i += 1
        else:
            hold_window(word_window, "Wrong! For the color " + color + " you need to press: '" + key + "'", 80, 4)
            i += 1

    word_window['word'].update(value="Done! Great job!", text_color='black', font="Ariel 80")
    word_window.refresh()
    time.sleep(3)
    word_window['word'].update(value="Let's continue?", text_color='black', font="Ariel 80")
    word_window['button'].update(visible=True)
    word_window.refresh()
    while True:
        event, values = word_window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == "button":
            break
    word_window.close()


def run_stroop_real(words):
    colors = {'red': '1', 'green': '2', 'blue': '3'}

    col_word = sg.Column([[sg.Text("Press the key as quick as possible! You will have limited time for each word!",
                                   font="Ariel 40", justification='center', size=(1000, 1), pad=((0, 0), (300, 0)),
                                   background_color='white', text_color='black', key='word', visible=True)],
                          [sg.Text(
                              'Remember, Each color is represented by a designated key, and your goal is to press the key that corresponds to the color of the presented word.',
                              font=("Ariel 26 "), justification='center', background_color='white',
                              text_color='black', key='remember')],
                          [sg.Text('Red',
                                   font="Ariel 26", justification='center', text_color='red', background_color='white', key='red 1'),
                           sg.Text("= the key '1' ", font="Ariel 26", background_color='white', text_color='black', key='red 2')],
                          [sg.Text('Green',
                                   font="Ariel 26", justification='center', text_color='green',
                                   background_color='white', key='green 1'),
                           sg.Text("= the key '2' ", font="Ariel 26", background_color='white', text_color='black', key='green 2')],
                          [sg.Text('Blue',
                                   font="Ariel 26", justification='center', text_color='blue',
                                   background_color='white', key='blue 1'),
                           sg.Text("= the key '3' ", font="Ariel 26", background_color='white', text_color='black', key='blue 2')],
                          [sg.Button("I'm ready!", font= "Ariel 40", size=(30,1), key='button', visible=True)]], element_justification='center', background_color='white')

    layout_word = [[col_word]]
    word_window = sg.Window('Stroop', layout_word, resizable=True, size=(1000, 1000),
                            background_color='white', return_keyboard_events=True).finalize()
    word_window.maximize()


    event, values = word_window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        word_window.close()
    elif event == 'button':
        word_window['remember'].update(visible=False)
        word_window['red 1'].update(visible=False)
        word_window['red 2'].update(visible=False)
        word_window['green 1'].update(visible=False)
        word_window['green 2'].update(visible=False)
        word_window['blue 1'].update(visible=False)
        word_window['blue 2'].update(visible=False)
        word_window['button'].update(visible=False)

    hold_window(word_window, "+", 100, 1.5)

    i = 0
    while i < len(words):
        color, key = random.choice(list(colors.items()))

        word_window['word'].update(value=words[i], text_color=color, font="Ariel 100")
        event, values = word_window.read(timeout=1000)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == '__TIMEOUT__':
            hold_window(word_window, "Try Faster! ", 100, 3)
            hold_window(word_window, "+", 100, 1.5)

        else:
            hold_window(word_window, "+", 100, 1.5)

        i += 1
    hold_window(word_window, "Done! Great job!", 80, 3)
    word_window['word'].update(value="Let's continue?", text_color='black', font="Ariel 80")
    word_window['button'].update(visible=True)
    word_window.refresh()
    while True:
        event, values = word_window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == "button":
            break
    word_window.close()


def hold_window(window, text, size, hold_time):
    window['word'].update(value=text, text_color='black', font="Ariel " + str(size))
    t = time.time()
    while time.time() - t < hold_time:
        window.refresh()

