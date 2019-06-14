from PIL import Image
from pathlib import Path

image_path = Path('./img')

for img_file in image_path.glob('**/*.png'):
    with Image.open(img_file) as im:
        im.resize((250, 270)).save(img_file)

print('save images')
