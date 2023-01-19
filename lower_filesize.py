import os
from PIL import Image


# for image in os.listdir(os.curdir):
#     if image.endswith('py'):
#         continue
#     image_name = os.path.basename(image)
#     current_image = Image.open(image)
#     current_image.save(f'new_{image_name}', quality=35, optimize=True)
    

for image in os.listdir(os.curdir):
    if image.endswith('py'):
        continue
    name = os.path.basename(image)
    new_name = name.split('new_')
    os.rename(image, new_name[1])
    