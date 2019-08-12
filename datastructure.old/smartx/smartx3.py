from enum import Enum

class Color(Enum):
    GREEN = 1
    RED = 2
    YELLOW = 3

class Fruit:
    pass

class Apple(Fruit):

    def __init__(self, color):
        '''
        @params color Color type
        '''
        self._color = color

class Watermelon(Fruit):

    def __init__(self, seedless):
        '''
        @params seedless boolean
        '''
        self._seedless = seedless

class Strawberry(Fruit):
    pass

class AbstractFruitGrower:

    def plant(self):
        pass

    def grow(self):
        pass

    def harvest(self):
        pass

class FruitGrower(AbstractFruitGrower):

    def plant(self, fruit):
        self.fruit = fruit
        # plant
        

    def grow(self, fruit):
        if not self.fruit:
            raise Exception("没有种植{}".format(fruit))
        # grow
        

    def harvest(self, fruit):
        if not self.fruit:
            raise Exception("没有培育{}".format(fruit))
        # harvert
        return self.fruit

    def sleep(self):
        pass

fg = FruitGrower()

def produce(fruit):
    fg.plant(fruit)
    fg.grow(fruit)
    r = fg.harvest(fruit)
    return r

def testing():
    f1 = produce(Apple(Color.RED))
    f2 = produce(Watermelon(True))

    
    
    




    
