import re

def lowercase_text(text):

    return text.lower()

def remove_punctuation(text):

    return re.sub(r'[^\w\s]', '', text)

def count_words(text):

    return len(text.split())
