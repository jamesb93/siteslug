from pathlib import Path
import os

sounds = [x for x in Path('b').rglob('*.aif')]

for i, x in enumerate(sounds):
    os.rename(x, f'static/sounds/{i+1}.aif')
