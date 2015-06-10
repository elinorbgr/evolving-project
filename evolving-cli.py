#!/bin/env python3

from neural import random_genome
from simulator import Simulator

from conf import WIDTH, HEIGHT, ANIMAL_COUNT, TIME_TICK
from conf import INIT_GENOME_LEN, INIT_GENOME_POOL
from conf import OUTPUT_PERIOD, OUTPUT_PREFIX, DEBUG_TIME

def main():
    genomes = [ random_genome(INIT_GENOME_LEN) for _ in range(INIT_GENOME_POOL) ]

    sim = Simulator(WIDTH, HEIGHT, ANIMAL_COUNT, genomes)

    next_output = 0
    time = 0
    deltatime = TIME_TICK

    while True:
        # output to file
        next_output -= deltatime
        if next_output <= 0:
            next_output = OUTPUT_PERIOD
            with open(OUTPUT_PREFIX + str(time) + ".txt", 'w') as f:
                f.writelines("{} : {}".format(a.energy, a.brain.genome) for a in sim.animals)
        # update state
        time += deltatime
        sim.update(deltatime)
        # debug
        if DEBUG_TIME:
            print("time: " + str(time))

if __name__ == '__main__':
    main()
