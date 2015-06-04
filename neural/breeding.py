# Breeding

import random

from neural import ALPHABET

from conf import REBREEDING_CHANCE, MUTATION_RATE

def breed_cs(genA,genB):
    aCut = int(random.randint(0,int(len(genA)/2)) + len(genA)/4)
    bCut = int(random.randint(0,int(len(genB)/2)) + len(genB)/4)
    childA = []
    childB = []
    for i in range(0,aCut):
        childA.append(genA[i])
    for i in range(0,bCut):
        childB.append(genB[i])
    for i in range(bCut,len(genB)):
        childA.append(genB[i])
    for i in range(aCut,len(genA)):
        childB.append(genA[i])
    
    return [''.join(childA),''.join(childB)]



def breed_uni(genA,genB):
    childA = []
    childB = []
    size = min(len(genA),len(genB))
    for i in range(size):
        r = random.randint(0,100)
        if r < 50:
            childA.append(genA[i])
            childB.append(genB[i])
        else:
            childA.append(genB[i])
            childB.append(genA[i])
    if len(genA)< len(genB):
        for i in range(size,len(genB)):
            childB.append(genB[i])
    else:
        for i in range(size,len(genA)):
            childA.append(genA[i])
    return [''.join(childA),''.join(childB)]

def breed_2px(genA,genB):
    childA = []
    childB = []
    r = []
    size = min(len(genA),len(genB))
    for i in range(2):
        r.append(random.randint(0,size))
    
    for i in range(0,min(r)):
        childA.append(genA[i])
        childB.append(genB[i])
    for i in range(min(r),max(r)):
        childA.append(genB[i])
        childB.append(genA[i])
    for i in range(max(r),size):
        childA.append(genA[i])
        childB.append(genB[i])
    if len(genA)< len(genB):
        for i in range(size,len(genB)):
            childB.append(genB[i])
    if len(genA)> len(genB):
        for i in range(size,len(genA)):
            childA.append(genA[i])
    return [''.join(childA),''.join(childB)]

def mutate(gen):
    ngen = []
    for c in gen:
        if random.uniform(0,1) <= MUTATION_RATE:
            # mutate
            # 0.5 chances mutation
            # 0.25 chances addition/deletion
            if random.randint(1,2) == 1:
                ngen.append(random.choice(ALPHABET))
            elif random.randint(1,2) == 1:
                ngen.append(c)
                ngen.append(random.choice(ALPHABET))
        else:
            ngen.append(c)
    
    return ''.join(ngen)

def breed(genA, genB):
    (genA, genB) = breed_cs(genA, genB)
    while random.uniform(0,1) <= REBREEDING_CHANCE:
        (genA, genB) = breed_cs(genA, genB)
    if random.randint(1,2) == 1:
        return mutate(genA)
    else:
        return mutate(genB)