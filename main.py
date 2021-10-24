import random
import time

import PySimpleGUI as sg

import my_stroop
import third_stage
import json


#### First Window

col0_0 = sg.Column([[sg.Text('Please enter participant number', font=("Helvitica 20 bold"), justification='center', size=(1000, 1))],
                      [sg.Input(justification='center', font= ("Ariel", 20), size=(20,10), key='in')],
                      [sg.Button('Take me to the experiment!', size=(30,1))]], element_justification='center')

layout_zeroWindow = [[col0_0]]
zeroWindow = sg.Window('Participant Page', layout_zeroWindow, resizable=True, size=(1000, 500))
closed = 0
while True:
    event, values = zeroWindow.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        closed = 1
        break
    if event == 'Take me to the experiment!':
        break
zeroWindow.close()

participant_number = values['in']
print(int(participant_number))


########## first stage ##########

# locations = ["Paris (France)", 'London (England)', 'Rome (Italy)', 'Budapest (Hungary)', 'Los Angeles (USA)',
#              'New York (USA)', 'Miami (USA)', 'Tel Aviv', 'Jerusalem', 'Thailand', 'Japan', 'Buenos Aires (Argentina)',
#              'Vienna (Austria)', 'Brussels (Belgium)', 'Rio de Janeiro (Brazil)', 'Mexico', 'Costa Rica', 'Panama',
#              'Sofia (Bulgaria)', 'Toronto (Canada)', 'China', 'Zagreb (Croatia)', 'Cuba', 'Cyprus', 'Greece',
#              'Copenhagen (Denmark)', 'Fiji Islands', 'Georgia', 'Berlin (Germany)', 'Iceland', 'Indonesia',
#              'South Africa', 'Madagascar', 'Maldives', 'Morocco', 'Amsterdam (Netherlands)', 'New Zealand',
#              'Australia', 'Philippines', 'Lisbon (Portugal)', 'Moscow (Russia)', 'Bucharest (Romania)',
#              'Belgrade (Serbia)', 'Turkey', 'Abu Dhabi (United Arab Emirates)', 'Warsaw (Poland)', 'Seychelles',
#              'Madrid (Spain)', 'Barcelona (Spain)', 'Switzerland', 'Cambodia', 'Milano (Italy)', 'Venice (Italy)',
#              'Las Vegas (USA)', 'San Diego (USA)', 'San Fransisco (USA)', 'Vietnam', 'India', 'Monte Carlo',
#              'Kyiv (Ukraine)']

locations = ["Paris", 'London', 'Rome', 'Budapest', 'Los Angeles',
             'New York', 'Miami', 'Tel Aviv', 'Jerusalem', 'Thailand', 'Japan', 'Buenos Aires',
             'Vienna', 'Brussels', 'Rio de Janeiro', 'Mexico', 'Costa Rica', 'Grand Canyon',
             'Sofia', 'Toronto', 'China', 'Zagreb', 'Cuba', 'Cyprus', 'Greece',
             'Niagara Falls', 'Fiji Islands', 'Georgia', 'Berlin', 'Iceland', 'Indonesia',
             'South Africa', 'Madagascar', 'Maldives', 'Morocco', 'Amsterdam', 'New Zealand',
             'Australia', 'Philippines', 'Lisbon', 'Moscow', 'Bucharest',
             'Belgrade', 'Turkey', 'Dubai', 'Warsaw', 'Seychelles',
             'Madrid', 'Barcelona', 'Switzerland', 'Zanzibar', 'Milano', 'Venice',
             'Las Vegas', 'San Diego', 'San Francisco', 'Vancouver', 'India', 'Monte Carlo',
             'Kyiv']

## 60 locations

