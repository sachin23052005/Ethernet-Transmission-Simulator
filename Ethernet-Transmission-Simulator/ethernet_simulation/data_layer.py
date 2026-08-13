import numpy as np

MAP_4B5B = {
    '0000': '11110', '0001': '01001', '0010': '10100', '0011': '10101',
    '0100': '01010', '0101': '01011', '0110': '01110', '0111': '01111',
    '1000': '10010', '1001': '10011', '1010': '10110', '1011': '10111',
    '1100': '11010', '1101': '11011', '1110': '11100', '1111': '11101'
}
MAP_5B4B = {v: k for k, v in MAP_4B5B.items()}


def generate_bits(n=100):
    return np.random.randint(0, 2, n).tolist()


def encode_4b5b(bits):
    pad = (-len(bits)) % 4
    bits_padded = bits + [0] * pad
    encoded = []
    for i in range(0, len(bits_padded), 4):
        nibble = ''.join(map(str, bits_padded[i:i+4]))
        encoded += list(map(int, MAP_4B5B[nibble]))
    return encoded


def decode_5b4b(bits):
    pad = (-len(bits)) % 5
    bits_padded = bits + [0] * pad
    decoded, errors = [], 0
    for i in range(0, len(bits_padded), 5):
        chunk = ''.join(map(str, bits_padded[i:i+5]))
        if chunk in MAP_5B4B:
            decoded += list(map(int, MAP_5B4B[chunk]))
        else:
            decoded += [0,0,0,0]
            errors += 1
    return decoded, errors
