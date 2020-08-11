__all__ = ['get_code']

data = {'G': 'T', 'b': 'o', 'X': 'K', 'S': 'F', 'j': 'w', 't': 'g',
 'F': 'S', 'o': 'b', 'Z': 'M', 'W': 'J', 'l': 'y', 'Y': 'L',
 'D': 'Q', 'T': 'G', 'i': 'v', 'J': 'W', 'U': 'H', 'g': 't',
 'f': 's', 'C': 'P', 'B': 'O', 'w': 'j', 'P': 'C', 'v': 'i',
 'y': 'l', 'x': 'k', 'A': 'N', 'z': 'm', 'E': 'R', 'r': 'e',
 'K': 'X', 'L': 'Y', 'k': 'x', 'V': 'I', 'h': 'u', 'u': 'h',
 'p': 'c', 'd': 'q', 'O': 'B', 'n': 'a', 'e': 'r', 'q': 'd',
 's': 'f', 'I': 'V', 'M': 'Z', 'H': 'U', 'N': 'A', 'Q': 'D',
 'c': 'p', 'm': 'z', 'a': 'n', 'R': 'E'}

def get_code(string):
    return ''.join([data.get(c, c) for c in string])
