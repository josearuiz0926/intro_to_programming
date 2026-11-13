from morse_codebook import ENCODE_MAP
def encode_message(message):
    """Return a list of Morse patterns for a message string.

    Spaces become ' ' (a word gap); unknown characters become '?'.
    """
    encoded = []
    for character in message.upper():
        if character == ' ':
            encoded.append(' ')
        else:
            encoded.append(ENCODE_MAP.get(character, '?'))
    return encoded