# bug_week7.py
# BUG OF THE WEEK - Week 7: Functions
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Bug 1: Find with the console error message.
# Bug 2: Find with the VS Code Debugger.
# Bug 3: Find with the VS Code Debugger + test cases.
# Bug 4: Can ONLY be found by a thoughtful test case —
#         the one the test file (test_week7.py) will catch.
#
# ============================================================
# STANDARD DEBUGGING PROCESS (review):
#   STEP 1: Run — read error type and line number.
#   STEP 2: Fix ONE bug, save, run again.
#   STEP 3: Repeat until no crashes.
#   STEP 4: CHECK YOUR OUTPUT. Running != correct.
#
# VS CODE DEBUGGER (review):
#   Set breakpoint : click gray margin left of line number
#   Start          : F5  ->  Python File
#   Step Into      : F11  <- NEW THIS WEEK: follows execution
#                          INSIDE the function body
#   Step Over      : F10  (run current line, pause on next)
#   Continue       : F5
#   Stop           : Shift+F5
#   Variables panel: left sidebar while paused
#
# ============================================================
# NEW THIS WEEK: STEP INTO vs. STEP OVER
#
# Last week you used F10 (Step Over) to move line by line.
# Step Over treats a function call as ONE step — it runs the
# whole function and pauses on the next line after it returns.
#
# F11 (Step Into) follows execution INSIDE the function.
# This is essential for debugging functions — you can watch
# the parameter values at the moment the function receives
# them, and trace exactly what happens inside.
#
# Rule of thumb:
#   Use F10 when you trust the function and want to skip it.
#   Use F11 when the function IS the thing you are debugging.
#
# ============================================================
# NEW THIS WEEK: THE TEST FILE
#
# A second file — test_week7.py — IMPORTS this file as a
# module and checks each function: it calls the function,
# compares the result to the expected answer with
# if / elif / else, and prints PASS or FAIL.
#
# To run the tests:
#   Open test_week7.py and click Run  — OR —
#   in the VS Code terminal, from the folder holding both files,
#   type: python test_week7.py   and press Enter.
#
# PASS = the function gave back exactly what was expected
# FAIL = it didn't — the line shows what was expected
#        and what the function actually gave back.
#
# Bug 4 in this file will PASS a visual check of the output.
# It will only be caught by one specific test (TEST 8).
# Run the tests, read the FAIL line, and trace back
# to the function to find and fix the bug.
#
# ============================================================
# NEW THIS WEEK: THE  if __name__ == "__main__"  GUARD
#
# Notice that all the demo calls (the print statements that
# show each function in action) now live at the BOTTOM of this
# file, inside a block that starts with:
#
#     if __name__ == "__main__":
#
# Here is why. test_week7.py needs to IMPORT this file to get
# at your functions. When Python imports a file, it runs every
# line in it from top to bottom. Without this guard, importing
# bug_week7.py would also run all the demo calls — including the
# ones with bugs in them. If one of them crashed, the test file
# would never even get to run your tests.
#
# The guard means: "only run the demo code when this file is
# run DIRECTLY (python bug_week7.py), NOT when it is imported."
#   - You run it directly  -> demos run, you see the bugs.
#   - test_week7.py imports it -> demos are skipped, tests run cleanly.
#
# This is the bridge between a standalone script and a reusable
# module. You'll use this same pattern in the in-class project.
# ============================================================


# ============================================================
# BUG 1 — Find with: the console error message
#
# format_student() should return a label like:
#     "Smith, Jordan  (ID: S001)"
#
# Run the file. Read the error type and the line number,
# then compare that line to the function definition.
# (The bug is in the demo block at the bottom of the file.)
# ============================================================
def format_student(first_name, last_name, student_id):
    """Return a formatted student label."""
    return f"{last_name.title()}, {first_name.title()}  (ID: {student_id})"


