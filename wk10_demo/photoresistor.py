# =============================================================================
# photoresistor.py  -  the FAKE photoresistor ENGINE (the HAL uses this for you)
#
# You do NOT use this file directly. The HAL calls it, so in your program you
# just talk to the hardware layer like everything else:
#
#     hw.play("SOS")          # make the fake sensor "see" a message (test only)
#     value = hw.read_u16()   # read the light level, like any ADC pin
#
# TWO MODES (pick one with the switch below):
#
#   STEP_MODE = False  ->  REAL TIME. The signal follows the wall clock, exactly
#                          like real hardware. Great for the real experience, but
#                          you CANNOT single-step it in a debugger - the clock
#                          keeps moving while you are paused, so the signal races
#                          ahead of your code.
#
#   STEP_MODE = True   ->  ONE SAMPLE PER READ. The signal advances only when
#                          read_u16() is called, so it WAITS for you. Set a
#                          breakpoint, step line by line, watch the values - the
#                          signal moves one sample each read, perfectly in sync.
#                          (The sleep in your loop no longer sets the rate here,
#                          so this mode is for debugging the LOGIC, not for
#                          teaching the sampling rate.)
#
# read_u16() works the same in both modes, so main.py and your receiver never
# change.
# =============================================================================

STEP_MODE = False     # False = real time; True = one sample per read (debuggable)

import time
import morse_code
# In STEP_MODE, each read advances the signal by morse_code.SAMPLE_MS - the SAME
# sampling period main uses - so a dot is the same number of reads in both modes.

# A millisecond clock that works on both the PC and MicroPython (Pico / Wokwi).
try:
    _ticks = time.ticks_ms            # MicroPython
    _diff = time.ticks_diff
except AttributeError:
    def _ticks():                     # the PC
        return int(time.monotonic() * 1000)
    def _diff(a, b):
        return a - b

LOW = 100      # the reading when the light is off (dark)
HIGH = 900     # the reading when the light is on  (lit)

# the one fake sensor's state
_signal = []
_total = 0
_start = 0        # when play() was called (REAL-TIME mode)
_virtual = 0      # how far we have stepped into the message (STEP mode)


def build_signal(message):
    # Turn the message into a list of (is_on, how_many_ms) pieces. The gaps go
    # BETWEEN the parts, each already at its correct length.
    signal = []
    words = message.split(" ")
    for w in range(len(words)):
        if w > 0:
            signal.append((False, morse_code.WORD_GAP_MS))        # gap between words
        patterns = morse_code.encode_message(words[w])
        for p in range(len(patterns)):
            if p > 0:
                signal.append((False, morse_code.LETTER_GAP_MS))    # gap between letters
            pattern = patterns[p]
            for s in range(len(pattern)):
                if s > 0:
                    signal.append((False, morse_code.SYMBOL_GAP_MS))  # gap between symbols
                if pattern[s] == ".":
                    signal.append((True, morse_code.DOT_MS))        # dot is on 1 unit
                else:
                    signal.append((True, morse_code.DASH_MS))       # dash is on 3 units
    return signal


def play(message):
    # Load a message and start "playing" it, starting from the beginning.
    global _signal, _total, _start, _virtual
    _signal = build_signal(message)
    _total = 0
    for piece in _signal:
        _total = _total + piece[1]
    _start = _ticks()     # for real-time mode
    _virtual = 0          # for step mode


def read():
    # How far into the message are we RIGHT NOW?
    if STEP_MODE:
        elapsed = _advance()                 # moves only when we read (debuggable)
    else:
        elapsed = _diff(_ticks(), _start)    # follows the wall clock (real time)
    return _value_at(elapsed)


def _advance():
    # STEP mode: hand back the current spot, then step forward one sample.
    global _virtual
    here = _virtual
    _virtual = _virtual + morse_code.SAMPLE_MS
    return here


def _value_at(elapsed):
    # Find which piece of the signal 'elapsed' ms lands in, and return its light.
    if elapsed >= _total:
        return LOW                           # message finished (or none): dark
    total = 0
    for piece in _signal:
        total = total + piece[1]             # end time of this piece
        if elapsed < total:                  # we are inside this piece
            if piece[0]:
                return HIGH
            else:
                return LOW
    return LOW
