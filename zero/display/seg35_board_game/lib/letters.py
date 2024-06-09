from pins_init import cathode_pins, anode_pins, bmi
import time
import random
from ulab import numpy as np
from letters_map import LETTERS


def display_patternSleep(pattern, sleep):
    # First, turn off all rows and columns
    for pin in cathode_pins:
        pin.value = True
    for pin in anode_pins:
        pin.value = False

    # Then, light up leds according to the pattern
    for row in range(len(pattern)):
        for col in range(len(pattern[row])):
            if pattern[row][col] == 1:
                cathode_pins[row].value = False
                anode_pins[col].value = True
                time.sleep(sleep)  # add small delay to avoid all dots lighting up
                cathode_pins[row].value = True
                anode_pins[col].value = False

def display_pattern(pattern):
    display_patternSleep(pattern, 0.005)

def display_sequence(word, delay):
    sequence = [LETTERS[c] + [['0']] * 3 for c in word]
    sequence = [elem for sublist in sequence for elem in sublist]
    display = [['0'] * 7] * 7
    for _ in range(len(sequence) + 7):
        display_pattern(display)
        time.sleep(delay)
        display = display[1:] + [sequence.pop(0)] if sequence else [['0'] * 7]


def get_all_characters():
    return "".join(sorted(LETTERS.keys()))

def get_random_letter():
    return random.choice(list(LETTERS.values()))

def get_all_character_objects():
    return [LETTERS[char] for char in sorted(LETTERS.keys())]
