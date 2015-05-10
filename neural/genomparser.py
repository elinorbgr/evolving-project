# Genom parsing

import string

class InvalidGenomeError:
    def __init__(self, char):
        self.char = char
    def __str__(self):
        return "Invalid char: {}".format(self.char)

def parse_genome(genome):
    declarations = []
    links = []
    id_1 = ""
    value_1 = 0
    id_2 = ""
    value_2 = 0
    state = 0 # 1 = parsing neuron, 2 = parsing first link, 3 = parsing second link
    for c in genome:
        if c in string.ascii_lowercase:
            if state == 1:
                id_1 += c
                declarations.append((id_1, value_1))
                state = 0
            else if state == 2:
                id_1 += c
                state = 3
            else if state = 3:
                id_2 += c
                links.append((id_1, value_1, id_2, value_2))
                state = 0
        else if c in string.ascii_uppercase:
            if state == 1 or state == 2:
                id_1 += c
            else if state == 3:
                id_2 += c
        else if c.is_digit():
            if state == 1 or state == 2:
                value_1 = 10 * value_1 + int(c)
            else if state == 3:
                value_2 = 10 * value_1 + int(c)
        else if c == '+':
            id_1 = ""
            value_1 = 0
            state = 1
        else if c == '-':
            id_1 = ""
            value_1 = 0
            id_2 = ""
            value_2 = 0
            state = 2
        else:
            raise InvalidGenomeError(c)
    return (declarations, links)