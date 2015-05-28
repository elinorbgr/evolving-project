import random

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-"

def random_genome(len):
    return ''.join(random.choice(ALPHABET) for _ in xrange(len))