# bug_week2.py
# BUG OF THE WEEK - Week 2: Lists & Sensor History Buffers
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Use the SAME structured debugging steps you used in Week 1.
#
# ============================================================
# HOW TO DEBUG IN A STRUCTURED WAY:
#
#   STEP 1: Run the program and READ the error message carefully.
#           - What LINE number does it point to?
#           - What TYPE of error is it? (IndexError, AttributeError, TypeError...)
#
#   STEP 2: Go to that line and fix ONE bug at a time.
#
#   STEP 3: Save and RUN again.
#
#   STEP 4: Repeat until the program runs cleanly AND prints the RIGHT answer.
#
#   NEW THIS WEEK: the LAST bug does NOT crash the program!
#   It runs, but prints the WRONG number. You will have to read the
#   output carefully -- and use the DEBUGGER -- to catch it.
# ============================================================

# A history buffer of the last 5 temperature readings (in Celsius)
readings = [23.6, 23.1, 22.8, 23.4, 23.0]

# --- REPORT THE OLDEST AND NEWEST READINGS ---
# This line is correct -- no bug here.
print("Oldest reading: " + str(readings[0]))

# BUG HINT: A list with 5 items has indexes 0 through 4.
#           What is the index of the LAST item? What happens if you go past it?
print("Newest reading: " + str(readings[4]))

# --- ADD A NEW READING TO THE BUFFER ---
# BUG HINT: Which list method ADDS an item to the END of a list?
#           It is NOT .add() -- that belongs to a different data type.
readings.append(22.6)

# --- COUNT HOW MANY READINGS ARE ABOVE THE WARNING THRESHOLD --- 4
WARN = 23.0
warm_count = 0

# BUG HINT: This loop is supposed to check EVERY reading.
#           Look closely at where range() STARTS. Which index gets skipped?
#           Set a breakpoint here and watch 'i' and 'warm_count' in the debugger.
for i in range(0, len(readings)):
    if readings[i] > WARN:
        warm_count = warm_count + 1

# BUG HINT: warm_count is a number (int).
#           Can you join a number to a string with + directly?
print("Readings above " + str(WARN) + " C: " + str(warm_count))
message = f"readings-{readings}"
print(message)

# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#   1. Which bug was hardest to find: a crash, or the one that printed
#      the wrong number without crashing? Why?
#   2. How did the debugger help you see what the loop was doing?
#   3. What is the difference between an IndexError and an AttributeError?
# ============================================================