# locations = ['Paris', 'Madrid', 'Barcelona', 'Switzerland', 'Rio de Janeiro']
#
# locations = ["Paris", 'London', 'Rome', 'Budapest', 'Los Angeles',
#              'New York', 'Miami', 'Tel Aviv', 'Jerusalem', 'Thailand', 'Japan', 'Buenos Aires',
#              'Vienna', 'Brussels', 'Rio de Janeiro', 'Mexico', 'Costa Rica', 'Panama',
#              'Sofia', 'Toronto', 'China', 'Zagreb', 'Cuba', 'Cyprus', 'Greece']

col1_0 = sg.Column([[sg.Text('You will be shown several Locations for a vacation you are planning to have.', font="Ariel 18", justification='center', size=(1000, 1), pad=((0,0), (300,0)))],
                    [sg.Text('Each location has its ideal conditions!',
                     font=("Ariel 18 bold underline"), justification='center')],
                    [sg.Text('Please rate your level of interest in a vacation taking place in each location, on a continuous scale between "not insterested at all" to "very insterested!".', pad=((0,0), (30,0)),
                             font="Ariel 18 bold", justification='center')],
                    [sg.Text(
                        'Please try to use all of the scale!',
                        font="Ariel 18 bold underline", justification='center', pad=((0, 0), (0, 30)))],
                      [sg.Button("Got it! I'm ready to start!", font='Ariel 20', size=(30, 1))]],
                   element_justification='center')

if closed != 1:
    layout_firstWindow = [[col1_0]]
    firstWindow = sg.Window('First Page', layout_firstWindow, resizable=True, size=(1000, 1000)).finalize()
    firstWindow.maximize()
    while True:
        event, values = firstWindow.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            closed = 1
            break
        if event == "Got it! I'm ready to start!":
            break

    firstWindow.close()

locations_shuffled = random.sample(locations, len(locations))
locations_result = {}

col_location = sg.Column([[sg.Text(locations_shuffled[0], font='Ariel 50 bold', key='location', auto_size_text=True, justification='center', size=(30,1))],
                          [sg.Button("Submit", font= 'Ariel 20', key='Submit', size=(10,1))]
                          ], element_justification='center', vertical_alignment='c')
col_slider = sg.Column([[sg.Text("Very Interested!", font='Ariel 30 bold', key='very', auto_size_text=True, justification='center', size=(30,1))],
                        [sg.Slider((1, 100), disable_number_display=True, default_value=50, orientation='v', key='slider', enable_events=True, size=(48,50))],
                        [sg.Text("Not Interested At All!", font='Ariel 30 bold', key='not', auto_size_text=True, justification='center', size=(30,1))]], element_justification='center')
layout_exp = [[col_location, col_slider]]
i_window = sg.Window("Locations", layout_exp, resizable=True).finalize()
i_window.maximize()

if closed != 1:
    i = 0
    while i < len(locations_shuffled):
        window, event, values = sg.read_all_windows()
        if event in (sg.WIN_CLOSED, 'Exit'):
            closed = 1
            break
        if event == 'Submit':
            locations_result[values['slider']] = locations_shuffled[i]

            if i != len(locations_shuffled) - 1:
                i_window['location'].update(value=locations_shuffled[i+1])
                i_window['slider'].update(value=50)
            i += 1
    i_window.close()

print(locations_result)
sorted_values = sorted(locations_result.keys(), reverse=True)
print(sorted_values)
sorted_locations = [locations_result[sorted_values[i]] for i in range(len(sorted_values))]

i = 1
inferiors = []
while i < len(sorted_values):
    inferiors.append(sorted_locations[i])
    i += 2
inferior_to_be_primed = random.sample(inferiors, round(2*len(inferiors)/3))
inferior_to_be_primed_tuple = tuple(inferior_to_be_primed)
inferior_not_primed = [x for x in inferiors if x not in inferior_to_be_primed_tuple]
inferior_not_primed_tuple = tuple(inferior_not_primed)

print("sorted: " + str(sorted_locations))
print("to_be_primed: " + str(inferior_to_be_primed))
print("not primed: " + str(inferior_not_primed))

