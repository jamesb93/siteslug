from pathlib import Path
import os

sounds = [x for x in Path(".").rglob('*.wav')]

for i, x in enumerate(sounds):
    os.rename(x, f'static/sounds/{i}.wav')
    
