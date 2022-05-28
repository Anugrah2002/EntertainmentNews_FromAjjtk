# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MS4FYm5kVXbVaQXSXLCGviOyJJFRCmM3
"""

import os


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
os.system('unzip hindi_transliteration')

os.system ('wget https://storage.googleapis.com/vakyansh-open-models/tts/hindi/hi-IN/female_voice_0/glow.zip')
os.system('unzip glow.zip')

os.system('wget https://storage.googleapis.com/vakyansh-open-models/tts/hindi/hi-IN/female_voice_0/hifi.zip')
os.system('unzip hifi.zip')

os.system('rm glow.zip')
os.system('rm hifi.zip')

os.chdir('/workspace/EntertainmentNews_FromAjjtk/vakyansh-tts')

os.system('pip install unidecode')
os.system('pip3 uninstall numpy -y')
os.system('rm -rf ~/.local/lib/python3.6/site-packages/numpy')
os.system('pip install numpy==1.20.2')

from tts_infer.tts import TextToMel, MelToWav
from tts_infer.transliterate import XlitEngine
from tts_infer.num_to_word_on_sent import normalize_nums

import re
from scipy.io.wavfile import write
device = 'cpu'

text_to_mel = TextToMel(glow_model_dir='/workspace/EntertainmentNews_FromAjjtk/vakyansh-tts/tts_infer/translit_models/hindi/glow_ckp', device=device)
mel_to_wav = MelToWav(hifi_model_dir='/workspace/EntertainmentNews_FromAjjtk/vakyansh-tts/tts_infer/translit_models/hindi/hifi_ckp', device=device)

def translit(text, lang):
    print('translit line 55')
    try:
        print('translit line 55')
        reg = re.compile(r'[a-zA-Z]')
        print('translit line 55')
        engine = XlitEngine(lang)
        print('translit line 55')
        words = [engine.translit_word(word, topk=1)[lang][0] if reg.match(word) else word for word in text.split()]
        print('translit line 55')
        updated_sent = ' '.join(words)
        print('translit line 55')
        return updated_sent
    except Exception as e:
        print(e)

    
def run_tts(text, lang):
    print('runtts line 72')
    print(text)
    try:
        text = text.replace('।', '.') # only for hindi models
        print('runtts line 68')
        text_num_to_word = normalize_nums(text, lang) # converting numbers to words in lang
        print('runtts line 78')
        text_num_to_word_and_transliterated = translit(text_num_to_word, lang) # transliterating english words to lang
        print('runtts line 80')
        
        mel = text_to_mel.generate_mel(text_num_to_word_and_transliterated, noise_scale=0.632, length_scale=0.80)
        print('runtts line 83')
        print(type(mel))
        print('runtts line 85')
        print(mel)
        audio, sr = mel_to_wav.generate_wav(mel)
        print('runtts line 88')
        write(filename='temp.wav', rate=sr, data=audio) # for saving wav file, if needed
        print('runtts line 87')
        return (sr, audio)
    except Exception as e:
        print(e)

