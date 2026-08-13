import numpy as np

def add_awgn(waveform, snr_db):
    sig_power = np.mean(waveform**2)
    snr_lin = 10**(snr_db/10)
    noise_power = sig_power/snr_lin
    noise = np.random.normal(scale=np.sqrt(noise_power), size=waveform.shape)
    return waveform + noise


def bit_error_rate(original, recovered):
    L = min(len(original), len(recovered))
    errors = sum(1 for i in range(L) if original[i] != recovered[i])
    return errors/L if L>0 else 0, errors
