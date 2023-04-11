from neurons import *
from params import *

neuron_layers = []
all_neurons = []
output = 0
step = 0
layer = 0
activity_tot = [0 for i in range(SIZE)]

def setup():
    size(SCREEN_SIZE, SCREEN_SIZE)
    frameRate(30)
    global neuron_layers
    global output
    id = 0
    layer = 0
    for i in range(SIZE):
        neuron_layers.append([])
        for j in range(SIZE):
            neuron_layers[i].append(Neuron(i,j,id,layer))
            all_neurons.append(neuron_layers[i][j])
            id += 1
        layer += 1
    
    for i in range(len(neuron_layers) - 1):
        neurons = neuron_layers[i]
        next_neurons = neuron_layers[i+1]
        for n in neurons:
            n.build_neighs(next_neurons)
            
        
    if WRITE:
        output = createWriter("activity_sigma_"+str(SIGMA)+\
                              "_steps_"+str(STEPS)+\
                              "_size_"+str(SIZE)+".txt")
        output.println('#Size: '+str(SIZE ** 2))
        data_cols = "Wave"
        for i in range(SIZE):
            data_cols += " layer_" + str(i+1)
        output.println(data_cols)
        
def draw():
    background(0)
    global neuron_layers
    global output
    global step
    global layer
    global activity_tot
    step += 1
    
    neurons = neuron_layers[layer]
    
    # Fire neurons in the first layer     
    if layer == 0:
        # Select random indexes for the first layer neurons 
        # to activate
        fired_amount = min(1 + abs(randomGaussian() * SIZE / 3), 
                        TOP_ACTIVATION)
        activated_neurons = []
        while len(activated_neurons) < fired_amount:
            activate_id = floor(random(0,SIZE))
            if not activate_id in activated_neurons:
                activated_neurons.append(activate_id)
        for j in range(len(activated_neurons)):
            neurons[activated_neurons[j]].spont_fire()
            
    for n in all_neurons:
        n.update()
        n.show()
    
    for n in neurons:
        activity_tot[layer] += n.state
        n.get_next()    

        
    if WRITE and layer == SIZE - 1:   
        out_data = str((step+1) // SIZE) 
        for i in range(len(activity_tot)):
            out_data += " " + str(activity_tot[i]) 
        output.println(out_data)
        
    if WRITE and step == STEPS:
        output.close()
        exit()
            
    if layer == len(neuron_layers) - 1:
        layer = 0
        activity_tot = [0 for i in range(SIZE)]
    else:
        layer += 1
