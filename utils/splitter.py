# splitter.py
import os

from pydub import AudioSegment
from pydub.silence import split_on_silence

import librosa
import soundfile as sf

def split_on_sil(path=None):
    dirname = os.path.dirname(__file__)
    root_dir = os.path.split(dirname)[0]
    samples_path = os.path.join(root_dir, 'sample_wav')

    if path == None:
        samples_list = os.listdir(samples_path)
        print('You have not entered any path to a wav file. So choose from the available samples:')

        for n, i in enumerate(samples_list):
            print(f'{n + 1 }. {i}')

        choice = int(input('Enter the Serial number here: '))


        path = os.path.join(samples_path, samples_list[choice - 1])
    else:
        pass
    y, s = librosa.load(path, sr=192000)
    sf.write(path, y, s)

    audio = AudioSegment.from_wav(path)
    dBFS = audio.dBFS
    splits = split_on_silence(audio,
                              min_silence_len=1000,
                              silence_thresh=dBFS-16,
                              )
    print(f'Total initial splits: {len(splits)}')
    longer_splits = [splits[0]]
    for split in splits[1:]:
        if len(longer_splits[-1]) < 45000:
            longer_splits[-1] += split
        else:
            longer_splits.append(split)
    i = 0
    print(f'After check: {len(longer_splits)}')
    for split in longer_splits:

        chunk_name = f'chunk{i}.wav'
        #chunk_path = f'{root_dir}/chunks/{chunk_name}'
        chunk_path = os.path.join(root_dir, 'chunks')
        chunk_path = os.path.join(chunk_path, chunk_name)
        split.export(chunk_path, bitrate='192k', format="wav")
        i += 1
