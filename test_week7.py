# test_week7.py
# TEST CASES — Week 7
#
# HOW TO RUN THESE TESTS:
#   Open the VS Code terminal (Ctrl+`)
#   Make sure you are in the same folder as bug_week7.py
#   Type: python test_week7.py
#   Press Enter.   (Or just open this file and click Run.)
#
# Nothing to install — this is a plain Python file.
#
# HOW A TEST WORKS:
#   Every test does the same three things:
#     1. CALL a function from bug_week7 with inputs you choose.
#     2. Write down the answer you EXPECT.
#     3. Use if / elif / else to compare them and print the verdict.
#
#   result   = bug_week7.apply_discount(50.00, 20)
#   expected = 40.00
#
#   if result == expected:
#       print("   PASS")
#   elif result is None:
#       print("   FAIL - got None. Is a return statement missing?")
#   else:
#       print("   FAIL - expected", expected, "but got", result)
#
# READING THE OUTPUT:
#   PASS  <- the function gave back exactly what we expected
#   FAIL  <- the function gave back something else.
#            The line tells you what you expected and what you got.
#   TODO  <- a test you haven't written yet

# YOUR JOB THIS WEEK:
#   Tests 1-6 are fully written — study them as examples.
#   Tests 7-9 are STUBS — fill them in using the same pattern.
#   Test 10 is MISSING — write the whole function from scratch.
#
# ============================================================
# WHAT MAKES A GOOD TEST CASE? (running list)
#   first    — first item / lowest input
#   middle   — typical input in the middle
#   last     — last item / highest input
#   missing  — input not in the data
#   edge     — unusual but valid (empty string, zero, spaces)
#   boundary — exact value where behavior changes
#   empty    — empty list, empty string, zero quantity
#
# For each stub below, think about which category of test case
# would be most valuable to write.
# ============================================================


# ============================================================
# IMPORT — the doorway between the two files
#
# bug_week7.py is a MODULE: just a .py file in the same folder.
# This line runs bug_week7.py once and gives us access to
# everything inside it. We call its functions with the module
# name in front:
#
#     bug_week7.format_student("ada", "lovelace", "A001")
#
# The demo code at the bottom of bug_week7.py does NOT run here,
# because it sits inside  if __name__ == "__main__":
# ============================================================
import bug_week7


# ============================================================
# TESTS FOR format_student()
# Fully written — read these carefully as your model.
# ============================================================

def test_format_student_typical():
    # MIDDLE / happy-path test case: a normal first name,
    # last name, and ID.
    print("\nTEST 1 (middle): format_student('jordan', 'smith', 'S001')")

    result = bug_week7.format_student("jordan", "smith", "S001")
    expected = "Smith, Jordan  (ID: S001)"

    if result == expected:
        print("   PASS")
    elif result is None:
        print("   FAIL - got None. Is a return statement missing?")
    else:
        print("   FAIL - expected", expected, "but got", result)


def test_format_student_all_caps():
    # EDGE test case: names typed in ALL CAPS should still
    # come out title-cased.
    print("\nTEST 2 (edge - all caps): format_student('JORDAN', 'SMITH', 'S002')")

    result = bug_week7.format_student("JORDAN", "SMITH", "S002")
    expected = "Smith, Jordan  (ID: S002)"

    if result == expected:
        print("   PASS")
    elif result is None:
        print("   FAIL - got None. Is a return statement missing?")
    else:
        print("   FAIL - expected", expected, "but got", result)


# ============================================================
# TESTS FOR apply_discount()
# Fully written. Each test uses a DIFFERENT category from the
# running list above, and the comment says WHY that input was
# chosen. Notice: the expected answer is always worked out BY
# HAND first, never copied from what the function prints.
# ============================================================

def test_apply_discount_middle():
    # MIDDLE: an ordinary, everyday discount.
    # Avoid "easy" numbers like $100 — with $100, a percent and a
    # dollar amount look the same, which can hide a mistake.
    # By hand: 20% of $50 is $10, so $50 - $10 = $40.
    print("\nTEST 3 (middle): apply_discount(50.00, 20) should be 40.0")

    result = bug_week7.apply_discount(50.00, 20)
    expected = 40.00

    if result == expected:
        print("   PASS")
    elif result is None:
        print("   FAIL - got None. Is a return statement missing?")
    else:
        print("   FAIL - expected", expected, "but got", result)


def test_apply_discount_zero():
    # BOUNDARY (low end): the smallest discount allowed.
    # By hand: 0% off means the price doesn't change.
    # Watch whether this one passes or fails right now.
    # One passing test does NOT prove a function is correct —
    # that's why we test several categories.
    print("\nTEST 4 (boundary - low): apply_discount(80.00, 0) should be 80.0")

    result = bug_week7.apply_discount(80.00, 0)
    expected = 80.00

    if result == expected:
        print("   PASS")
    elif result is None:
        print("   FAIL - got None. Is a return statement missing?")
    else:
        print("   FAIL - expected", expected, "but got", result)


def test_apply_discount_full():
    # BOUNDARY (high end): the largest discount allowed.
    # By hand: 100% off means the item is free.
    # A price can never go below $0.00.
    print("\nTEST 5 (boundary - high): apply_discount(80.00, 100) should be 0.0")

    result = bug_week7.apply_discount(80.00, 100)
    expected = 0.00

    if result == expected:
        print("   PASS")
    elif result is None:
        print("   FAIL - got None. Is a return statement missing?")
    else:
        print("   FAIL - expected", expected, "but got", result)


