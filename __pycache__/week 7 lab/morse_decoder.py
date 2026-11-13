from morse_codebook import DECODE_MAP
def decode_pattern(pattern, unknown_char='?'):
    """Return the character for one Morse pattern, or unknown_char."""
    return DECODE_MAP.get(pattern, unknown_char)

def decode_message(encoded):
    """Return the decoded text string for a list of Morse patterns."""
    letters = []
    for pattern in encoded:
        if pattern == ' ':
            letters.append(' ')
        else:
            letters.append(decode_pattern(pattern))
    return "".join(letters)