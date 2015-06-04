import random

INPUT_AMPL_SUFFIX = "a"
INPUT_DIR_SUFFIX = "d"
OUTPUT_SUFFIX = "x"
INTERNAL_SUFFIX = "lmn"
NAME_LETTERS = "LMN"

NUMBERS = "0123"
BASE = 4

ALPHABET = "+-" + INPUT_DIR_SUFFIX + INPUT_AMPL_SUFFIX + OUTPUT_SUFFIX + INTERNAL_SUFFIX + NAME_LETTERS + NUMBERS

def random_genome(len):
    return ''.join(random.choice(ALPHABET) for _ in range(len))
