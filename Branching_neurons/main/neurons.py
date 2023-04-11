from params import *

class Neuron(object):
    def __init__(self, i, j, id):
        self.i = i
        self.j = j
        self.x = j * SPACING
        self.y = i * SPACING
        self.sq_size = SPACING
        
        self.id = id
        
        self.state = 0
        self.next_state = 0

        self.neigh_list = []
        self.weights = []
        
    def build_neighs(self, all_neurons):
        while len(self.neigh_list) < N_NEIGH:
            prob = int(random(0.0, len(all_neurons)))
            new_n = all_neurons[prob]
            if (self.id != new_n.id) and (not new_n.id in self.neigh_list):
                self.neigh_list.append(new_n)
                self.weights.append(random(0.0, 1.0))
                
        # Normalize weights to sum up to SIGMA
        old_weights_sum = 0
        for w in self.weights:
            old_weights_sum += w
        for i in range(len(self.weights)):
            new_weight = self.weights[i] * SIGMA / old_weights_sum
            self.weights[i] = new_weight
                
    def get_next(self):
        if self.state == 1:
            for i in range(len(self.neigh_list)):
                n = self.neigh_list[i]
                w = self.weights[i]
                input = random(0.0, 1.0)
                if input <= w:
                    n.next_state += 1
        # Check for spontaneous firing
        prob = random(0.0, 1.0)
        if prob <= SPONT_FIRE:
            self.next_state += 1
        
    def update(self):
        new_state = self.next_state
        if new_state > 0:
            self.state = 1
        else:
            self.state = 0
        self.next_state = 0
        
        
    def show(self):
        fill(255 * (1 - self.state))
        square(self.x, self.y, self.sq_size)
