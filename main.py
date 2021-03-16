# main.py

from utils.splitter import split_on_sil
from utils.speech_to_text import splits_to_string

def convert_speech(path=None):
    split_on_sil(path)
    speech_converted = splits_to_string()
    return speech_converted
txt = convert_speech()
print(txt)