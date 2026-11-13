# =============================================================================
# main.py  -  STARTER for this week's lab: a Morse SEND / RECEIVE station
#
# What is given to you:
#   - the exception that picks the hardware layer (hal_pico on a Pico / Wokwi,
#     hal_pc on your PC)
#   - a short DEMO that shows how to use the photoresistor
#   - the station loop that asks "send or receive?" each round
#
# What YOU write (this is the lab):
#   - send_message(message)   week 9 you wrote how to send a word, now (week 10)extend to a whole message (add word gaps)
#   - receive()               week 10, read the photoresistor and decode the message
#
# =============================================================================

# NEW in WEEK 10 - replace the hal_pico import and hal_pc imports with this try/except. 
# It will pick the right one for you, and you can run the same code on a Pico or on your PC.
try:
    import hal_pico as hw
except ImportError:
    import hal_pc as hw

import morse_code


# =============================================================================
# DEMO - how to use the photoresistor  (run it once, then delete this part)
# =============================================================================
# You read the photoresistor through the HAL, just like the LED: hw.read_u16()
# gives a NUMBER - about 900 when the light is on, about 100 when it is off.
# (For this demo, hw.play(...) makes the fake sensor "see" a message; with a
# real sensor the light comes from a real sender instead.) It changes its value
# every 1 ms on its own, in the BACKGROUND.
#
# Notice we only READ it every 100 ms here, even though it is changing every
# 1 ms. How often YOU read it is your SAMPLING RATE - and that decides how many
# reads make a dot. Turning the numbers into dots and letters is your job.
print("DEMO: reading the photoresistor while it plays the letter 'E'")
hw.play("E")                            # make the fake sensor "see" the letter E
count = 0
while count < 10:
    value = hw.read_u16()               # <-- this is how you read the sensor
    print("   read_u16() =", value)
    hw.sleep_ms(100)                    # our sampling rate for this demo
    count = count + 1
print("DEMO done.")
print("")


# =============================================================================
# WEEK9 Lab - you sent a word
# WEEK10 Lab - extend to send a whole message
# =============================================================================
def send_message(message):
    patterns = morse_code.encode_message(message)  # CHANGED: added the morse_code. prefix (was NameError)
    # CHANGED: loop by index (was "for pattern in patterns") so we can look at the
    # NEXT pattern to decide whether a letter gap is needed.
    for i in range(len(patterns)):
        pattern = patterns[i]
        if pattern == " ":
            # CHANGED: a word gap is 7 units TOTAL, sent as one off period.
            # (Was WORD_GAP_MS - LETTER_GAP_MS = 4 units.)
            hw.set_led_timed(False, morse_code.WORD_GAP_MS)  # gap between words
        elif pattern == "?":
            print("(unrecognized character, skipping)")
        else:
            for s in range(len(pattern)):
                # CHANGED: symbol gap goes BETWEEN symbols only (was after every
                # symbol, which stacked an extra gap onto the end of each letter).
                if s > 0:
                    hw.set_led_timed(False, morse_code.SYMBOL_GAP_MS)   # gap between symbols
                if pattern[s] == '.':
                    hw.set_led_timed(True, morse_code.DOT_MS)           # dot
                elif pattern[s] == '-':
                    hw.set_led_timed(True, morse_code.DASH_MS)          # dash
            # CHANGED: NEW letter gap (3 units). Only when another letter follows;
            # a space or the end of the message supplies its own gap.
            if i + 1 < len(patterns) and patterns[i + 1] != " ":
                hw.set_led_timed(False, morse_code.LETTER_GAP_MS)       # gap between letters
    # CHANGED: removed the trailing word-gap and the "(send_message to be completed)" print.
    hw.set_led(False)   # make sure the LED ends OFF

# =============================================================================
# WEEK10 Lab - read the photo resistor and decode the message
# NEW: everything in this section is new code (the old TODO stub was replaced).
# =============================================================================

# --- NEW: receive settings (tune these) ---------------------------------------
RX_THRESHOLD         = 500   # reading ABOVE this = light ON (fake sensor swings 100/900).
                             # A REAL ADC gives 0..65535: print some raw values with the
                             # light on and off, and put this halfway between them.
RX_ON_IS_HIGH        = True  # set False if your sensor reads LOWER when the light is ON
DEBOUNCE_SAMPLES     = 2     # a change must last this many reads in a row to count
                             # (2 reads = 10 ms, far shorter than a 200 ms dot)
END_OF_MESSAGE_UNITS = 10    # this many dark units in a row = message is over (> 7)
START_TIMEOUT_MS     = 10000 # give up if no light is ever seen in this time
UNKNOWN_TEXT         = "[unknown character]"  # shown where a pattern is not in the codebook


