# Breeding

import random


def breed(genA,genB):
    aSize = int(len(genA)/2)
    bSize = int(len(genB)/2)

    aMix = ''.join(random.sample(genA,len(genA)))
    bMix = ''.join(random.sample(genB,len(genB)))

    child1 = ''.join(random.sample(aMix[0:aSize]+bMix[0:bSize],aSize+bSize))
    child2 = ''.join(random.sample(aMix[aSize:]+bMix[bSize:],aSize+bSize))
    return [child1,child2]

def mutate(gen):
    ind = []
    for i in range(2):
        ind.append(random.randint(0,len(gen)-1))

    gen = list(gen)
    gen[ind[0]],gen[ind[1]] = gen[ind[1]], gen[ind[0]]
    
    return ''.join(gen)
    
    
    
