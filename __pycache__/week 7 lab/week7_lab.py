# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 7 Lab: Functions  —  "THE GREAT REFACTOR"
# Chapter 8 — Python Crash Course, 3rd Edition
#
# This is the turning point of the course. For six weeks you built a WORKING
# translator as one long script. Today you learn FUNCTIONS and MODULES by
# REFACTORING it — reorganizing code you already have, without changing what
# it does.
#
# >>> THE ONE RULE OF REFACTORING <<<
# Make ONE small move, then RUN the program and check the output is EXACTLY
# the same as before. If it changed, undo your last move and try again.
# Never make two moves without running in between. This is how professionals
# safely take a program apart: tiny steps, tested every time.
#
# HOW THIS LAB WORKS
# Below is your translator, with every function written and working — run it
# right now (F5) and note the output. Then follow STEP 1 -> STEP 4. Each step
# tells you EXACTLY which lines to CUT (they're marked) and which NEW FILE to
# paste them into, plus the one import line to add back here. Run after each
# step. When you finish, THIS file will be a short "main" that imports four
# small modules — and the output will be identical to what you see now.
# =============================================================================

# Timing constants (these can stay here for now; they move to config in Week 8)
DOT_MS        = 100
DASH_MS       = DOT_MS * 3
SYMBOL_GAP_MS = DOT_MS * 1
LETTER_GAP_MS = DOT_MS * 3
WORD_GAP_MS   = DOT_MS * 7


# =============================================================================
# STEP 1 (ANCHOR — worked for you):  the DATA  ->  morse_codebook.py
#
#   1. Create a new file in this folder named  morse_codebook.py
#   2. CUT everything between the CUT lines below and PASTE it into that file.
#   3. Back here, DELETE those lines and add this import at the TOP of this file
#      (just under the timing constants):
#          from morse_codebook import CODEBOOK, ENCODE_MAP, DECODE_MAP
#   4. SAVE both files and RUN. The output must be identical. (It will be!)
#
#   You just made your first MODULE — a file of code another file can import.
# =============================================================================
# >>>>>>>>>>>>>>>>>>>>>>>>  CUT INTO morse_codebook.py  >>>>>>>>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<<<<<<<<<<<<<<  END CUT (STEP 1)  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
from ast import pattern

from morse_codebook import CODEBOOK, ENCODE_MAP, DECODE_MAP

# =============================================================================
# STEP 2 (GUIDED — your turn):  ENCODING  ->  morse_encoder.py
#
#   1. Create a new file named  morse_encoder.py
#   2. CUT the encode_message() function below into it.
#   3. encode_message uses ENCODE_MAP, which now lives in morse_codebook.py —
#      so at the TOP of morse_encoder.py add:
#          from morse_codebook import ENCODE_MAP
#   4. Back here, add to your imports at the top of this file:
#          from morse_encoder import encode_message
#   5. SAVE all files and RUN. Same output? Then the move was safe.
#
#   Lesson: a function can live in any file, as long as that file can import
#   the names it needs.
# =============================================================================
# >>>>>>>>>>>>>>>>>>>>>>>>  CUT INTO morse_encoder.py  >>>>>>>>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<<<<<<<<<<<<<<  END CUT (STEP 2)  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
from morse_encoder import encode_message

# =============================================================================
# STEP 3 (EXTENSION — less help):  DECODING  ->  morse_decoder.py
#
#   Same pattern as Step 2, but you work out the import lines yourself.
#   - Create morse_decoder.py and CUT BOTH functions below into it.
#   - What name from morse_codebook do these functions need? Import it at the
#     top of morse_decoder.py.
#   - Add the matching "from morse_decoder import ..." line back here.
#   - RUN and confirm identical output.
#
#   Notice decode_pattern() has a DEFAULT parameter (unknown_char='?') — that
#   is a function feature from this chapter: callers can leave it out.
# =============================================================================
# >>>>>>>>>>>>>>>>>>>>>>>>  CUT INTO morse_decoder.py  >>>>>>>>>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<<<<<<<<<<<<<<  END CUT (STEP 3)  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

from morse_decoder import decode_message


# =============================================================================
# STEP 4 (STRETCH — write a function + meet the HAL)
#
# Look at the transmit code inside the demo block below: it is still INLINE,
# and it still uses print() for the "LED" like Weeks 1-6. Two jobs:
#
#   PART A — WRITE A FUNCTION:
#     Wrap that inline transmit loop in a function:
def transmit_pattern(pattern):
    for symbol in pattern:
        if symbol == '.':
            hw.set_led_timed(True, DOT_MS)
        elif symbol == '-':
            hw.set_led_timed(True, DASH_MS)
            hw.set_led_timed(False, SYMBOL_GAP_MS)
            hw.set_led_timed(False, LETTER_GAP_MS)
#     and call transmit_pattern(encoded[0]) from the demo instead of the loop.
#     RUN — same output.
#
#   PART B — MEET THE HAL (the file hal_stub.py is provided for you):
#     hal_stub.py hides the "LED" behind functions like hw.set_led_timed().
#     Move transmit_pattern() into a real transmitter later, and replace each
#     print("[LED]...") with a HAL call:
        import hal_stub as hw
        hw.set_led_timed(True, DOT_MS)     # LED on for a dot
        hw.set_led_timed(False, SYMBOL_GAP_MS)
#     RUN. The HAL is WHY modules matter: swap hal_stub for a future hal_pico
#     (same function names, real pin code) and this program blinks a real LED
#     on a Pi Pico — changing ONE import line and nothing else.
# =============================================================================


print("=" * 52)
print("Morse Translator — Week 7 refactor")
print("=" * 52)

# encode + decode (these calls do NOT change as you refactor —
# that is the whole point: same behavior, tidier code)
print("\n-- encode / decode --")
for word in ["SOS", "HELLO"]:
    enc = encode_message(word)
    print(f"  {word:6} -> {enc} -> '{decode_message(enc)}'")

# transmit the first letter of SOS — STEP 4 turns this into a function
print("\n-- transmit first letter of SOS --")
first = encode_message("SOS")[0]      # '...'
for symbol in first:                  # <-- STEP 4 PART A: wrap this loop
    if symbol == '.':
        print(f"  [LED] ON {DOT_MS}ms (dot), OFF {SYMBOL_GAP_MS}ms")
    elif symbol == '-':
        print(f"  [LED] ON {DASH_MS}ms (dash), OFF {SYMBOL_GAP_MS}ms")
print(f"  [LED] OFF {LETTER_GAP_MS}ms (letter gap)")


# =============================================================================
# CHECKLIST
#   [ ] Ran the BEFORE version and noted the output
#   [ ] STEP 1: codebook moved to morse_codebook.py; output unchanged
#   [ ] STEP 2: encode_message moved to morse_encoder.py; output unchanged
#   [ ] STEP 3: decode functions moved to morse_decoder.py; output unchanged
#   [ ] STEP 4A: wrote transmit_pattern() as a function
#   [ ] STEP 4B: transmit uses the HAL (hw.set_led_timed)
#   [ ] After every step I RAN the program and the output stayed the same
#   [ ] This file is now a short "main" that imports four modules
#
# WHY THIS MATTERS
#   You didn't add a single feature today — and that's the point. Refactoring
#   makes code easier to read, test, and reuse WITHOUT changing what it does.
#   Tiny tested steps are how you safely improve real software.
#
# LOOKING AHEAD — Week 8
#   Files and exceptions: save settings and a session log to disk, handle
#   errors with try/except, and wire your new modules together in main().
# =============================================================================
