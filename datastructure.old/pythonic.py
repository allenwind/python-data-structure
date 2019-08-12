import functools
import hashlib

def hexdigest(path, trunk=1024**2):
    md5 = hashlib.md5()
    with open(path, "rb") as fd:
        ifd = iter(functools.partial(fd.read, trunk), b'')
        for data in ifd:
            md5.update(data)
    return md5.hexdigest()

def main():
    path = r'D:\software\linuxmint-18.3-cinnamon-64bit.iso'
    md5_hex = hexdigest(path)
    print(md5_hex)

if __name__ == '__main__':
    main()
