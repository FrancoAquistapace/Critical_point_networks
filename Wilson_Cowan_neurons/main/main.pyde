from neurons import *
from params import *

neurons = []

def setup():
    #size(SCREEN_WIDTH, SCREEN_HEIGHT, P2D)
    size(SCREEN_SIZE, SCREEN_SIZE)
    frameRate(10)
    global neurons
    id = 0
    for i in range(SIZE):
        for j in range(SIZE):
            neurons.append(Neuron(i,j,id))
            id += 1
    
    for n in neurons:
        n.build_neighs(neurons)
    
def draw():
    background(0)
    #blendMode(ADD)
    global neurons
    for n in neurons:
        n.get_next()
    for n in neurons:
        n.update()
        n.show()
