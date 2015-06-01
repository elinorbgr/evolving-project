import random

# ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-"
ALPHABET = "adlmnxLMN0123+-"

BASE = 4

def random_genome(len):
    return ''.join(random.choice(ALPHABET) for _ in xrange(len))