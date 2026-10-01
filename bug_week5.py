# bug_week5.py
# BUG OF THE WEEK - Week 5: Dictionaries
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Use the SAME structured debugging steps from earlier weeks, plus the
# VS Code Debugger for the ones that do not crash.
#
# ============================================================
# STANDARD DEBUGGING PROCESS (review):
#
#   STEP 1: Run the program — read the error TYPE and LINE number.
#   STEP 2: Go to that line, fix ONE bug, save, and run again.
#   STEP 3: Repeat until the program runs with no crashes.
#   STEP 4: CHECK YOUR OUTPUT — a program that runs is not
#           necessarily a program that WORKS. Compare what prints
#           to the "Expected output" at the bottom of this file.
#
#   NEW THIS WEEK: dictionaries. A dictionary looks a value up by its
#   KEY instead of by a position number. Two things to watch for:
#     - KEYS ARE EXACT. "Alice" and "alice" are two different keys.
#     - A bad key raises a KeyError (a crash you can read).
#
#   Use the DEBUGGER for the bugs that do NOT crash: set a breakpoint,
#   Step Over (F10), and WATCH the variables change in the left panel.
# ============================================================

# A grade book: each student NAME (the key) maps to their GRADE (the value).
grade_book = {
    "alice":   95,
    "bob":     82,
    "carlos":  90,
    "diana":   78,
    "eve":     93,
}

# ============================================================
# BUG 1 — Find with: standard run 
#
# HINT: Dictionary keys are exact. 
# ============================================================
print("--- Grade Lookup ---")
student = "Alice"
print(f"{student}'s grade: {grade_book[student.lower()]}")

print("\n--- All Grades ---")
for name, grade in grade_book.items():
    print(f"  {name}: {grade}")


# ============================================================
# BUG 2 - Noisy
# ============================================================
# ============================================================
# BUG 3 -Silent -  Find with: VS Code Debugger
# ============================================================
print("\n--- Honor Roll (grade >= 90) ---")
for name, grade in grade_book.items():
    if grade >= 90:
        print(f"  {name.title()} made the honor roll!")


# ============================================================
# BUG 4 — Find with: VS Code Debugger (logic error, no crash)
#
# HINT: This is supposed to find the student with the HIGHEST grade.
#       Run it — does it find anyone? Set a breakpoint on the 'if' inside
#       the loop and watch 'top_grade'. 
# ============================================================
print("\n--- Top Student ---")
top_student = ""
top_grade = 0
for name, grade in grade_book.items():
    if grade > top_grade:
        top_student = name
        top_grade = grade

if top_student:
    print(f"  Top student: {top_student.title()} with a {top_grade}")
else:
    print("  No top student found.")


# ============================================================
# EXPECTED OUTPUT (once all 4 bugs are fixed)
# ------------------------------------------------------------
#   --- Grade Lookup ---
#   Alice's grade: 95
#
#   --- All Grades ---
#     alice: 95
#     bob: 82
#     carlos: 90
#     diana: 78
#     eve: 95
#
#   --- Honor Roll (grade >= 90) ---
#     Alice made the honor roll!
#     Carlos made the honor roll!
#     Eve made the honor roll!
#
#   --- Top Student ---
#     Top student: Alice with a 95
# ============================================================


