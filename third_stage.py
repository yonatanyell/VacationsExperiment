import random
import time


def main_experiment(window, to_be_primed_tuple, inferior_not_primed_tuple, locations_tuples, timeout):
    primed_cnt = 0
    total_number_primed = 0
    chosen_primed = []

    inferior_cnt = 0
    total_number_not_primed = 0
    chosen_not_primed = []

    for i in range(len(locations_tuples)):
        current_locations = locations_tuples[i]
        random.shuffle(current_locations)
        window["location1"].update(visible=True, value=current_locations[0], text_color='black')
        window["location2"].update(visible=True, value=current_locations[1], text_color='black')
        window["location1_key"].update(visible=True, value="To choose the left location, press the key: 'a'")
        window["location2_key"].update(visible=True, value="To choose the right location, press the key: 'k'")
        window["main_text"].update(visible=False)
        window.refresh()
        window["location1"].update(visible=True, value=current_locations[0], text_color='black')
        window["location2"].update(visible=True, value=current_locations[1], text_color='black')
        window["location1_key"].update(visible=True, value="To choose the left location, press the key: 'a'")
        window["location2_key"].update(visible=True, value="To choose the right location, press the key: 'k'")
        window["main_text"].update(visible=False)
        window.refresh()
        event, values = window.read(timeout=timeout)
        if event == 'a':
            if current_locations[0] in to_be_primed_tuple or current_locations[1] in to_be_primed_tuple:
                chosen_primed.append(current_locations[0])
                total_number_primed += 1
                if current_locations[0] in to_be_primed_tuple:
                    primed_cnt += 1
            else:
                chosen_not_primed.append(current_locations[0])
                total_number_not_primed += 1
                if current_locations[0] in inferior_not_primed_tuple:
                    inferior_cnt += 1

            window["location2"].update(visible=False)
            window["location2_key"].update(visible=False)
            window["location1"].update(visible=True, text_color='blue')
            window["location1_key"].update(visible=True, value='Was successfully selected')
            window.refresh()
            window["location2"].update(visible=False)
            window["location2_key"].update(visible=False)
            window["location1"].update(visible=True, text_color='blue')
            window["location1_key"].update(visible=True, value='Was successfully selected')
            window.refresh()
            time.sleep(2)
        elif event == 'k':
            if current_locations[0] in to_be_primed_tuple or current_locations[1] in to_be_primed_tuple:
                chosen_primed.append(current_locations[1])
                total_number_primed += 1
                if current_locations[1] in to_be_primed_tuple:
                    primed_cnt += 1
            else:
                chosen_not_primed.append(current_locations[1])
                total_number_not_primed += 1
                if current_locations[1] in inferior_not_primed_tuple:
                    inferior_cnt += 1

            window["location1"].update(visible=False)
            window["location1_key"].update(visible=False)
            window["location2"].update(visible=True, text_color='blue')
            window["location2_key"].update(visible=True, value='Was successfully selected')
            window.refresh()
            window["location1"].update(visible=False)
            window["location1_key"].update(visible=False)
            window["location2"].update(visible=True, text_color='blue')
            window["location2_key"].update(visible=True, value='Was successfully selected')
            window.refresh()
            time.sleep(2)
        elif event == '__TIMEOUT__':
            window["location1"].update(visible=False)
            window["location2"].update(visible=False)
            window["location1_key"].update(visible=False)
            window["location2_key"].update(visible=False)
            window["main_text"].update(value="Time's out! Please try to answer faster", visible=True)
            window.refresh()
            window["location1"].update(visible=False)
            window["location2"].update(visible=False)
            window["location1_key"].update(visible=False)
            window["location2_key"].update(visible=False)
            window["main_text"].update(value="Time's out! Please try to answer faster", visible=True)
            window.refresh()
            time.sleep(4)
    window["location1"].update(visible=False)
    window["location1_key"].update(visible=False)
    window["location2"].update(visible=False)
    window["location2_key"].update(visible=False)
    window.refresh()
    return primed_cnt, total_number_primed, chosen_primed, inferior_cnt, total_number_not_primed, chosen_not_primed