########## second stage - stroop ##########

col1_0 = sg.Column([[sg.Text('In this stage, you will be presented with words in different colors.', font="Ariel 18", justification='center', size=(1000, 1), pad=((0,0), (300,0)), background_color='white', text_color='black')],
                    [sg.Text('Each color is represented by a designated key, and your goal is to press the key that '
                             'corresponds to the color of the presented word as quick as possible.',
                             font="Ariel 18 ", justification='center', background_color='white', text_color='black')],
                    [sg.Text('Red',
                             font="Ariel 18", justification='center', text_color='red', background_color='white'),
                     sg.Text("= the key '1' ", font= "Ariel 18", background_color='white', text_color='black')],
                    [sg.Text('Green',
                             font="Ariel 18", justification='center', text_color='green', background_color='white'),
                     sg.Text("= the key '2' ", font="Ariel 18", background_color='white', text_color='black')],
                    [sg.Text('Blue',
                             font="Ariel 18", justification='center', text_color='blue', background_color='white'),
                     sg.Text("= the key '3' ", font="Ariel 18", background_color='white', text_color='black')],
                    [sg.Text("Let's try some examples", pad=((0,0), (50,0)),
                             font = "Ariel 18 bold", justification='center', background_color='white', text_color='black')],
                      [sg.Button("Sure!", font= 'Ariel 20', size=(30,1))]],
                   element_justification='center', background_color='white')

if closed != 1:
    layout_firstWindow = [[col1_0]]
    firstWindow = sg.Window('First Page', layout_firstWindow, resizable=True, size=(1000, 1000), background_color='white').finalize()
    firstWindow.maximize()
    while True:
        event, values = firstWindow.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            closed = 1
            break
        if event == "Sure!":
            break

    firstWindow.close()

training_examples = ['This', 'is', 'so', 'much', 'fun', 'I', 'want', 'to', 'do', 'it', 'every', 'day!']
my_stroop.run_stroop_training(training_examples)

real_words = ['Hello', 'World', 'Math', 'Calculate', 'Window', 'Chair', 'Table', 'Flight', 'Plane', 'Piano', 'Pillow', 'Remote',
         'Dog', 'Silk', 'Cat', 'Closet', 'Pants', 'Board', 'Bottle', 'Wallet', 'Phone', 'Car', 'Bench', 'Kitchen', 'Python',
         'Screen', 'Movie', 'Picture', 'Wall', 'Clock', 'Desk', 'Notes', 'Calendar', 'Computer', 'Pencil', 'Student',
         'Mirror', 'Inside', 'Friend', 'Mask', 'Mail', 'Find', 'Podcast', 'Seven', 'Eleven', 'Strength', 'Learn', 'Begin', 'Trust', 'Young',
              'Ten', 'Bold', 'Paper', 'Shirt', 'Orange', 'Pen', 'Program', 'Erase', 'Guitar', 'Within']

# real_words = ['hello', 'world', 'This', 'is', 'so', 'much', 'fun', 'I', 'want', 'to', 'do', 'it', 'every', 'day!']

# 60 words
# to_be_primed = 20 (half of 60 locations = 30, 10 not primed)
# total number of 80 words in stroop

real_words += inferior_to_be_primed
random.shuffle(real_words)
print(real_words)
my_stroop.run_stroop_real(real_words) # 1000 milliseconds (1 second)


########## Third stage ##########

