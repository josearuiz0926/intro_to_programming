# =============================================================================
# hal_pc.py  -  the PC version of the hardware (the "emulator")
#
# There are no real pins on your PC, so this file PRETENDS:
#   - the LED just prints "[LED] ON" / "[LED] OFF"
#
# hal_pico.py has these SAME function names for the real Pico, so the SAME
# program runs in both places without changing a line.
# =============================================================================

import time
import photoresistor      # the fake photoresistor engine


# --- LED ---------------------------------------------------------------------
def set_led(on):
    if on:
        print("[LED] ON")
    else:
        print("[LED] OFF")


def sleep_ms(ms):
    time.sleep(ms / 1000.0)


def set_led_timed(on, ms):
        set_led(on)
        print(f"[LED] TIMED for {ms} ms")
        sleep_ms(ms)


def now_ms():
    return int(time.monotonic() * 1000)


def elapsed_ms(since):
    return now_ms() - since


def board_info():
    return "PC emulator (hal_stub)"


# --- photoresistor (there is no real ADC on a PC, so we use the fake one) ----
def read_u16():
    return photoresistor.read()      # the latest value from the fake sensor


def play(message):
    # Test helper: make the photoresistor "see" this message. (On real hardware
    # the light comes from a real sender instead.)
    photoresistor.play(message)
