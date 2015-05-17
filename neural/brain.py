import math

from neural.genomparser import parse_genome, neuron_type

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

class Neuron:
    def __init__(self):
        self.value = 0.0
        self.value_buffer = 0.0
        self.bias = 0.0
        self.inputs = []

    def connect(self, neuron, weight):
        self.inputs.append((neuron, weight))

    def compute(self):
        x = self.bias
        for (n, w) in self.inputs:
            x += w * n.value
        self.value_buffer = sigmoid(x)

    def sync(self):
        self.value = self.value_buffer
        self.value_buffer = 0.0

def find_best_match(nid, neurons):
    if nid in neurons:
        return nid
    else:
        best_match = ""
        best_score = 0
        for n in neurons.keys():
            if n.len() > best_score and n.len() < nid.len():
                if nid.endswith(n):
                    best_match = n
                    best_score = n.len()
        if best_score > 0:
            return best_match
        else:
            return None

class Brain:
    def __init__(self, genome, hard_inputs, hard_outputs):
        self.genome = genome
        (declarations, links) = parse_genome(genome)
        self.network = Network()
        self.neurons = {}
        self.ampl_input_neurons = {}
        self.dir_input_neurons = {}
        self.output_neurons = {}

        self.hard_outputs = hard_outputs

        for name in hard_inputs:
            n = Neuron()
            self.neurons[name] = n

        for name in hard_outputs:
            n = Neuron()
            self.neurons[name] = n

        for (nid, value) in declarations:
            n = Neuron()
            self.neurons[name] = n
            t = neuron_type(n)
            if t == 1:
                self.ampl_inputs[value] = n
            elif t == 2:
                self.dir_inputs[value] = n
            elif t == 3:
                self.outputs[value] = n
            else:
                if value % 2 == 0:
                    n.bias = float(value) / 1000
                else:
                    n.bias = -float(value) / 1000

        for (nid1, val1, nid2, val2) in links:
            bid1 = best_match(nid1, self.neurons)
            if bid1 is None:
                continue
            bid2 = best_match(nid2, self.neurons)
            if bid2 is None:
                continue
            w = float(val1 - val2) / 1000
            self.neurons[bid2].connect(self.neurons[bid1], w)

    def compute(self, hard_inputs, inputs):
        for (k,v) in hard_inputs.items():
            self.neurons[k].value = v
        for (k,(ampliture, direction)) in ampl_inputs.items():
            if k in self.ampl_inputs_neurons:
                self.ampl_input_neurons[k].value = ampliture
            if k in self.dir_input_neurons:
                self.dir_input_neurons[k].value = direction
        for n in self.neurons:
            n.compute()
        for n in self.neurons:
            n.sync()
        houtputs = {}
        for o in self.hard_outputs:
            houtputs[o] = self.neurons[o].value
        outputs = {}
        for (o, n) in self.output_neurons:
            outputs[o] = n.value
        return (houtputs, outputs)

