# -*- coding: utf-8 -*-
import librosa
import wave
from pathlib import Path

def prepare_wav(wav):
     parts = wav.split('.')
     try:
         wave.open(wav, 'r')
     except:
         old_wav = wav + ""
         try:
             wav_file, sr = librosa.load(wav, sr=None, mono=False)
         except:
             return wav
         parts[-1] = "wav"
         wav = '.'.join(parts)
         try:
             soundfile.write(wav, wav_file.T, sr, format='WAV')
         except:
             return old_wav
         if old_wav != wav:
             os.remove(old_wav)
     return wav

def make_wav_scp(wav):
    scp='temp/wav.scp'
    with open(scp, 'w') as f:
         wav_file = wave.open(wav, 'r')
         if wav_file.getnchannels() == 1:
             f.write(str(Path(wav).stem) + '.0\t' + 'sox ' + wav + ' -t wav - remix 1 |\n')
         else:
             f.write(str(Path(wav).stem) + '.0\t' + 'sox ' + wav + ' -t wav - remix 1 |\n')
             f.write(str(Path(wav).stem) + '.1\t' + 'sox ' + wav + ' -t wav - remix 2 |\n')
