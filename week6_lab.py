# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 6 Lab: User Input and while Loops
# Chapter 7 — Python Crash Course, 3rd Edition
#
# Standalone script — the LAST week before "The Great Refactor."
# Still no functions and no imports. New tools: input() and while loops.
# This week your translator becomes INTERACTIVE, and you start turning
# measured signal durations back into dots, dashes, and gaps.
#
# NOTE: this file asks for keyboard input, so RUN it (F5) and type at the
# prompts. Type 'quit' to leave the loop.
# =============================================================================

# --- Carried forward: build both lookup dictionaries from the codebook -------
CODEBOOK = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
]
ENCODE_MAP = {letter: pattern for (letter, pattern) in CODEBOOK}
# Reverse map for decoding: pattern -> letter (both maps are given to you).
DECODE_MAP = {pattern: letter for (letter, pattern) in CODEBOOK}

DOT_MS = 100   # base unit, carried forward (boundaries are multiples of it)


# =============================================================================
# SECTION 1 — ANCHOR
# =============================================================================
print("=" * 52)
print("SECTION 1: ANCHOR — An Interactive Encoder")
print("=" * 52)
print("Type a message to encode. Type 'quit' to stop.\n")

# A while loop repeats as long as its condition stays True. We use a
# 'sentinel' value ('quit') to decide when to stop. (Week 7: this whole
# loop body becomes a clean function call.)
while True:
    text = input("Message> ")
    if text.lower() == 'quit':
        print("Goodbye!")
        break                      # leave the while loop

    encoded = []
    for character in text.upper():
        if character == ' ':
            encoded.append(' ')
        else:
            encoded.append(ENCODE_MAP.get(character, '?'))
    print(f"  Morse: {' '.join(encoded)}\n")

# -- ANCHOR QUESTIONS ------------------------------------------------------
# Q1. What is the 'sentinel' value here, and what would happen if we forgot
#     the break? The sentinel is 'quit'. If we forgot the break, it would
#     create an infinite loop. (Careful — that's an infinite loop. Use Ctrl+C to escape.)
# Q2. Why do we check text.lower() == 'quit' instead of text == 'quit'?
#    Because the user might type 'Quit', 'QUIT', or any other case variation. Using lower() ensures that we catch all variations of the word 'quit'.
# Q3. input() always returns a string. Why does that matter the moment you ask the user for a NUMBER (see the GUIDED section)?
#  it matters because if we want to perform numerical operations or comparisons, 
# we need to convert the string input into an integer using int(). If we don't convert it, we might encounter errors or unexpected behavior 
# when trying to use the input as a number.


# =============================================================================
# SECTION 2 — GUIDED
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 2: GUIDED — Classify Received Signal Durations")
print("=" * 52)

# The RECEIVER measures how long the light was ON or OFF, in milliseconds,
# and must decide what each measurement means. The boundaries are multiples
# of DOT_MS:
#     ON  pulse:   shorter than DOT_MS*2 (200ms) = dot,  otherwise dash
#     OFF gap:     shorter than DOT_MS*2 = symbol gap (within a letter)
#                  shorter than DOT_MS*5 (500ms) = letter gap
#                  DOT_MS*5 or longer = word gap
#
# (Week 7: these become classify_pulse() and classify_gap().)

pulse_durations = [55, 105, 180, 240, 300]   # measured ON times (ms)
gap_durations   = [90, 150, 320, 480, 700]   # measured OFF times (ms)

print("\nPulse (LED ON) classification:")
for duration in pulse_durations:
    # TODO: if duration < DOT_MS * 2 -> 'dot', else -> 'dash'. Print it.
    kind = ""    # TODO: use an if/else to set kind
    if duration < DOT_MS * 2:
        kind = 'dot'
    else: 
        kind = 'dash'
    print(f"  {duration:4}ms -> {kind}")

print("\nGap (LED OFF) classification:")
for duration in gap_durations:
    # TODO: use if / elif / else with the two boundaries above to set 'kind'
    #       to 'symbol_gap', 'letter_gap', or 'word_gap'. Print it.
    kind = ""    # TODO
    if duration < DOT_MS * 2:
        kind = 'symbol_gap'
    elif duration < DOT_MS * 5:
        kind = 'letter_gap'
    else:
        kind = 'word_gap'

    print(f"  {duration:4}ms -> {kind}")


