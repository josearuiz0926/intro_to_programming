# =============================================================================
# morse_code.py  -  the codebook + encode + decode, all in one place
# =============================================================================

# --- Morse timing, in milliseconds -------------------------------------------
# The DOT is the base unit. Everything else is a multiple of it (ITU ratios).
# 200 ms makes the LED slow enough to READ BY EYE on Wokwi. Once your logic
# works, lower DOT_MS to send faster.
DOT_MS        = 200
DASH_MS       = DOT_MS * 3     # a dash is 3 dots
SYMBOL_GAP_MS = DOT_MS * 1     # gap between symbols INSIDE one letter
LETTER_GAP_MS = DOT_MS * 3     # gap between letters
WORD_GAP_MS   = DOT_MS * 7     # gap between words

# -----------------------------------------------------------------------------
# 1. THE CODEBOOK  -  the data (the same codebook you built in Weeks 3-5)
#
# CODEBOOK is a list of (letter, pattern) pairs. From it we build two
# dictionaries: one to go letter -> pattern (to encode), and one to go
# pattern -> letter (to decode).
# -----------------------------------------------------------------------------
CODEBOOK = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
    ('0', '-----'),('1', '.----'),('2', '..---'),('3', '...--'),('4', '....-'),
    ('5', '.....'),('6', '-....'),('7', '--...'),('8', '---..'),('9', '----.'),
]

# Build the two lookup dictionaries with simple loops.
ENCODE_MAP = {}
for letter, pattern in CODEBOOK:
    ENCODE_MAP[letter] = pattern      # 'A' -> '.-'

DECODE_MAP = {}
for letter, pattern in CODEBOOK:
    DECODE_MAP[pattern] = letter      # '.-' -> 'A'


# -----------------------------------------------------------------------------
# 2. ENCODE  -  text  ->  list of Morse patterns
#
#   encode_message("SOS")  ->  ['...', '---', '...']
# -----------------------------------------------------------------------------
def encode_message(message):
    """Turn a message string into a list of Morse patterns."""
    patterns = []
    for character in message.upper():
        if character == ' ':
            patterns.append(' ')              # a space between words
        elif character in ENCODE_MAP:
            patterns.append(ENCODE_MAP[character])
        else:
            patterns.append('?')              # a character we don't know
    return patterns


# -----------------------------------------------------------------------------
# 3. DECODE  -  list of Morse patterns  ->  text
#
#   decode_message(['...', '---', '...'])  ->  'SOS'
# -----------------------------------------------------------------------------
def decode_pattern(pattern):
    """Turn ONE Morse pattern into its character (or '?' if we don't know it)."""
    if pattern in DECODE_MAP:
        return DECODE_MAP[pattern]
    else:
        return '?'


def decode_message(patterns):
    """Turn a list of Morse patterns back into text."""
    text = ""
    for pattern in patterns:
        if pattern == ' ':
            text = text + " "             # a space between words
        else:
            text = text + decode_pattern(pattern)
    return text
