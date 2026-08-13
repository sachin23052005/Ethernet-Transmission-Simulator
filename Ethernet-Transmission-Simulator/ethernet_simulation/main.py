from data_layer import generate_bits, encode_4b5b, decode_5b4b
from modulation_layer import nrz_modulate, nrz_demodulate
from modulation_layer import manchester_modulate, manchester_demodulate
from modulation_layer import mlt3_modulate, mlt3_demodulate
from channel_layer import add_awgn, bit_error_rate
from visualization import plot_results, turtle_sender_receiver


# -------- Utility Functions for Text Conversion --------
def text_to_bits(text):
    """Convert text string into a list of bits."""
    bits = []
    for char in text.encode('utf-8'):
        bits.extend([int(b) for b in f"{char:08b}"])
    return bits


def bits_to_text(bits):
    """Convert bit list back into text."""
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        value = int(''.join(map(str, byte)), 2)
        chars.append(value)
    try:
        return bytes(chars).decode('utf-8', errors='ignore')
    except:
        return "<Decoding Error>"


# -------- Main Simulation --------
def main():
    # -------- Input from user --------
    paragraph = input("Enter a paragraph to transmit: ")

    # Convert text → bits
    bits = text_to_bits(paragraph)
    print(f"\nOriginal text converted to {len(bits)} bits.")

    # -------- Parameters --------
    spp = 50
    snr_db = 20
    encoding = "MLT3"   # Options: "MLT3", "NRZ", "Manchester"

    # -------- Sender Side --------
    encoded = encode_4b5b(bits)

    if encoding == "MLT3":
        waveform = mlt3_modulate(encoded, spp)
    elif encoding == "NRZ":
        waveform = nrz_modulate(encoded, spp)
    elif encoding == "Manchester":
        waveform = manchester_modulate(encoded, spp)
    else:
        raise ValueError("Invalid encoding type")

    # -------- Channel --------
    noisy = add_awgn(waveform, snr_db)

    # -------- Receiver Side --------
    if encoding == "MLT3":
        demod_bits = mlt3_demodulate(noisy, spp)
    elif encoding == "NRZ":
        demod_bits = nrz_demodulate(noisy, spp)
    elif encoding == "Manchester":
        demod_bits = manchester_demodulate(noisy, spp)

    recovered_bits, errors_decode = decode_5b4b(demod_bits)

    # -------- Convert Bits → Text --------
    recovered_text = bits_to_text(recovered_bits)

    # -------- BER Calculation --------
    ber, err = bit_error_rate(bits, recovered_bits[:len(bits)])

    # -------- Console Output --------
    print(f"\nEncoding Scheme: {encoding}")
    print("\n--- Sender Side ---")
    print(f"Original Text: {paragraph}")
    print("First 64 Original Bits:", bits[:64])
    print("First 64 Encoded Bits: ", encoded[:64])

    print("\n--- Receiver Side ---")
    print("First 64 Demodulated Bits:", demod_bits[:64])
    print("First 64 Recovered Bits:  ", recovered_bits[:64])
    print(f"\nRecovered Text: {recovered_text}")
    print(f"Bit errors: {err}, BER: {ber:.4f}, Decode Errors: {errors_decode}")

    # -------- Visualization --------
    plot_results(bits, encoded, waveform, recovered_bits, noisy_waveform=noisy)
    turtle_sender_receiver(encoded[:60], demod_bits[:60], original_text=paragraph, recovered_text=recovered_text)



if __name__ == "__main__":
    main()