# =============================================================================
# SECTION 3 — EXTENSION
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION — An Encode / Decode Menu")
print("=" * 52)

# Build a small menu that loops until the user chooses to quit:
#     1) Encode text  -> Morse   (type a message, get dots and dashes)
#     2) Decode Morse -> text    (type space-separated Morse, get the message)
#     3) Quit
#
# Use a while loop with input() and an if/elif/else on the menu choice.
# Re-show the menu after each action.
#
#   ENCODE: upper-case the text, then loop each character. Look it up with
#           ENCODE_MAP.get(char, '?'); use '/' for a space. Join with spaces.
#   DECODE: split the typed Morse on spaces into tokens, then loop them. Look
#           each token up with DECODE_MAP.get(token, '?'); turn '/' back into
#           a space. Join the letters together.
#   (Both ENCODE_MAP and DECODE_MAP are built for you at the top of the file.)
#
# Copying the encode loop from the ANCHOR again is a hint about why functions
# exist — that's next week.

# TODO: implement the menu loop here
#   while True:
#       print the three options
#       choice = input("Choose 1-3> ")
#       if choice == '1':      # encode text -> Morse
#           ...
#       elif choice == '2':    # decode Morse -> text
#           ...
#       elif choice == '3':
#           break
#       else:
#           print an "invalid choice" message
while True:
    print("\nMenu:")
    print("1) Encode text -> Morse")
    print("2) Decode Morse -> text")
    print("3) Quit")
    
    choice = input("Choose 1-3> ")
    
    if choice == '1':
        text = input("Enter text to encode: ")
        encoded = []
        for character in text.upper():
            if character == ' ':
                encoded.append('/')
            else:
                encoded.append(ENCODE_MAP.get(character, '?'))
        print(f"Encoded Morse: {' '.join(encoded)}")
        
    elif choice == '2':
        morse = input("Enter Morse code to decode (use '/' for spaces): ")
        tokens = morse.split()
        decoded = []
        for token in tokens:
            if token == '/':
                decoded.append(' ')
            else:
                decoded.append(DECODE_MAP.get(token, '?'))
        print(f"Decoded text: {''.join(decoded)}")
        
    elif choice == '3':
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

# =============================================================================
# SECTION 4 — STRETCH
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 4: STRETCH — Robust Numeric Input")
print("=" * 52)

# Ask the user "How many times should I repeat the message?" and keep
# asking until they enter a valid whole number greater than 0.
#   - input() returns a string; you'll need int() to convert it.
#   - A bad entry like "five" will CRASH int() with a ValueError. Instead of
#     pre-screening the text, wrap the conversion in a try / except block:
#     try to int() it, and if it raises ValueError, print a message and let
#     the loop ask again. Only break once you have a whole number > 0.
#   - Once you have a valid count, encode a fixed message and print its
#     Morse that many times.
#
# Reflect in a comment: this is a "validation loop." Why is catching the error
# with try / except safer than trusting the first thing the user types?
#
# Hint (the shape, not the answer): wrap the risky int() in try, break only
# after you've confirmed the value is > 0, and handle the except ValueError.

# TODO: implement the validation loop here


# =============================================================================
# CHECKLIST
#   [ ] ANCHOR:    typed messages; 'quit' exits cleanly; answered Q1-Q3
#   [ ] GUIDED:    pulses classify as dot/dash; gaps as symbol/letter/word
#   [ ] EXTENSION: menu ENCODES and DECODES; Quit exits the loop
#   [ ] STRETCH:   (optional) numeric input is validated before use
#   [ ] I noticed how many times I copy-pasted the encoding loop
#
# LOOKING AHEAD — Week 7: THE GREAT REFACTOR
#   You now have a WORKING translator — but the same encoding loop is
#   copy-pasted in several places, and everything lives in one giant file.
#   Next week you learn FUNCTIONS. You'll wrap each piece of logic in a
#   function, split the project into MODULES (separate .py files), and meet
#   the hardware layer that finally turns "[LED]" print lines into a real
#   blinking LED you can run on a Pi Pico. Keep ALL your week 1-6 files.
# =============================================================================
