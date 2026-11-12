# hal_stub.py
# =============================================================================
# Week 7 — the Hardware Abstraction Layer (HAL), PC version.
#
# For six weeks the "LED" was a print() statement scattered through your
# code. That was fine on your laptop, but a real Pi Pico blinks a real LED
# with completely different commands (machine.Pin, utime.sleep_ms).
#
# The HAL is the trick that lets the SAME translator run in both places:
# every piece of hardware behavior is hidden behind a function here. Your
# main program never says print("[LED] ON") or touches a Pico pin directly —
# it just calls hal.set_led(True). To move to real hardware later, you swap
# in a file called hal_pico.py with the same function names but real pin
# code, and change ONE import line. Nothing else in the project changes.
#
# THIS file is the stub: it SIMULATES the hardware by printing.
# =============================================================================

def set_led(on):
    """Turn the (simulated) LED on or off."""
    print("  [LED] ON" if on else "  [LED] OFF")


def sleep_ms(milliseconds):
    """Pause for a number of milliseconds.

    On the Pico this is utime.sleep_ms(); on the PC we just announce it so
    you can read the timing without actually waiting.
    """
    print(f"      (hold {milliseconds}ms)")


def set_led_timed(on, milliseconds):
    """Set the LED, then hold that state for the given time. A convenience
    wrapper so transmit code reads as one step per symbol."""
    set_led(on)
    sleep_ms(milliseconds)


def get_board_info():
    """Identify which HAL is running. The Pico version returns 'Pi Pico'."""
    return "PC (hal_stub)"
