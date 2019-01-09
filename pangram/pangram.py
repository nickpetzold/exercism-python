import string as str
import re

def is_pangram(sentence):
    a_to_z = list(str.ascii_lowercase)
    freq_dict = {}
    for x in a_to_z:
        freq_dict[x] = 0
    arr = list(re.sub(r'[^a-z]','',sentence.lower()))
    print(arr)
    for a in arr:
        freq_dict[a] += 1

    return False if 0 in freq_dict.values() else True
