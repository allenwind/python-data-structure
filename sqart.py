import random

def square(x, accuracy=100):
    val = x/2
    for _ in range(accuracy):
        val = (val + x/val)/2

    return val

def test():
    for _ in range(20):
        val = random.uniform(1, 99999999)
        out = square(val)
        print("input: {}, output: {}, accuracy: {}".format(val, out**2, val-out**2))

if __name__ == '__main__':
    test()
    
    
