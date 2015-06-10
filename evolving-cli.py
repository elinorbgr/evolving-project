#!/bin/env python3

import sys

from neural import random_genome
from simulator import Simulator

from conf import WIDTH, HEIGHT, ANIMAL_COUNT, TIME_TICK
from conf import INIT_GENOME_LEN, INIT_GENOME_POOL
from conf import OUTPUT_PERIOD, OUTPUT_PREFIX, DEBUG_TIME

def main():
    if len(sys.argv) < 2:
        genomes = [ random_genome(INIT_GENOME_LEN) for _ in range(INIT_GENOME_POOL) ]
        sim = Simulator(WIDTH, HEIGHT, ANIMAL_COUNT, genomes)
    else:
        sim = Simulator(WIDTH, HEIGHT, 0, [])
        with open(sys.argv[1]) as f:
            for line in f:
                sim.insert_animal(line.strip())

    next_output = 0
    time = 0
    deltatime = TIME_TICK

    while True:
        # output to file
        next_output -= deltatime
        if next_output <= 0:
            next_output = OUTPUT_PERIOD
            with open(OUTPUT_PREFIX + str(time) + ".txt", 'w') as f:
                f.writelines(a.brain.genome + "\n" for a in sim.animals)
        # update state
        time += deltatime
        sim.update(deltatime)
        # debug
        if DEBUG_TIME:
            print("time: " + str(time))

if __name__ == '__main__':
    main()