# ============================================================
# BUG 2 — Find with: VS Code Debugger using F11 (Step Into)
#
# format_schedule() should return a string listing a student's
# courses, one per line, like this:
#     Schedule for Maria:
#       - Python
#       - Circuits
#       - Technical Writing
#
# Run the file and compare what prints to what it should print.
#
# DEBUGGER INSTRUCTIONS:
#   1. Set a breakpoint on: schedule = format_schedule(name, courses)
#   2. Press F5 to start.
#   3. Press F11 (Step Into) — you jump INSIDE format_schedule.
#   4. Watch the Variables panel as you Step Over (F10) each line.
#   5. Keep stepping until you are back in the demo block.
#      What value did 'schedule' end up holding?
# ============================================================
def format_schedule(student_name, course_list):
    """Return a formatted schedule string for a student."""
    result = f"Schedule for {student_name.title()}:\n"
    for course in course_list:
        result += f"  - {course}\n"
    return result

# ============================================================
# BUG 3 — Find with: VS Code Debugger + test cases
#
# apply_discount() should apply a percentage discount to a price
# and return the discounted price. The discount is passed as a
# whole number (20 means 20%).
#
# DEBUGGER INSTRUCTIONS:
#   1. Set a breakpoint on: result = apply_discount(100.00, 20)
#   2. Press F11 to Step Into the function.
#   3. In the Variables panel, watch 'price' and 'discount_percent'.
#   4. Step Over the calculation line. What is 'discounted'?
#   5. Work out each Expected answer yourself, then run each case
#      by changing the numbers in the demo block. Fill in the table:
#
#   | Test Case        | price  | discount | Expected  | Actual | Pass? |
#   |------------------|--------|----------|-----------|--------|-------|
#   | A: 10% off $100  | 100.00 |   10     |     90.00 |        |       |
#   | B: 0% (no disc.) | 100.00 |    0     |     100.00 |        |       |
#   | C: 100% off      | 100.00 |  100     |           |        |       |
#   | D: 20% off $50   |  50.00 |   20     |     40.00 |        |       |
#   | E: BOUNDARY 1%   | 100.00 |    1     |      99.00 |        |       |
# ============================================================
def apply_discount(price, discount_percent):
    """Return price after applying a percentage discount."""
    discounted = price - (price * discount_percent / 100)
    return round(discounted, 2)


# ============================================================
# BUG 4 — Find with: TEST CASES (test_week7.py catches this)
#
# build_roster() takes a course name (and, optionally, a list of
# students) and returns a dictionary with the course as the key
# and the list of students as the value:
#     build_roster("Python")  ->  {'Python': ['(enrolled)']}
#
# This function looks correct, and a quick glance at the demo
# output may look fine too. Look closely at EVERY line it prints.
#
# Run: python test_week7.py
# Read the FAIL line for TEST 8: it shows the expected value and
# what the function actually gave back. Then come back here and
# trace through the function to find the bug.
# ============================================================
def build_roster(course_name, students=None):
    """Return a roster dictionary for a course."""
    roster = list(students) if students is not None else []
    roster.append("(enrolled)")    # simulates adding a marker
    return {course_name: roster}


# ============================================================
# DEMO BLOCK — runs ONLY when you run this file directly.
# (See "THE __main__ GUARD" note at the top of the file.)
# This is where the bugs show up when you press F5 / Run.
# ============================================================
if __name__ == "__main__":

    # --- Bug 1 demo ---
    print("--- Student Label ---")
    label = format_student("jordan", "smith",  "S001")
    print(label)

    # --- Bug 2 demo ---
    print("\n--- Course Schedule ---")
    name    = "maria"
    courses = ["Python", "Circuits", "Technical Writing"]
    schedule = format_schedule(name, courses)
    print(schedule)

    # --- Bug 3 demo: change the numbers to run the test cases ---
    print("\n--- Discount Calculator ---")
    result = apply_discount(100.00, 20)
    print(f"20% off $100.00 -> ${result}")

    # --- Bug 4 demo ---
    print("\n--- Course Roster ---")
    roster1 = build_roster("Python")
    print(roster1)
    roster2 = build_roster("Circuits")
    print(roster2)

