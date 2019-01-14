import re

def abbreviate(words):
    words = re.sub(r'[\-]', ' ', words.upper())
    result_list = re.sub(r'[^A-Z\s]', '', words).split()
    result = ''
    for word in result_list:
        result += word[0]
    return result
