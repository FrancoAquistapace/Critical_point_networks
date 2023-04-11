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
        self.ref_counter = 0
        
        self.neigh_list = []
        
    def build_neighs(self, all_neurons):
        for n in all_neurons:
            x_dist = self.x - n.x
            y_dist = self.y - n.y
            distance = sqrt((x_dist ** 2) + (y_dist ** 2))
            if distance <= RADIO*SPACING and not self.id == n.id:
                self.neigh_list.append(n)
                
    def get_next(self):
        input = 0
        prob = random(0.0, 1.0)
        for n in self.neigh_list:
            input += n.state
        if (input >= THRESH or prob < SPONT_FIRE) and self.ref_counter <= 0:
            self.next_state = 1
            self.ref_counter = REF_PERIOD
        else:
            self.next_state = 0
        
    def update(self):
        new_state = self.next_state
        self.state = new_state
        self.ref_counter += -1
        
        
    def show(self):
        fill(255 * (1 - self.state))
        square(self.x, self.y, self.sq_size)
