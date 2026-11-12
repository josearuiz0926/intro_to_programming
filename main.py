# =============================================================================
# ENGR 1210 - Morse Optical Comms
# =============================================================================
# GOAL
#   Blink a Morse message on an LED - first on your LAPTOP, then, with the SAME
#   file and no changes, on a real Pico 2 in Wokwi. That "it just works on the
#   board too" moment is the whole idea of a HAL (Hardware Abstraction Layer).
#
# =============================================================================

from email import message

import hal_pc as hw
#import hal_pico as hw  # uncomment this line to run on the real Pico 2
from morse_code import WORD_GAP_MS, DOT_MS, DASH_MS, SYMBOL_GAP_MS, LETTER_GAP_MS, encode_message


def blink_pattern(message):
   pattern = encode_message(message)
   for letter in pattern:
         
    # pattern is one letter, like '...'
        for symbol in letter:
            if symbol == '.':
                hw.set_led_timed(True, DOT_MS)               # dot
                hw.set_led_timed(False, SYMBOL_GAP_MS)       # gap after a symbol
            elif symbol == '-':
                hw.set_led_timed(True, DASH_MS)              # dash
                hw.set_led_timed(False, SYMBOL_GAP_MS)       # gap after a symbol
            else:
                hw.set_led_timed(False, LETTER_GAP_MS)         # gap after a symbol
print("...done")

# The SAME loop runs in both worlds. You type a morse pattern; the HAL blinks it.
# On the laptop, "the LED" is the [LED] ON/OFF lines. On the board, it's the
# real onboard LED (type your message in the serial console / Wokwi's Serial
# Monitor). 
print("Board:", hw.board_info())      # tells you which world the HAL picked
print("Type a message and watch it blink. Type 'quit' to stop.")

while True:
    pattern = input("\nMorse pattern to blink (or 'quit'): ").strip()
    if pattern.lower() == "quit":
        break
    if pattern:
        blink_pattern(pattern)