def test_apply_discount_odd_price():
    # EDGE: a realistic, un-round price and percent.
    # Real prices end in .99 and discounts aren't always round.
    # This also checks that the answer is rounded to cents.
    # By hand: 15% of $19.99 is about $3.00, so $19.99 - $3.00 = $16.99.
    print("\nTEST 6 (edge - odd price): apply_discount(19.99, 15) should be 16.99")

    result = bug_week7.apply_discount(19.99, 15)
    expected = 16.99

    if result == expected:
        print("   PASS")
    elif result is None:
        print("   FAIL - got None. Is a return statement missing?")
    else:
        print("   FAIL - expected", expected, "but got", result)



# ============================================================
# STUB 1 (TEST 7) — Your turn: apply_discount() on a FREE item
#
# What should 50% off a $0.00 item be?
# Work out the answer BY HAND before you write the test.
#
# Test case category: EMPTY (zero quantity)
#
# TO DO:
#   1. Delete the TODO print line.
#   2. Write the result = ... line (call the function).
#   3. Write the expected = ... line.
#   4. Copy the if / elif / else from any test above.
# ============================================================
def test_apply_discount_free_item():
    print("\nTEST 7 (empty): apply_discount(0.00, 50) should be 0.0")
    result = bug_week7.apply_discount(0.00, 50)
    expected = 0.00

    if result ==expected:
        print("   PASS")
    elif result is None:
        print("   FAIL - got None. Is a return statement missing?")
    else:
        print("   FAIL - expected", expected, "but got", result)



# ============================================================
# STUB 2 (TEST 8) — Your turn: format_schedule(), typical case
#
# Use these inputs:
#     name    = "maria"
#     courses = ["Python", "Circuits"]
#
# The expected value is ONE string. The \n means "new line":
#     "Schedule for Maria:\n  - Python\n  - Circuits\n"
#
# Test case category: MIDDLE (typical schedule)
# ============================================================
def test_format_schedule_typical():
    print("\nTEST 8 (middle): format_schedule('maria', ['Python', 'Circuits'])")

    name    = "maria"
    courses = ["Python", "Circuits"]
    result = bug_week7.format_schedule(name, courses)
    expected = "Schedule for Maria:\n  - Python\n  - Circuits\n"
    if result == expected:
        print("   PASS")
    elif result is None:
        print("   FAIL - got None. Is a return statement missing?")
    else:
        print("   FAIL - expected", expected, "but got", result)


# ============================================================
# STUB 3 (TEST 9) — Your turn: format_schedule(), NO courses
#
# A brand-new student hasn't signed up for anything yet.
# What should the schedule look like with an EMPTY list?
#     courses = []
#
# Think it through: the heading line is still there, but there
# are no course lines under it. Write that as one string.
#
# Test case category: EMPTY (empty list)
# ============================================================
def test_format_schedule_empty():
    print("\nTEST 9 (empty): format_schedule('maria', [])")
    name    = "maria"
    courses = []
    result = bug_week7.format_schedule(name, courses)
    expected = "Schedule for Maria:\n"
    if result == expected:
        print("   PASS")
    elif result is None:
        print("   FAIL - got None. Is a return statement missing?")
    else:
        print("   FAIL - expected", expected, "but got", result)



# ============================================================
# MISSING TEST (TEST 10) — Write this one entirely from scratch.
#
# There is NO stub. You write the whole thing: the def line,
# the print line, the calls, and the if / elif / else.
#
# What to test: build_roster() called TWICE with no student list.
# Each call should start FRESH — the second call should know
# nothing about the first.
#
# Your test must:
#   1. Call bug_week7.build_roster("Python")   (ignore the result)
#   2. Call bug_week7.build_roster("Circuits") and save it in result
#   3. The second result should look exactly like a first call:
#          expected = {"Circuits": ["(enrolled)"]}
#   4. Compare with if / elif / else and print PASS or FAIL.
#
# Name it:  test_build_roster_twice
# Then go to the bottom of the file and UN-COMMENT the line
# that runs it.
#
# Test case category: STATEFUL (new!) — it needs TWO calls,
# because it checks whether one call affects the next.
# ============================================================

# Write your test here:
def test_build_roster_twice():
    print("\nTEST 10 (stateful): build_roster('Python') then build_roster('Circuits')")
    bug_week7.build_roster("Python")  # First call, ignore result
    result = bug_week7.build_roster("Circuits")  # Second call, save result
    expected = {"Circuits": ["(enrolled)"]}  # What we expect from the second call

    if result == expected:
        print("   PASS")
    elif result is None:
        print("   FAIL - got None. Is a return statement missing?")
    else:
        print("   FAIL - expected", expected, "but got", result)



# ============================================================
# RUN ALL THE TESTS
# Each line below calls one test function, in order.
# ============================================================
print("========== WEEK 7 TESTS ==========")
test_format_student_typical()
test_format_student_all_caps()
test_apply_discount_middle()
test_apply_discount_zero()
test_apply_discount_full()
test_apply_discount_odd_price()
test_apply_discount_free_item()
test_format_schedule_typical()
test_format_schedule_empty()
test_build_roster_twice()      # <- un-comment after you write TEST 10
print("\n==================================")


# ============================================================
# HOW TO KNOW YOU ARE DONE:
#
# Run: python test_week7.py
#
# You should see PASS under every test:
#   TEST 1   PASS
#   TEST 2   PASS
#   TEST 3   PASS
#   TEST 4   PASS
#   TEST 5   PASS
#   TEST 6   PASS
#   TEST 7   PASS   <- your stub
#   TEST 8   PASS   <- your stub
#   TEST 9   PASS   <- your stub
#   TEST 10  PASS   <- your new test
#
# 10 PASS lines and no TODO lines = all 4 bugs fixed
#                                  + all tests written.
# ============================================================
