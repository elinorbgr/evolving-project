# Breeding

import random


def breed_cs(genA,genB):
    aCut = random.randint(0,len(genA))
    bCut = random.randint(0,len(genB))
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
    ind = []
    for i in range(2):
        ind.append(random.randint(0,len(gen)-1))

    gen = list(gen)
    gen[ind[0]],gen[ind[1]] = gen[ind[1]], gen[ind[0]]
    
    return ''.join(gen)

def breed(genA, genB):
    (genA, genB) = breed_cs(genA, genB)
    while random.randint(1,4) == 1:
        (genA, genB) = breed_cs(genA, genB)
    if random.randint(1,2) == 1:
        return mutate(genA)
    else:
        return mutate(genB)