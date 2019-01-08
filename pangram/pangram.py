def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def is_pangram(sentence):
    freq_dict = {}
    for letter in char_range('a', 'z'):
        freq_dict[letter] = 0
    for i in list(sentence.replace(" ", "")):
        freq_dict[i] += 1
    return False if 0 in freq_dict.values() else True
