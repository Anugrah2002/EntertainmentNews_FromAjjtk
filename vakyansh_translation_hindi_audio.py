# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MS4FYm5kVXbVaQXSXLCGviOyJJFRCmM3
"""

import os
import sys


os.system('git clone https://github.com/Open-Speech-EkStep/vakyansh-tts')
os.chdir('vakyansh-tts') 
os.system('bash install.sh')
os.system('python setup.py bdist_wheel')
os.system ('pip install -e .')
os.chdir('tts_infer')
os.system('mkdir translit_models')
os.chdir('translit_models')
os.system('wget https://storage.googleapis.com/vakyaansh-open-models/translit_models/default_lineup.json')
os.system('mkdir hindi')
os.chdir('hindi')
os.system('wget https://storage.googleapis.com/vakyaansh-open-models/translit_models/hindi/hindi_transliteration.zip')
os.system('unzip hindi_transliteration.zip')

os.system ('wget https://storage.googleapis.com/vakyansh-open-models/tts/hindi/hi-IN/female_voice_0/glow.zip')
os.system('unzip glow.zip')

os.system('wget https://storage.googleapis.com/vakyansh-open-models/tts/hindi/hi-IN/female_voice_0/hifi.zip')
os.system('unzip hifi.zip')

os.system('rm glow.zip')
os.system('rm hifi.zip')

os.chdir('../../')

os.system('pip install unidecode')
os.system('pip3 uninstall numpy -y')
os.system('rm -rf ~/.local/lib/python3.6/site-packages/numpy')
os.system('pip install numpy')
print('line 42')
os.system('pwd')
print('line 44')
sys.path.insert(1, 'EntertainmentNews_FromAjjtk/vakyansh-tts/tts_infer')
import tts
import transliterate
import num_to_word_on_sent

import re
from scipy.io.wavfile import write
device = 'cpu'

text_to_mel = tts.TextToMel(glow_model_dir='translit_models/hindi/glow_ckp', device=device)
mel_to_wav = tts.MelToWav(hifi_model_dir='translit_models/hindi/hifi_ckp', device=device)

def translit(text, lang):
    reg = re.compile(r'[a-zA-Z]')
    engine = transliterate.XlitEngine(lang)
    words = [engine.translit_word(word, topk=1)[lang][0] if reg.match(word) else word for word in text.split()]
    updated_sent = ' '.join(words)
    return updated_sent
    
def run_tts(text, lang):
    text = text.replace('।', '.') # only for hindi models
    text_num_to_word = num_to_word_on_sent.normalize_nums(text, lang) # converting numbers to words in lang
    text_num_to_word_and_transliterated = translit(text_num_to_word, lang) # transliterating english words to lang
    
    mel = text_to_mel.generate_mel(text_num_to_word_and_transliterated, noise_scale=0.632, length_scale=0.80)
    audio, sr = mel_to_wav.generate_wav(mel)
    write(filename='temp.wav', rate=sr, data=audio) # for saving wav file, if needed
    return (sr, audio)
