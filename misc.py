import networkx as nx
import matplotlib.pyplot as plt

from animal import Animal

def draw_animal_genome(animal):
    G = nx.DiGraph()
    for (nid1, neuron) in animal.brain.neurons.items():
        G.add_node(nid1)
        for (neuron2, w) in neuron.inputs:
            G.add_weighted_edges_from([(neuron2.nid, nid1, w*1000)])
    pos = nx.spring_layout(G, pos=nx.random_layout(G), iterations=200)
    nx.draw_networkx(G, pos=pos, with_labels=True)
    plt.show()

def draw_genome(genome):
    animal = Animal(genome, 1)
    draw_animal_genome(animal)