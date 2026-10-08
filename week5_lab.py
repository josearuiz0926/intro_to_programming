# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 5 Lab: Dictionaries
# Chapter 6 — Python Crash Course, 3rd Edition
#
# Standalone script. Still no functions, still no imports.
# New tool this week: DICTIONARIES. For four weeks you've looked letters up
# by scanning a list with .index(). A dictionary replaces all of that with
# a direct, one-step lookup — and a second dictionary will let you decode.
# =============================================================================

# --- Carried forward: the codebook as (letter, pattern) tuples ---------------
CODEBOOK = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
]


# =============================================================================
# SECTION 1 — ANCHOR
# =============================================================================
print("=" * 52)
print("SECTION 1: ANCHOR — The Encode Map")
print("=" * 52)

# A dictionary stores key -> value pairs. Here the KEY is a letter and the
# VALUE is its pattern. We build it from CODEBOOK with a dict comprehension.
ENCODE_MAP = {letter: pattern for (letter, pattern) in CODEBOOK}

print(f"\nENCODE_MAP has {len(ENCODE_MAP)} entries.")
print(f"Looking up 'S': {ENCODE_MAP['S']}     (one step — no scanning!)")
print(f"Looking up 'O': {ENCODE_MAP['O']}")

# -- Safe lookup with .get() -----------------------------------------------
# ENCODE_MAP['@'] would CRASH with a KeyError. .get() returns a default
# instead, which is perfect for "unknown character -> '?'".
print(f"Looking up '@': {ENCODE_MAP.get('@', '?')}   (.get returns '?' for unknowns)")

# -- ANCHOR QUESTIONS ------------------------------------------------------
# Q1. Last week a lookup for 'Z' scanned 26 entries. How many entries does
#     ENCODE_MAP['Z'] check? Why doesn't dictionary size slow it down?
# just the one entry. unlike list lookups, which may require scanning multiple entries. it uses a hash table internally so it just goes straight to the correct entry rather than checking each thing in a list till it hits the desired 'value'
# Q2. What is the difference between ENCODE_MAP['@'] and
#     ENCODE_MAP.get('@', '?') ? When would each be the right choice?
#  ENCODE_MAP['@'] would raise a KeyError because '@' is not a key in the dictionary.
#  ENCODE_MAP.get('@', '?') would return '?' instead of raising an error, which is useful for handling unknown characters instead of crashing.

# Q3. Why can a dictionary NEVER have the parallel-list bug from Week 2,
#     where a letter and its pattern drift out of alignment?
# Because each key in a dictionary is unique and directly maps to its value.
# There is no separate list of keys and values that can get out of sync. the association
# is maintained internally by the dictionary itself.


# =============================================================================
# SECTION 2 — GUIDED
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 2: GUIDED — The Decode Map and a Round Trip")
print("=" * 52)

# To DECODE we need the mirror dictionary: pattern -> letter.
# TODO Step 1: build DECODE_MAP by flipping ENCODE_MAP. Use a dict
#              comprehension over ENCODE_MAP.items():
#                  {pattern: letter for letter, pattern in ENCODE_MAP.items()}
DECODE_MAP = {pattern: letter for letter, pattern in ENCODE_MAP.items()}    # TODO: replace {} with the comprehension above

print(f"\nDECODE_MAP has {len(DECODE_MAP)} entries.")

# -- Encode a message using the dictionary ---------------------------------
message  = "SOS"
encoded  = []
for character in message.upper():
    if character == ' ':
        encoded.append(' ')
    else:
        encoded.append(ENCODE_MAP.get(character, '?'))
print(f"\nEncoded '{message}' -> {encoded}")

# -- Decode it back using the mirror dictionary ----------------------------
# TODO Step 2: loop over 'encoded'. For each pattern, if it is ' ' append a
#              space ' ' to 'decoded_chars'; otherwise use DECODE_MAP.get()
#              with a default of '?' and append the letter.
decoded_chars = []
# (write your loop here)
for pattern in encoded:
    if pattern ==' ':
        decoded_chars.append(' ')
    else:
        decoded_chars.append(DECODE_MAP.get(pattern, '?'))

decoded = "".join(decoded_chars)
print(f"Decoded back   -> '{decoded}'")
# Expected once complete: 'SOS'


# =============================================================================
# SECTION 3 — EXTENSION
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION — Round-Trip Check on a Phrase")
print("=" * 52)

# A good translator should satisfy: decode(encode(text)) == text
# (ignoring case). Worked helper data: a phrase with two words.
phrase = "HI MOM"

encoded_phrase = []
for character in phrase.upper():
    if character == ' ':
        encoded_phrase.append(' ')
    else:
        encoded_phrase.append(ENCODE_MAP.get(character, '?'))
print(f"\nEncoded '{phrase}' -> {encoded_phrase}")

# -- YOUR EXTENSION --------------------------------------------------------
# Decode 'encoded_phrase' back into text (remember: ' ' -> ' '). Then print
# whether the round trip matched the original uppercased phrase.
# Hint: build the decoded string, then compare it to phrase.upper().

# TODO: decode encoded_phrase and report whether the round trip matched
decoded_phrase_chars = []
for pattern in encoded_phrase:
    if pattern == ' ':
        decoded_phrase_chars.append(' ')
    else:
        decoded_phrase_chars.append(DECODE_MAP.get(pattern, '?'))
decoded_phrase = "".join(decoded_phrase_chars)
print(f"Decoded back   -> '{decoded_phrase}'")
print(f"Round trip matched: {decoded_phrase == phrase.upper()}")


# =============================================================================
# SECTION 4 — STRETCH
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 4: STRETCH — Add the Digits, and Audit the Maps")
print("=" * 52)

# 1. Add the ten digits 0-9 to the project. Their patterns are:
#       0 -----   1 .----   2 ..---   3 ...--   4 ....-
#       5 .....   6 -....   7 --...   8 ---..   9 ----.
#    Extend CODEBOOK (or build a digits dict) and rebuild ENCODE_MAP and
#    DECODE_MAP so numbers encode and decode too. Test with "SOS 911".
#
# 2. Audit: confirm len(ENCODE_MAP) == len(DECODE_MAP). If they differ, two
#    different letters share a pattern — which would be a real bug. Explain
#    why flipping a dictionary can silently lose entries.

# TODO: implement the stretch challenge here


# =============================================================================
# CHECKLIST
#   [ ] ANCHOR:    ran the encode map; answered Q1-Q3
#   [ ] GUIDED:    DECODE_MAP built; 'SOS' round-trips back to 'SOS'
#   [ ] EXTENSION: 'HI MOM' round-trips and reports a match
#   [ ] STRETCH:   (optional) digits added; map sizes audited
#   [ ] I can explain why dict lookup beats scanning a list
#
# LOOKING AHEAD — Week 6
#   Next week: INPUT and WHILE LOOPS. You'll turn this into an interactive
#   translator — type a message, get Morse back, repeat until you quit —
#   and start measuring received pulse durations to decode real signals.
# =============================================================================
