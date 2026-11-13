# =============================================================================
# hal_pico.py  -  the REAL hardware version, for the Pico 2 (on Wokwi or a board)
#
# Same function names as hal_stub.py, so the SAME program runs here without
# any change. This file is the only place that knows about real pins.
#
# =============================================================================

from machine import Pin, ADC
import time
import photoresistor      # the fake photoresistor engine (used until USE_REAL)

# Flip this to True once a REAL photoresistor is wired to GP26. Nothing else in
# your program changes - read_u16() keeps working the same way.
USE_REAL = False

# --- Pins --------------------------------------------------------------------
ONBOARD_LED_PIN = 25           # the Pico 2's built-in LED (no wiring needed)
TX_LED_PIN      = 25           # the LED we TRANSMIT on.
LDR_ADC_PIN     = 26           # ADC0 - wire the photoresistor's AO pin here
LIGHT_THRESHOLD = 30000   # placeholder - calibrate() overrides this at runtime

hwLED = Pin(TX_LED_PIN, Pin.OUT)
hwPR = ADC(Pin(LDR_ADC_PIN))


def set_led(on):
    if on:
        hwLED.value(1)
    else:
        hwLED.value(0)

def sleep_ms(ms):
    time.sleep_ms(ms)

def set_led_timed(on, ms):
    set_led(on)
    time.sleep_ms(ms)

def now_ms():
    return time.ticks_ms()

def elapsed_ms(since):
    # ticks_diff handles the timer wrapping around; use it instead of a-b.
    return time.ticks_diff(time.ticks_ms(), since)


def board_info():
    return "Raspberry Pi Pico 2 (hal_pico)"


# --- photoresistor -----------------------------------------------------------
def read_u16():
    if USE_REAL:
        return hwPR.read_u16()       # the REAL photoresistor on GP26 (ADC0)
    else:
        return photoresistor.read()  # the fake sensor (no wiring needed)


def play(message):
    # With the fake sensor, make it "see" this message. On real hardware the
    # light comes from a real sender, so there is nothing to play.
    if not USE_REAL:
        photoresistor.play(message)
