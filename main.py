import random

import PySimpleGUI as sg

#### First Window

col1 = sg.Column([[sg.Text('Please enter participant number', font=("Ariel bold", 20), justification='center', size=(1000,1))],
                      [sg.Input(justification='center', font= ("Ariel", 20), size=(20,10), key='in')],
                      [sg.Button('Take me to the experiment!', size=(30,1))]], element_justification='center')

layout_firstWindow = [[col1]]
firstWindow = sg.Window('First Page', layout_firstWindow, resizable=True, size=(1000,500))
while True:
    event, values = firstWindow.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Take me to the experiment!':
        break
firstWindow.close()

participant_number = values['in']

######### start of the experiment

number_of_trials = 100
features = ['Location', 'Cleanliness', 'Value for money', 'Comfort']
hotels = ["hotel1", "hotel2", "hotel3"]
ratings = {1: '1.png', 1.5: '1.5.png', 2: '2.png', 2.5: '2.5.png', 3:'3.png', 3.5: '3.5.png', 4: '4.png',
           4.5: '4.5.png', 5: '5.png'}
combinations = [[[4,5], [3,4]], [[5,4.5], [2,4]]]

feature_1, feature_2 = None, None
while feature_1 == feature_2:
    feature_1, feature_2 = features[random.randint(0, len(features) - 1)], features[
        random.randint(0, len(features) - 1)]

current_ratings = combinations[random.randint(0, len(combinations) - 1)]
image_1_1 = ratings[current_ratings[0][0]]
image_1_2 = ratings[current_ratings[0][1]]
image_2_1 = ratings[current_ratings[1][0]]
image_2_2 = ratings[current_ratings[1][1]]

current_hotel_1, current_hotel_2 = None, None
while current_hotel_1 == current_hotel_2:
    current_hotel_1, current_hotel_2 = hotels[random.randint(0, len(hotels) - 1)], hotels[
        random.randint(0, len(hotels) - 1)]

col1 = sg.Column([[sg.Text(current_hotel_1, font=("Ariel bold", 20), text_color='black', background_color='white', justification='center', key='hotel1')],
                  [
                   sg.Image(image_1_1, background_color='white', key='rating_1.1')],
                  [
                   sg.Image(image_1_2, background_color='white', key='rating_1.2')],
                  [sg.Button('Choose this hotel', font=("Ariel", 15), size=(27,1), key='first')]], element_justification='left', background_color='white')

col2 = sg.Column([[sg.Text(current_hotel_2, font=("Ariel bold", 20), text_color='black', background_color='white', justification='center', key='hotel2')],
                  [sg.Text(feature_1, font=("Ariel", 15), text_color='black', background_color='white', justification='left', size=(15,1), pad=((50,0),(0,0)), key='feature_1'),
                   sg.Image(image_2_1, background_color='white', key='rating_2.1')],
                  [sg.Text(feature_2, font=("Ariel", 15), text_color='black', background_color='white', justification='left', size=(15,1), pad=((50,0),(0,0)), key='feature_2'),
                   sg.Image(image_2_2, key='rating_2.2', background_color='white')],
                  [sg.Button('Choose this hotel', font=("Ariel", 15), size=(27,1), key='second')]], element_justification='right', background_color='white')

i=1
data = []
exp_window = sg.Window('Exp', [[col1, col2]], resizable=True, background_color='white')
while i<number_of_trials+1:
    event, values = exp_window.read()
    if event == 'first':
        print('first')
    elif event == 'second':
        print('second')
    elif event in (sg.WIN_CLOSED, 'Exit'):
        break

    feature_1, feature_2 = None, None
    while feature_1 == feature_2:
        feature_1, feature_2 = features[random.randint(0, len(features)-1)], features[random.randint(0, len(features)-1)]

    current_ratings = combinations[random.randint(0, len(combinations)-1)]
    image_1_1 = ratings[current_ratings[0][0]]
    image_1_2 = ratings[current_ratings[0][1]]
    image_2_1 = ratings[current_ratings[1][0]]
    image_2_2 = ratings[current_ratings[1][1]]

    current_hotel_1, current_hotel_2 = None, None
    while current_hotel_1 == current_hotel_2:
        current_hotel_1, current_hotel_2 = hotels[random.randint(0, len(hotels)-1)], hotels[random.randint(0, len(hotels)-1)]

    exp_window['hotel1'].update(current_hotel_1)
    exp_window['hotel2'].update(current_hotel_2)
    exp_window['rating_1.1'].update(image_1_1)
    exp_window['rating_1.2'].update(image_1_2)
    exp_window['rating_2.1'].update(image_2_1)
    exp_window['rating_2.2'].update(image_2_2)
    exp_window['feature_1'].update(feature_1)
    exp_window['feature_2'].update(feature_2)

    i += 1
exp_window.close()



# exp_window = sg.Window('Exp', [[col1, col2]], resizable=True, background_color='white')
#exp_window.close()

# col1 = [[sg.Text('This is my sample text', font=("Ariel", 20), key='-text-', justification="center", size=(1000,1))], [sg.Image('2.png', pad=(100,20))], [sg.Button('Ok')]]
# col2 = [[sg.Text("Please choose from the following")], [sg.Image('2.png')], [sg.Button('Ok')]]
#
# layout = [[sg.Column(col1)]]
#
# window = sg.Window('Window Title', layout, resizable=True, size=(1000, 500))
#
# event, values = window.read()
#
# print('Hello', values[0], "! Thanks for trying PySimpleGUI")
#
# window.close()
