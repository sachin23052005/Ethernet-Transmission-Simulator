import numpy as np

# -------- NRZ --------
def nrz_modulate(bits, spp=50):
    levels = [1 if b else -1 for b in bits]
    return np.repeat(levels, spp)

def nrz_demodulate(waveform, spp=50):
    nbits = len(waveform)//spp
    recovered = []
    for i in range(nbits):
        block = waveform[i*spp:(i+1)*spp]
        recovered.append(1 if np.median(block) > 0 else 0)
    return recovered

# -------- Manchester --------
def manchester_modulate(bits, spp=50):
    waveform = []
    for b in bits:
        if b == 1:
            waveform += [1]*int(spp/2) + [-1]*int(spp/2)
        else:
            waveform += [-1]*int(spp/2) + [1]*int(spp/2)
    return np.array(waveform)

def manchester_demodulate(waveform, spp=50):
    nbits = len(waveform)//spp
    recovered = []
    for i in range(nbits):
        block = waveform[i*spp:(i+1)*spp]
        first_half = np.mean(block[:spp//2])
        second_half = np.mean(block[spp//2:])
        recovered.append(1 if first_half > second_half else 0)
    return recovered

# -------- MLT-3 --------
def mlt3_modulate(bits, spp=50):
    levels = [0, 1, 0, -1]
    idx, current = 0, 0
    seq = []
    for b in bits:
        if b == 1:
            idx = (idx + 1) % len(levels)
            current = levels[idx]
        seq.append(current)
    return np.repeat(seq, spp)

def mlt3_demodulate(waveform, spp=50):
    nbits = len(waveform)//spp
    recovered, prev = [], None
    for i in range(nbits):
        block = waveform[i*spp:(i+1)*spp]
        level = np.median(block)
        if prev is None:
            recovered.append(0)
        else:
            recovered.append(1 if abs(level - prev) > 0.4 else 0)
        prev = level
    return recovered