def light_is_on(value):
    # NEW: one raw reading -> True (light ON) / False (light OFF) using the threshold.
    if RX_ON_IS_HIGH:
        return value > RX_THRESHOLD
    return value < RX_THRESHOLD


def decode_morse_string(morse):
    # NEW: Morse string -> text. Letters are separated by one space, words by " / ".
    #   "... --- ..."          -> "SOS"
    #   ".... .. / - .... ..." -> "HI THE"
    # Uses the EXISTING codebook (morse_code.DECODE_MAP / decode_pattern):
    # no second lookup table is created.
    text = ""
    words = morse.split(" / ")
    for w in range(len(words)):
        if w > 0:
            text = text + " "                          # space between words
        for pattern in words[w].split(" "):
            if pattern == "":
                continue
            if pattern in morse_code.DECODE_MAP:       # known? let the codebook decode it
                text = text + morse_code.decode_pattern(pattern)
            else:
                text = text + UNKNOWN_TEXT             # unknown: mark it, keep decoding
    return text


def receive():
    # NEW: read the light through the HAL, time each ON / OFF run, classify it,
    # build a Morse string, then decode it. Timing comes from morse_code.py
    # (base unit = DOT_MS). Cut-offs sit halfway between the ideal lengths:
    #   ON  run:  < 2 units = dot (1)          >= 2 units = dash (3)
    #   OFF run:  < 2 units = symbol gap (1)   2..5 units = letter gap (3)
    #             >= 5 units = word gap (7)
    unit_ms    = morse_code.DOT_MS
    sample_ms  = morse_code.SAMPLE_MS
    dash_cut   = 2 * unit_ms       # ON run shorter than this = dot
    letter_cut = 2 * unit_ms       # OFF run at least this long = letter gap
    word_cut   = 5 * unit_ms       # OFF run at least this long = word gap
    end_ms     = END_OF_MESSAGE_UNITS * unit_ms

    morse      = ""        # the Morse string being built ("... --- ...")
    letter     = ""        # dots/dashes of the letter in progress
    state      = False     # the ACCEPTED light state (starts dark)
    run        = 0         # how many reads the accepted state has lasted
    pending    = 0         # reads in a row that disagree with 'state' (debounce)
    seen_light = False     # has the message started yet?
    started    = hw.now_ms()

    while True:
        raw_on = light_is_on(hw.read_u16())      # read the sensor THROUGH the HAL

        if raw_on == state:
            # Same as before. A short disagreeing blip was noise, so those
            # reads are folded back into this run.
            run = run + pending + 1
            pending = 0
        else:
            pending = pending + 1
            if pending >= DEBOUNCE_SAMPLES:
                # A real transition: close the run that just ended.
                run_ms = run * sample_ms
                if state:
                    # An ON run ended: dot or dash.
                    if run_ms < dash_cut:
                        letter = letter + "."
                    else:
                        letter = letter + "-"
                elif seen_light:
                    # An OFF run ended (ignore the dark before the message starts).
                    if run_ms >= word_cut:
                        if letter != "":
                            morse = morse + letter + " / "   # end of letter AND word
                            letter = ""
                    elif run_ms >= letter_cut:
                        if letter != "":
                            morse = morse + letter + " "     # end of letter
                            letter = ""
                    # else: symbol gap = same letter, nothing to do

                state = raw_on
                run = pending            # the debounce reads belong to the new run
                pending = 0
                if state:
                    seen_light = True

        # Stop conditions
        if seen_light and (not state) and run * sample_ms >= end_ms:
            break                                   # long dark = message finished
        if (not seen_light) and hw.elapsed_ms(started) > START_TIMEOUT_MS:
            return ""                               # nothing ever arrived

        hw.sleep_ms(sample_ms)                      # steady sampling rate

    morse = morse + letter                          # close the last letter
    print("  morse heard:", morse)
    return decode_morse_string(morse)


# =============================================================================
# THE MORSE CODE STATION  (given - this is how your two functions get used)
# =============================================================================
print("Board:", hw.board_info())
print("Morse station. Choose a mode each round.")

while True:
    mode = input("\n[s]end or [r]eceive? (blank to quit) ")
    mode = mode.strip().lower()
    if mode == "":
        break

    if mode == "s" or mode == "send":
        message = input("  message to SEND: ")
        message = message.strip().upper()
        if message != "":
            send_message(message)             # <-- your function flashes the LED

    elif mode == "r" or mode == "receive":
        message = input("  message being sent to you: ")
        message = message.strip().upper()
        if message != "":
            hw.play(message)                  # fake sensor: make it "see" this message
            decoded = receive()               # <-- your function reads + decodes
            print("  you received:", decoded)

    else:
        print("  please type s or r")

print("done.")
