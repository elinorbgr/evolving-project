# Breeding

import random

from neural import ALPHABET

from conf import REBREEDING_CHANCE, MUTATION_RATE

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

def count_matches(str1, str2):
    matches = 0
    for (c1, c2) in zip(str1, str2):
        if c1 == c2:
            matches += 1
    return matches

def best_offset(genA, genB):
    best_offset = 0
    best_matches = 0
    for k in range(-len(genB)+1, len(genA)):
        matches = count_matches(
            genA[max(0, k):min(len(genA), len(genB)+k)],
            genB[max(0, -k):min(len(genB), len(genA)-k)]
        )
        if matches > best_matches:
            best_offset = k
            best_matches = matches
    return best_offset

def breed_aligned(genA, genB):
    offset = best_offset(genA, genB)
    k = random.randint(max(0, offset), min(len(genA), len(genB)+offset))
    return (genA[:k] + genB[k-offset:], genB[:k-offset] +genA[k:])

def breed(genA, genB):
    (genA, genB) = breed_cs(genA, genB)
    while random.uniform(0,1) <= REBREEDING_CHANCE:
        (genA, genB) = breed_aligned(genA, genB)
    if random.randint(1,2) == 1:
        return mutate(genA)
    else:
        return mutate(genB)