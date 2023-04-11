from neurons import *
from params import *

neurons = []
output = 0
step = 0

def setup():
    size(SCREEN_SIZE, SCREEN_SIZE)
    frameRate(10)
    global neurons
    global output
    id = 0
    for i in range(SIZE):
        for j in range(SIZE):
            neurons.append(Neuron(i,j,id))
            id += 1
    
    for n in neurons:
        n.build_neighs(neurons)
        
    if WRITE:
        output = createWriter("activity_sigma_"+str(SIGMA)+".txt")
        output.println('#Size: '+str(SIZE ** 2))
        output.println("Step activity")
        
def draw():
    background(0)
    global neurons
    global output
    global step
    step += 1
    activity_tot = 0
    for n in neurons:
        n.get_next()
    for n in neurons:
        n.update()
        n.show()
        activity_tot += n.state
        
    if WRITE:    
        output.println(str(step)+" "+str(activity_tot))
        
        if step == STEPS:
            output.close()
            exit()
