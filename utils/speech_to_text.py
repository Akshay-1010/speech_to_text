# speech_to_text.py


import os
import time

import speech_recognition as sr

import librosa
import soundfile as sf

import animation


wheel = ("◢", "◣", "◤", "◥")
@animation.wait(wheel)
def splits_to_string():
    dirname = os.path.dirname(__file__)
    root_dir = os.path.split(dirname)[0]
    path = os.path.join(root_dir, 'chunks')
    print(path)
    total_string = ''
    splits = os.listdir(path)
    # reducing size
    for split in splits:
        wav_path = os.path.join(path, split)
        y, s = librosa.load(wav_path, sr=16000)
        sf.write(wav_path, y, s)
    r = sr.Recognizer()
    for split in sorted(splits):
        print(split)
        wav_path = os.path.join(path, split)
        audio = sr.AudioFile(wav_path)
        with audio as source:
            r.adjust_for_ambient_noise(source)
            #audio_listened = r.record(source)
            audio_file = r.record(source)
        total_string += r.recognize_google(audio_file)
        os.remove(wav_path)
        #rec = r.recognize_google(audio_listened)
        #total_string += rec
        #os.remove(split)


    return total_string