col_3_0 = sg.Column([[sg.Text('In this stage, you will be shown pairs of locations for a possible vacation you are planning to have.', font="Ariel 18", justification='center', size=(1000, 1), pad=((0,0), (300,0)), background_color='white', text_color='black', key='instructions', visible=True)],
                    [sg.Text('You will need to choose which location out of the two you prefer most, when each location has the exact same ideal conditions!',
                     font=("Ariel 18 "), justification='center', background_color='white', text_color='black', key='conditions', visible=True)],
                     [sg.Text(
                         "Location 1",
                         font=("Ariel 50 bold"), justification='center', background_color='white', text_color='black',
                         pad=((0, 30), (10, 0)), visible=False, key='location1'),
                     ],
                    [sg.Text("To choose the left location, press the key: 'A'",
                             font="Ariel 18 bold", justification='left', text_color='black', background_color='white', pad=((0, 10), (20, 0)), visible=False, key='a'),
                     sg.Text("To choose the right location, press the key: 'k'",
                             font="Ariel 18 bold", justification='right', text_color='black', background_color='white', visible=False, key='k'),
                     ],
                      [sg.Button("Let's see an example!", font= 'Ariel 20', size=(30,1))]],
                   element_justification='center', background_color='white', key='button')

layout_third_stage = [[col_3_0]]
third_stage_window = sg.Window('Third Stage', layout_third_stage, resizable=True, size=(1000, 1000),
                        background_color='white').finalize()
third_stage_window.maximize()
i = 0
while True:
    event, values = third_stage_window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        closed = 1
        break
    if event == "Let's see an example!":
        break

third_stage_window.close()

col_3_1_1 = sg.Column([[sg.Text("Location 1",  size=(14, 1), justification='center', background_color='white', text_color='black',
                                key='location1', font="Ariel 70 bold", pad=((0, 0), (200, 0)))],
                       [sg.Text("To choose the left location, press the key: 'a'",
                                font="Ariel 18 bold", justification='center', text_color='black',
                                background_color='white', key='location1_key')]], element_justification='center',
                      background_color='white')
col_3_1_2 = sg.Column([[sg.Text("", font= 'Ariel 20', size=(30, 5), key="main_text", background_color='white', justification='center', pad=((0, 0), (200, 0)))],
                       [sg.Button("Got it! Let's start", font='Ariel 20', key="button", pad=((100, 0), (300, 0)))]],
                      background_color='white')
col_3_1_3 = sg.Column([[sg.Text("Location 2", justification='center', size=(14, 1), font="Ariel 70 bold", background_color='white',
                                text_color='black', key='location2', pad=((0, 0), (200, 0)))],
                       [sg.Text("To choose the right location, press the key: 'k'",
                                font="Ariel 18 bold", justification='center', text_color='black',
                                background_color='white', key='location2_key')]], element_justification='center',
                      background_color='white')
third_stage_main_window_layout = [[col_3_1_1, col_3_1_2, col_3_1_3]]
third_stage_main_window = sg.Window('Third Stage', third_stage_main_window_layout, resizable=True, size=(1000, 1000),
                                    background_color='white', element_justification='center', return_keyboard_events=True).finalize()

third_stage_main_window.maximize()
i = 0

