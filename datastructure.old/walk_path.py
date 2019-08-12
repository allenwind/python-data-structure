import os

def walk(path):
    try:
        files = os.listdir(path)
    except FileNotFoundError:
        files = []
    for file in files:
        if os.path.isfile(file):
            yield file
        else:
            yield from walk(file)

if __name__ == '__main__':
    for file in walk("F:"):
        print(file)