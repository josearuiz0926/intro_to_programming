# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 2 Lab: Introducing Lists
# Chapter 3 — Python Crash Course, 3rd Edition
#
# Standalone script. No functions, no imports — just lists and indexing.
# (Reminder: in Week 7 this logic becomes functions in separate modules.
#  For now, everything lives in this one file, top to bottom.)
#
# SECTION 1 ANCHOR | SECTION 2 GUIDED | SECTION 3 EXTENSION | SECTION 4 STRETCH
# Rule: you must be able to EXPLAIN every line you submit.
# =============================================================================


# =============================================================================
# SECTION 1 — ANCHOR  (read, run, understand)
# =============================================================================
print("=" * 52)
print("SECTION 1: ANCHOR — Storing the Codebook in Lists")
print("=" * 52)

# The codebook maps each letter to its Morse pattern. This week we don't
# have dictionaries yet (those are Week 5) or loops (Week 3), so we store
# the data in TWO PARALLEL LISTS that line up by position:
#
#     letters[0] is 'A'   and   patterns[0] is '.-'
#     letters[1] is 'B'   and   patterns[1] is '-...'
#
# The lists MUST stay in the same order. Position is the only thing
# connecting a letter to its pattern. (Hold onto that thought — it's
# fragile, and it's exactly why Week 5's dictionary will be a relief.)

letters  = ['A',  'B',    'C',    'D',   'E']
patterns = ['.-', '-...', '-.-.', '-..', '.']
print()
print(f"\nThe codebook currently has {len(letters)} letters.")
print(f"First letter:  {letters[0]}  ->  {patterns[0]}")
print(f"Last letter:   {letters[-1]}  ->  {patterns[-1]}")   # -1 = last item

# -- Looking up a pattern by letter (no loop needed) -----------------------
# .index() finds WHERE a value sits in a list. We use the letter's
# position in 'letters' to grab the matching slot in 'patterns'.
c_position = letters.index('C')        # where is 'C'? -> 2
c_pattern  = patterns[c_position]      # same slot in the other list
print(f"\nLooking up 'C': it is at position {c_position}, pattern is '{c_pattern}'")

# -- Growing the codebook with append() ------------------------------------
letters.append('F')
patterns.append('..-.')
print(f"After adding F: {len(letters)} letters, last is {letters[-1]} -> {patterns[-1]}")

# -- ANCHOR QUESTIONS ------------------------------------------------------
# Q1. Why must 'letters' and 'patterns' stay in exactly the same order?-because if they change and you try to match them up they will be different.
#     What breaks if you append to one list but forget the other?-the corresponding pattern wont just magically appear. you have to insert it as well
# Q2. letters[-1] always gives the last item. Why is that handier than
#     writing letters[4] when the list keeps growing? if you are coding a list that maybe autogenerates and you dont know how long the list is you can just use -1 to reference last in list
# Q3. .index('C') returns a number. What do you think happens if you call
#     letters.index('Z') when 'Z' is not in the list? (Try it, read the error.)- i got a value error. it doesnt exist within the index


# =============================================================================
# SECTION 2 — GUIDED  (fill in every # TODO)
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 2: GUIDED — Encode a Word by Hand")
print("=" * 52)

# The full codebook is given to you below (A-Z). You'll loop over it next
# week; this week you index into it by hand.
letters  = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
patterns = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---',
            '-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-',
            '..-','...-','.--','-..-','-.--','--..']

print(f"\nFull codebook loaded: {len(letters)} letters.")

# -- Encode the word "SOS" using three index lookups -----------------------
# We have no loop yet, so we do each letter explicitly.
# Step 1 is done for you. Do steps 2 and 3 the same way.

s_pattern = patterns[letters.index('S')]    # done for you
# TODO: get the pattern for 'O'
o_pattern = patterns[letters.index('O')]    # TODO: replace "" using patterns[letters.index(...)]
# TODO: get the pattern for the second 'S' (it's the same lookup as the first)
s2_pattern = patterns[letters.index('S')]   # TODO

print("\nEncoding 'SOS' by hand:")
print(f"  S -> {s_pattern}")
print(f"  O -> {o_pattern}")
print(f"  S -> {s2_pattern}")

# -- Combine the three patterns into one list, then print it ----------------
# TODO: put the three pattern variables into a list, in order
sos_encoded = [s_pattern, o_pattern, s2_pattern]   # TODO: e.g. [s_pattern, o_pattern, s2_pattern]
print(f"\n  'SOS' encoded -> {sos_encoded}")
# Expected once complete: ['...', '---', '...']


# =============================================================================
# SECTION 3 — EXTENSION  (working pattern; add one piece)
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION — Decode One Pattern by Hand")
print("=" * 52)

# Encoding goes letter -> pattern. DECODING goes the other way:
# pattern -> letter. With parallel lists we just search the OTHER list.
# Worked example: which letter is '-.-.' ?
decoded_position = patterns.index('-.-.')   # where does that pattern sit?
decoded_letter   = letters[decoded_position]
print(f"\nPattern '-.-.' is at position {decoded_position} -> letter '{decoded_letter}'")

# -- YOUR EXTENSION --------------------------------------------------------
# Decode the pattern '...' the same way: find its position in 'patterns',
# then read the matching letter from 'letters'. Print the result.
# (Week 3: a loop will let you decode a whole message at once.)

# TODO: decode the pattern '...' and print the letter


# =============================================================================
# SECTION 4 — STRETCH  (no starter code)
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 4: STRETCH — List Slicing and Sorting")
print("=" * 52)

# Using only list operations from Chapter 3 (slices, sorted(), len()):
#
#   1. Print just the FIRST FIVE letters using a slice (letters[:5]).
#   2. Print the LAST THREE patterns using a slice.
#   3. Make an alphabetically SORTED copy of 'letters' with sorted()
#      and confirm the original 'letters' list is unchanged.
#   4. In a comment, explain a danger of parallel lists: if you sorted
#      'letters' but not 'patterns', what would go wrong with lookups?
#      (This is the bug that dictionaries will make impossible in Week 5.)

# TODO: implement the stretch challenge here
decoded_position = patterns.index('...')
decoded_letter =letters[decoded_position]
print(f"Pattern '...' is at position {decoded_position} --> letter '{decoded_letter}'")

# =============================================================================
# CHECKLIST
#   [ ] ANCHOR:    ran it; answered Q1-Q3 (including the .index('Z') error)
#   [ ] GUIDED:    'SOS' encodes to ['...', '---', '...']
#   [ ] EXTENSION: '...' decodes to 'S'
#   [ ] STRETCH:   (optional) slicing + sorted() + the parallel-list danger
#   [ ] I can explain why parallel lists are fragile
#
# LOOKING AHEAD — Week 3
#   Next week you learn FOR LOOPS and TUPLES. You'll merge these two lists
#   into ONE list of (letter, pattern) pairs, and a loop will encode an
#   entire message automatically — no more copy-pasting index lookups.
# =============================================================================