while True:
    event, values = third_stage_main_window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        third_stage_main_window.close()
    elif event == "a":
        third_stage_main_window["location2"].update(visible=False)
        third_stage_main_window["location2_key"].update(visible=False)
        third_stage_main_window["location1"].update(visible=True, text_color='blue')
        third_stage_main_window["location1_key"].update(visible=True, value='Was successfully selected')
        third_stage_main_window.refresh()
        third_stage_main_window.refresh()
        third_stage_main_window["location2"].update(visible=False)
        third_stage_main_window["location2_key"].update(visible=False)
        third_stage_main_window["location1"].update(visible=True, text_color='blue')
        third_stage_main_window["location1_key"].update(visible=True, value='Was successfully selected')
        third_stage_main_window.refresh()
        third_stage_main_window.refresh()
        time.sleep(2)
        third_stage_main_window["location2"].update(visible=True)
        third_stage_main_window["location2_key"].update(visible=True)
        third_stage_main_window["location1"].update(visible=True, text_color='black')
        third_stage_main_window["location1_key"].update(visible=True, value="To choose the left location, press the key: 'a'")
        third_stage_main_window.refresh()
        third_stage_main_window.refresh()
        third_stage_main_window["location2"].update(visible=True)
        third_stage_main_window["location2_key"].update(visible=True)
        third_stage_main_window["location1"].update(visible=True, text_color='black')
        third_stage_main_window["location1_key"].update(visible=True, value="To choose the left location, press the key: 'a'")
        third_stage_main_window.refresh()
        third_stage_main_window.refresh()
    elif event == "k":
        third_stage_main_window["location1"].update(visible=False)
        third_stage_main_window["location1_key"].update(visible=False)
        third_stage_main_window["location2"].update(visible=True, text_color='blue')
        third_stage_main_window["location2_key"].update(visible=True, value='Was successfully selected')
        third_stage_main_window.refresh()
        third_stage_main_window.refresh()
        third_stage_main_window["location1"].update(visible=False)
        third_stage_main_window["location1_key"].update(visible=False)
        third_stage_main_window["location2"].update(visible=True, text_color='blue')
        third_stage_main_window["location2_key"].update(visible=True, value='Was successfully selected')
        third_stage_main_window.refresh()
        third_stage_main_window.refresh()
        time.sleep(2)
        third_stage_main_window["location1"].update(visible=True)
        third_stage_main_window["location1_key"].update(visible=True)
        third_stage_main_window["location2"].update(visible=True, text_color='black')
        third_stage_main_window["location2_key"].update(visible=True, value="To choose the right location, press the key: 'k'")
        third_stage_main_window.refresh()
        third_stage_main_window.refresh()
        third_stage_main_window["location1"].update(visible=True)
        third_stage_main_window["location1_key"].update(visible=True)
        third_stage_main_window["location2"].update(visible=True, text_color='black')
        third_stage_main_window["location2_key"].update(visible=True, value="To choose the right location, press the key: 'k'")
        third_stage_main_window.refresh()
        third_stage_main_window.refresh()
    elif event == "button":
        third_stage_main_window["location1"].update(visible=False)
        third_stage_main_window["location2"].update(visible=False)
        third_stage_main_window["location1_key"].update(visible=False)
        third_stage_main_window["location2_key"].update(visible=False)
        third_stage_main_window["button"].update(visible=False)
        third_stage_main_window.refresh()
        third_stage_main_window.refresh()
        break

sorted_locations_tuples = [[sorted_locations[i-1], sorted_locations[i]] for i in range(1, len(sorted_locations), 2)]
random.shuffle(sorted_locations_tuples)

locations_primed = [x for x in sorted_locations_tuples if x[0] in inferior_to_be_primed_tuple or x[1] in inferior_to_be_primed_tuple]
locations_not_primed = [x for x in sorted_locations_tuples if x[0] in inferior_not_primed_tuple or x[1] in inferior_not_primed_tuple]

if int(participant_number) % 2 == 0:
    third_stage_main_window["main_text"].update(visible=True, value="For the next pairs of locations, "
                                                                    "you will have 10 seconds to answer.",
                                                text_color='black', font='Ariel 20')
    third_stage_main_window.refresh()
    time.sleep(10)

    third_stage_main_window["main_text"].update(visible=True, value="Please be ready with your fingers "
                                                                    "placed on the relevant keys! "
                                                                    "('a' for the left option, "
                                                                    "'k' for the right option.",
                                                text_color='black', font='Ariel 20')
    third_stage_main_window.refresh()
    time.sleep(10)

    primed_cnt_ten, total_number_primed_ten, chosen_primed_ten, inferior_cnt_ten, total_number_not_primed_ten, \
    chosen_not_primed_ten = third_stage.main_experiment(third_stage_main_window, inferior_to_be_primed_tuple,
                                                        inferior_not_primed_tuple, sorted_locations_tuples,
                                                        timeout=10000)


