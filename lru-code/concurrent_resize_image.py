import os
import time
import concurrent.futures
import functools

import cropresize2

from PIL import Image

def resize_image(path, weight, height):
    fd = open(path, 'rb')
    image = Image.open(fd, mode='r')

    img = cropresize2.crop_resize(image, (weight, height))
    a, b = os.path.split(path)
    target = a + 'resize_' + b
    img.save(target)
    fd.close()
    return os.stat(target)

def image_size(path):
    with open(path, 'rb') as fd:
        img = Image.open(fd)
        return img.size

def concurrent_resize(src_dir):
    os.chdir(src_dir)
    files = os.listdir(src_dir)
    resize = functools.partial(resize_image, weight=64, height=64)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for file, stat in zip(files, executor.map(resize, files)):
            print(file, stat)

if __name__ == '__main__':
    src_dir = ''
    concurrent_resize(src_dir)
    


