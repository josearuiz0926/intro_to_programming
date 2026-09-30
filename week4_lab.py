# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 4 Lab: if Statements
# Chapter 5 — Python Crash Course, 3rd Edition
#
# Standalone script. Still no functions, still no imports.
# New tool this week: if / elif / else. This is what lets us make
# DECISIONS — handle spaces, lowercase input, unknown characters, and
# decide what the "LED" should do for each symbol.
#
# (The LED is still just a printed line this week. Real hardware and a
#  swappable hardware module arrive in Week 7.)
# =============================================================================

# --- Carried forward from earlier weeks --------------------------------------
DOT_MS        = 100
DASH_MS       = DOT_MS * 3
SYMBOL_GAP_MS = DOT_MS * 1
LETTER_GAP_MS = DOT_MS * 3
WORD_GAP_MS   = DOT_MS * 7

CODEBOOK = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
]
letters  = [pair[0] for pair in CODEBOOK]
patterns = [pair[1] for pair in CODEBOOK]


# =============================================================================
# SECTION 1 — ANCHOR
# =============================================================================
print("=" * 52)
print("SECTION 1: ANCHOR — Classifying a Symbol with if/elif/else")
print("=" * 52)

# A received Morse element is one of four kinds. An if/elif/else chain
# checks each possibility in order and stops at the first match.
# (This decision logic becomes the function classify_symbol() in Week 7.)

test_symbols = ['.', '-', ' ', '*']
print("\nClassifying symbols:")
for symbol in test_symbols:
    if symbol == '.':
        kind = 'dot'
    elif symbol == '-':
        kind = 'dash'
    elif symbol == ' ':
        kind = 'word_gap'
    else:
        kind = 'unknown'
    print(f"  '{symbol}' -> {kind}")

# -- ANCHOR QUESTIONS ------------------------------------------------------
# Q1. The chain checks '.', then '-', then ' ', then else. What happens if
#     a symbol matches the FIRST branch — do the others still get checked?-No
#
# Q2. Why do we need the final 'else' (unknown)? What real input might land
#     there, and why is silently ignoring it safer than crashing?- the final else catches anything that isnt a dot, dash,
# or space. A typo or digit. the program shoudlnt crash over one bad character. itll just label it as unknown

# Q3. Could you rewrite this with three separate 'if' statements instead of
#     elif? Would the result be the same? Which is clearer?
# with three seperat if statements the result is the same but only if you leave off the else. every if gets checked eve after a match. elif is clearer because the branches are mutually exclusive and it says so.


# =============================================================================
# SECTION 2 — GUIDED
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 2: GUIDED — Encode a Message (with the messy cases)")
print("=" * 52)

# Last week we could only encode clean, all-known, space-free words.
# Now 'if' lets us handle reality: lowercase letters, spaces between
# words, and characters that aren't in the codebook.

message = "Hi Mom"     # mixed case AND a space — last week this would crash

# TODO Step 1: normalize the message to uppercase so 'h' matches 'H'.
message = message.upper()      # TODO: replace with message.upper()

encoded = []
# TODO Step 2: loop over each character. Inside the loop, use if/elif/else:
#   - if the character is a space ' ':  append ' ' to encoded (a word gap)
#   - elif the character is in 'letters' (use the 'in' test):
#         look it up with letters.index() and append its pattern
#   - else:  it's unknown — append '?'
# Hint:
#   for character in message:
#       if character == ' ':
#           encoded.append(' ')
#       elif character in letters:
#           encoded.append(patterns[letters.index(character)])
#       else:
#           encoded.append('?')

# (write your loop here)
for character in message:
      if character == ' ':
          encoded.append(' ')
      elif character in letters:
          encoded.append(patterns[letters.index(character)])
      else:
          encoded.append('?')


print(f"\nEncoding '{message}':")
print(f"  result -> {encoded}")
# Expected once complete: ['....', '..', ' ', '--', '---', '--']


# =============================================================================
# SECTION 3 — EXTENSION
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION — Decide What the LED Does")
print("=" * 52)

# To "transmit" a pattern we walk through its dots and dashes and decide,
# for each one, how long the LED is ON. This is the heart of the
# transmitter — and it's all if/elif. (Week 7: this becomes transmit_pattern().)
#
# Worked example for the letter 'A' ('.-'):
print("\nTransmitting 'A' ( .- ):")
for symbol in '.-':
    if symbol == '.':
        print(f"  [LED] ON {DOT_MS}ms (dot), then OFF {SYMBOL_GAP_MS}ms")
    elif symbol == '-':
        print(f"  [LED] ON {DASH_MS}ms (dash), then OFF {SYMBOL_GAP_MS}ms")
print(f"  [LED] OFF {LETTER_GAP_MS}ms (letter gap)")

# -- YOUR EXTENSION --------------------------------------------------------
# Do the same for the letter 'S' ('...'). Loop over its pattern, and for
# each symbol print the matching LED action with the correct timing.
# End with the letter-gap line.

# TODO: transmit the pattern for 'S'
print("\nTransmitting 'S' ( ... ):")
for symbol in '...':
    if symbol == '.':
        print(f"  [LED] ON {DOT_MS}ms (dot), then OFF {SYMBOL_GAP_MS}ms")
    elif symbol == '-':
        print(f"  [LED] ON {DASH_MS}ms (dash), then OFF {SYMBOL_GAP_MS}ms")
print(f"  [LED] OFF {LETTER_GAP_MS}ms (letter gap)")


# =============================================================================
# SECTION 4 — STRETCH
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 4: STRETCH — A Grade-Style Boundary Check")
print("=" * 52)

# A receiver measures how long a pulse stayed ON (in ms) and must decide:
# was it a dot or a dash? The boundary is the midpoint, DOT_MS * 2 = 200ms.
#
#   1. For each measured duration in this list, use if/else to print
#      'dot' or 'dash':
#         measurements = [60, 110, 200, 260, 95, 305]
#      Rule: shorter than 200ms -> dot, otherwise -> dash.
#   2. The value exactly AT the boundary (200) is the tricky one. Decide
#      which way it should go and justify it in a comment. (This exact
#      boundary question returns in Week 6.)
#   3. Bonus: also flag any measurement that is suspiciously far from a
#      clean dot (100) or dash (300) as 'noisy?'.

# TODO: implement the stretch challenge here


# =============================================================================
# CHECKLIST
#   [ ] ANCHOR:    ran the classifier; answered Q1-Q3
#   [ ] GUIDED:    'Hi Mom' -> ['....', '..', ' ', '--', '---', '--']
#   [ ] EXTENSION: 'S' transmits as three dots + a letter gap
#   [ ] STRETCH:   (optional) dot/dash boundary decisions
#   [ ] I can explain why the first matching branch wins
#
# LOOKING AHEAD — Week 5
#   Next week: DICTIONARIES. Every letters.index() lookup you've written
#   gets replaced by an instant dictionary lookup, and you'll build a
#   reverse dictionary that decodes patterns straight back to letters.
# =============================================================================