else:
    third_stage_main_window["main_text"].update(visible=True, value="For the next pairs of locations, "
                                                                    "you will have only 2 seconds to answer.",
                                                text_color='black', font='Ariel 20')
    third_stage_main_window.refresh()
    time.sleep(15)

    third_stage_main_window["main_text"].update(visible=True, value="Please be ready with your fingers "
                                                                    "placed on the relevant keys! "
                                                                    "('a' for the left option, "
                                                                    "'k' for the right option).",
                                                text_color='black', font='Ariel 20')
    third_stage_main_window.refresh()
    time.sleep(20)

    third_stage_main_window["main_text"].update(visible=True, value="Starting automatically in 3 seconds",
                                                text_color='black', font='Ariel 20')
    third_stage_main_window.refresh()
    time.sleep(1)
    third_stage_main_window["main_text"].update(visible=True, value="Starting automatically in 2 seconds",
                                                text_color='black', font='Ariel 20')
    third_stage_main_window.refresh()
    time.sleep(1)
    third_stage_main_window["main_text"].update(visible=True, value="Starting automatically in 1 seconds",
                                                text_color='black', font='Ariel 20')
    third_stage_main_window.refresh()
    time.sleep(1)

    primed_cnt_one, total_number_primed_one, chosen_primed_one, inferior_cnt_one, total_number_not_primed_one, \
    chosen_not_primed_one = third_stage.main_experiment(third_stage_main_window, inferior_to_be_primed_tuple,
                                                        inferior_not_primed_tuple, sorted_locations_tuples,
                                                        timeout=2000)


f = open("participant_" + str(participant_number) + ".txt", "w+")
f.write(json.dumps(locations_result))
f.write('\n')
f.write("Sorted Locations: " + str(sorted_locations))
f.write('\n')
f.write("Primed: " + str(inferior_to_be_primed))
f.write('\n')
f.write("Inferior Not Primed: " + str(inferior_not_primed))
f.write('\n')
f.write("Pairs: " + str(sorted_locations_tuples))
f.write('\n')
f.write("Pairs of primed: " + str(locations_primed))
f.write('\n')
f.write("Pairs of not primed: " + str(locations_not_primed))
f.write('\n')
f.write('\n')
if int(participant_number) % 2 == 0:
    f.write("Ten Seconds:")
    f.write('\n')
    f.write("Primed: chose " + str(primed_cnt_ten) + " inferiors out of total number: " + str(total_number_primed_ten))
    f.write('\n')
    f.write("Primed locations chosen: " + str(chosen_primed_ten))
    f.write('\n')
    f.write("Not Primed: chose " + str(inferior_cnt_ten) + " inferiors out of total number: " + str(
        total_number_not_primed_ten))
    f.write('\n')
    f.write("Not Primed locations chosen: " + str(chosen_not_primed_ten))
    f.write('\n')
    f.write('\n')
else:
    f.write("One Second:")
    f.write('\n')
    f.write("Primed: chose " + str(primed_cnt_one) + " inferiors out of total number: " + str(total_number_primed_one))
    f.write('\n')
    f.write("Primed locations chosen: " + str(chosen_primed_one))
    f.write('\n')
    f.write("Not Primed: chose " + str(inferior_cnt_one) + " inferiors out of total number: " + str(
        total_number_not_primed_one))
    f.write('\n')
    f.write("Not Primed locations chosen: " + str(chosen_not_primed_one))

f.close()

### thank you stage

col_end = sg.Column([[sg.Text('Thank you for participating!', font="Ariel 40", justification='center', background_color='white', text_color='black',size=(1000, 1), pad=((0,0), (300,0)))],
                      [sg.Button("End the experiment", font= 'Ariel 20', size=(30,1))]], element_justification='center', background_color='white')

thank_you_window_layout = [[col_end]]
thank_you_window = sg.Window('Third Stage', thank_you_window_layout, resizable=True, size=(1000, 1000),
                                    background_color='white', element_justification='center', return_keyboard_events=True).finalize()
thank_you_window.maximize()
event, values = thank_you_window.read()
if event == 'End the experiment':
    thank_you_window.close()