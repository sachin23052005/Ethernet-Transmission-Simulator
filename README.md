# 🌐 Ethernet Transmission Simulator

> **Python | Computer Networks | 4B/5B Encoding | NRZ | Manchester | MLT-3 | AWGN | BER**

An educational **Ethernet transmission simulation system implemented in Python** that demonstrates how digital data can be converted into bits, encoded using **4B/5B**, transmitted using different line-coding schemes, affected by channel noise, and recovered at the receiver.

The simulator supports **NRZ, Manchester, and MLT-3 modulation**, introduces **Additive White Gaussian Noise (AWGN)** into the transmission channel, performs demodulation and 5B/4B decoding, reconstructs the original text, and calculates the resulting **Bit Error Rate (BER)**.

The project also provides graphical visualization of the transmission process using **Matplotlib** and a live sender-to-receiver animation using **Turtle**.

---

# 📌 Project Overview

Digital communication systems transmit information as signals over a communication channel.

In this project, a text message is treated as the data to be transmitted. The simulator models a simplified transmission pipeline consisting of:

```text
Text
  │
  ▼
Text → Binary Bits
  │
  ▼
4B/5B Encoding
  │
  ▼
Line Coding / Modulation
  │
  ├──────────────┐
  │              │
  ▼              ▼
 NRZ        Manchester
  │
  ▼
 MLT-3
  │
  ▼
AWGN Channel
  │
  ▼
Demodulation
  │
  ▼
5B/4B Decoding
  │
  ▼
Recovered Bits
  │
  ▼
Bits → Text
  │
  ▼
BER Calculation
```

The purpose of the project is to provide a practical understanding of the relationship between **data encoding, physical-layer signaling, channel noise, signal recovery, and transmission errors**.

---

# 🎯 Objectives

The main objectives of this project are:

1. Convert text data into binary representation.
2. Implement 4B/5B encoding.
3. Implement 5B/4B decoding.
4. Simulate different line-coding/modulation schemes.
5. Implement NRZ modulation and demodulation.
6. Implement Manchester modulation and demodulation.
7. Implement MLT-3 modulation and demodulation.
8. Simulate transmission through a noisy channel using AWGN.
9. Recover the transmitted bit stream at the receiver.
10. Convert the recovered bits back into text.
11. Calculate Bit Error Rate (BER).
12. Visualize the sender and receiver signals.
13. Provide a live sender-to-receiver transmission animation.

---

# 🏗️ System Architecture

The project is divided into four main layers:

```text
                    Ethernet Transmission Simulator
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
   Data Layer            Modulation Layer        Channel Layer
        │                      │                      │
   4B/5B Encoding       NRZ / Manchester /       AWGN Noise
   5B/4B Decoding              MLT-3                 │
        │                      │                  BER Analysis
        └──────────────┬───────┴──────────────────────┘
                       │
                       ▼
                 Visualization
                       │
              ┌────────┴────────┐
              ▼                 ▼
          Matplotlib          Turtle
```

---

# 📂 Project Structure

```text
Ethernet-Transmission-Simulator/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
└── ethernet_simulation/
    │
    ├── main.py
    ├── data_layer.py
    ├── modulation_layer.py
    ├── channel_layer.py
    ├── visualization.py
    └── data_source.py
```

### File Description

| File                  | Purpose                                           |
| --------------------- | ------------------------------------------------- |
| `main.py`             | Main program and complete transmission pipeline   |
| `data_layer.py`       | 4B/5B encoding, 5B/4B decoding and bit generation |
| `modulation_layer.py` | NRZ, Manchester and MLT-3 modulation/demodulation |
| `channel_layer.py`    | AWGN noise simulation and BER calculation         |
| `visualization.py`    | Matplotlib plots and Turtle animation             |
| `data_source.py`      | Reserved data-source module                       |
| `requirements.txt`    | Python dependencies                               |
| `README.md`           | Project documentation                             |
| `LICENSE`             | MIT License                                       |

---

# 🔄 Complete Transmission Pipeline

The complete system works through the following stages:

## Step 1 — User Input

The user enters a paragraph through the command line.

Example:

```text
Enter a paragraph to transmit: Hello Computer Networks
```

---

## Step 2 — Text to Binary

Each character is converted into its UTF-8 byte representation and then into 8-bit binary.

For example:

```text
A
```

is represented as:

```text
01000001
```

The complete text is converted into a list of binary values:

```text
[0, 1, 0, 0, 0, 0, 0, 1, ...]
```

---

# 🔢 Step 3 — 4B/5B Encoding

The binary stream is divided into groups of four bits.

Each 4-bit group is mapped to a corresponding 5-bit code using a predefined 4B/5B mapping table.

Example:

```text
4-bit input
    ↓
  0000
    ↓
4B/5B mapping
    ↓
  11110
```

The implementation contains mappings for all 16 possible 4-bit combinations.

```text
0000 → 11110
0001 → 01001
0010 → 10100
0011 → 10101
...
1111 → 11101
```

If the input length is not divisible by four, padding bits are added before encoding.

---

# 📡 Step 4 — Line Coding / Modulation

After 4B/5B encoding, the encoded bit stream is converted into a waveform.

The project supports three schemes:

```text
NRZ
Manchester
MLT-3
```

The selected encoding scheme is configured in `main.py`.

Example:

```python
encoding = "MLT3"
```

The available choices are:

```text
MLT3
NRZ
Manchester
```

---

# 📈 NRZ Modulation

In the implemented NRZ scheme:

```text
Bit 1 → +1
Bit 0 → -1
```

Each bit is repeated according to the configured samples-per-bit value.

The default value is:

```text
Samples Per Bit = 50
```

Conceptually:

```text
1 → +1 +1 +1 +1 ...
0 → -1 -1 -1 -1 ...
```

---

# 🔀 Manchester Modulation

Manchester encoding represents each bit using two signal levels.

The implementation uses:

```text
Bit 1 → +1 followed by -1
Bit 0 → -1 followed by +1
```

This produces a transition in the middle of every bit period.

Conceptually:

```text
1 → ────┐____
        │

0 → ____┌────
```

The receiver determines the transmitted bit by comparing the average signal level of the first and second halves of the bit period.

---

# 🔁 MLT-3 Modulation

The project also implements **MLT-3 modulation**.

The signal uses four levels:

```text
0 → 0
1 → +1
2 → 0
3 → -1
```

For a `1` bit, the signal moves to the next level in the sequence.

For a `0` bit, the current signal level is maintained.

Conceptually:

```text
0 → +1 → 0 → -1 → 0 → +1 → ...
```

The MLT-3 implementation therefore reduces the frequency of signal transitions compared with some simpler line-coding approaches.

---

# 🌊 Step 5 — AWGN Channel

After modulation, the waveform passes through a simulated communication channel.

The project uses **Additive White Gaussian Noise (AWGN)**.

The noise level is controlled using the **Signal-to-Noise Ratio (SNR)**.

The default configuration is:

```text
SNR = 20 dB
```

The channel calculates the signal power and uses the selected SNR to determine the noise power.

Conceptually:

```text
Transmitted Signal
       │
       ▼
   + AWGN Noise
       │
       ▼
Received Noisy Signal
```

This simulates imperfections that can occur during communication.

---

# 📥 Step 6 — Demodulation

At the receiver, the noisy waveform is processed using the corresponding demodulation method.

For example:

```text
MLT-3 waveform
      ↓
MLT-3 demodulator
      ↓
Recovered encoded bits
```

The same encoding scheme selected at the transmitter is used at the receiver.

---

# 🔓 Step 7 — 5B/4B Decoding

The recovered 5-bit groups are converted back into their original 4-bit representations.

```text
5-bit encoded data
       ↓
  5B/4B Decoder
       ↓
Original 4-bit groups
```

If an invalid 5-bit code is encountered, the decoder records a decoding error and substitutes:

```text
0000
```

for that group.

---

# 📝 Step 8 — Binary to Text

After decoding, the recovered binary stream is divided into groups of eight bits.

Each group is converted back into a byte and then decoded as UTF-8 text.

The receiver therefore attempts to reconstruct the original user message.

```text
Recovered Bits
      ↓
8-bit Groups
      ↓
Bytes
      ↓
UTF-8
      ↓
Recovered Text
```

---

# 📊 Step 9 — Bit Error Rate

The project calculates **Bit Error Rate (BER)** by comparing the original bit stream with the recovered bit stream.

The calculation is:

```text
BER = Number of Bit Errors / Number of Compared Bits
```

For example:

```text
Original:  10110101
Received:  10100101

Bit Errors = 1
Total Bits = 8

BER = 1 / 8
    = 0.125
```

The simulator reports:

```text
Bit errors: X
BER: 0.XXXX
Decode Errors: X
```

BER provides an indication of how successfully the data survived the simulated transmission channel.

---

# 📈 Visualization

The project provides two visualization approaches.

## Matplotlib Visualization

The `plot_results()` function generates a multi-panel visualization containing:

### Sender Side

* Original bits
* 4B/5B encoded bits
* Modulated waveform

### Receiver Side

* Noisy waveform
* Demodulated/decoded bits
* Original vs recovered bit comparison

Conceptually:

```text
┌─────────────────────┬─────────────────────┬─────────────────────┐
│ Original Bits       │ 4B/5B Encoded       │ Modulated Waveform  │
├─────────────────────┼─────────────────────┼─────────────────────┤
│ Noisy Waveform      │ Recovered Bits      │ Comparison          │
└─────────────────────┴─────────────────────┴─────────────────────┘
```

---

# 🖥️ Live Turtle Simulation

The project also includes a live animated visualization using Python's `turtle` module.

The simulation represents:

```text
Sender
  │
  │ Transmission
  ▼
Receiver
```

The animation displays:

* Transmission progress
* Current transmitted bit
* Sender waveform
* Receiver waveform
* Original text
* Recovered text
* Transmission completion status

The simulation is titled:

```text
LIVE SIMULATION - Ethernet 100Mbps MLT-3 Transmission
```

and visually demonstrates the movement of the signal between sender and receiver.

---

# ⚙️ Configuration

The main transmission parameters are configured in `main.py`.

### Samples Per Bit

```python
spp = 50
```

This controls how many waveform samples represent each encoded bit.

### Signal-to-Noise Ratio

```python
snr_db = 20
```

This controls the amount of AWGN added to the transmitted waveform.

### Encoding Scheme

```python
encoding = "MLT3"
```

Available options:

```python
encoding = "MLT3"
encoding = "NRZ"
encoding = "Manchester"
```

---

# 🛠️ Technologies Used

## Programming Language

* Python

## Libraries

* NumPy
* Matplotlib
* Turtle
* Time

## Networking / Communication Concepts

* Digital data representation
* 4B/5B encoding
* 5B/4B decoding
* NRZ line coding
* Manchester encoding
* MLT-3 encoding
* Modulation
* Demodulation
* AWGN channel
* Signal-to-Noise Ratio
* Bit Error Rate

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Ethernet-Transmission-Simulator.git
```

Navigate into the project:

```bash
cd Ethernet-Transmission-Simulator
```

---

## 2. Install Dependencies

Create a `requirements.txt` file containing:

```text
numpy
matplotlib
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

`Turtle` and `time` are part of Python's standard library and normally do not need to be installed separately.

---

# ▶️ Running the Project

Navigate to the simulation directory:

```bash
cd ethernet_simulation
```

Run:

```bash
python main.py
```

The program will ask:

```text
Enter a paragraph to transmit:
```

Enter any text.

The program then:

1. Converts the text to bits.
2. Encodes the bits using 4B/5B.
3. Modulates the encoded signal.
4. Adds AWGN noise.
5. Demodulates the received signal.
6. Performs 5B/4B decoding.
7. Reconstructs the text.
8. Calculates BER.
9. Displays signal visualizations.
10. Launches the sender/receiver animation.

---

# 🧪 Example Execution

Example input:

```text
Hello Computer Networks
```

The simulator displays information similar to:

```text
Original text converted to XXXX bits.

Encoding Scheme: MLT3

--- Sender Side ---

Original Text: Hello Computer Networks
First 64 Original Bits: [...]
First 64 Encoded Bits: [...]

--- Receiver Side ---

First 64 Demodulated Bits: [...]
First 64 Recovered Bits: [...]

Recovered Text: Hello Computer Networks

Bit errors: X
BER: 0.XXXX
Decode Errors: X
```

The exact results depend on the input data and the randomly generated AWGN noise.

---

# 🔬 Key Concepts Demonstrated

This project provides practical implementation of several Computer Networks and digital communication concepts.

### 1. Data Representation

Converting human-readable text into binary data.

### 2. Block Encoding

Using 4B/5B encoding to transform groups of four bits into five-bit code groups.

### 3. Line Coding

Representing digital bits as physical signal levels using:

* NRZ
* Manchester
* MLT-3

### 4. Signal Modulation

Converting digital data into a waveform representation.

### 5. Communication Channel

Simulating a noisy channel using AWGN.

### 6. Signal Recovery

Recovering digital bits from the received noisy waveform.

### 7. Error Detection

Comparing transmitted and recovered bits to calculate BER.

### 8. Data Reconstruction

Converting the recovered binary data back into the original text.

---

# 📊 Transmission Flow

The complete sender-to-receiver process can be summarized as:

```text
                 SENDER
                   │
                   ▼
              User Input
                   │
                   ▼
             Text → Bits
                   │
                   ▼
              4B/5B Encode
                   │
                   ▼
        ┌──────────────────────┐
        │ Line Coding          │
        │                      │
        │ NRZ                  │
        │ Manchester           │
        │ MLT-3                │
        └──────────┬───────────┘
                   │
                   ▼
              AWGN Channel
                   │
                   ▼
                RECEIVER
                   │
                   ▼
              Demodulation
                   │
                   ▼
              5B/4B Decode
                   │
                   ▼
             Bits → Text
                   │
                   ▼
             BER Analysis
```

---

# 💡 Design Decisions

## Modular Architecture

The project separates the major responsibilities into different Python modules:

```text
data_layer.py
       │
       ├── Encoding
       └── Decoding

modulation_layer.py
       │
       ├── NRZ
       ├── Manchester
       └── MLT-3

channel_layer.py
       │
       ├── AWGN
       └── BER

visualization.py
       │
       ├── Matplotlib
       └── Turtle

main.py
       │
       └── Complete Pipeline
```

This makes the simulator easier to understand and modify.

---

# ⚠️ Limitations

This project is an **educational simulation** rather than a complete implementation of a physical Ethernet system.

Some limitations include:

* The communication channel is simulated rather than connected to physical network hardware.
* AWGN is used as the channel-noise model.
* The implementation works with text input rather than actual Ethernet frames.
* Ethernet headers, MAC addressing, CRC, collision handling, and frame transmission are not implemented.
* The modulation and demodulation implementations are simplified for educational purposes.
* BER is calculated over the available compared bits.
* The current configuration uses a fixed SNR unless manually changed.
* The simulator focuses on the transmission/physical-layer concepts represented in the implementation.

---

# 🔮 Future Improvements

The project could be extended with additional networking functionality.

### Physical Layer

* Add configurable SNR experiments.
* Compare BER across different encoding schemes.
* Plot BER versus SNR.
* Add additional line-coding techniques.
* Analyze bandwidth requirements.

### Data Link Layer

* Implement Ethernet frame structure.
* Add MAC addresses.
* Add frame headers and trailers.
* Implement CRC/error detection.
* Simulate frame loss and retransmission.

### Network Layer

* Add IP addressing.
* Simulate packet forwarding.
* Implement routing algorithms.

### Performance Analysis

A useful future experiment would be comparing BER across different SNR values:

```text
SNR
 │
 │\
 │ \
 │  \
 │   \
 │    \
 └──────────────►
       BER
```

This would allow experimental analysis of how channel quality affects transmission reliability.

### Visualization

Future versions could include:

* Interactive SNR controls.
* Real-time BER graphs.
* Side-by-side comparison of NRZ, Manchester and MLT-3.
* Interactive waveform inspection.
* Transmission-speed controls.

---

# 🎓 Project Context

This project was developed as a **Computer Networks course project** to gain practical experience with digital data transmission, encoding, modulation, noisy communication channels, and error analysis.

The project focuses on understanding communication concepts by implementing a simplified end-to-end transmission system in Python.

---

# 📚 Learning Outcomes

Through this project, the following concepts were explored practically:

* Binary data representation
* 4B/5B encoding
* 5B/4B decoding
* NRZ signaling
* Manchester signaling
* MLT-3 signaling
* Modulation and demodulation
* Signal sampling
* AWGN noise
* Signal-to-Noise Ratio
* Bit Error Rate
* Sender/receiver architecture
* Digital signal visualization
* Python modular programming

---

# 👨‍💻 Author

**Sachin Anil Prasad**

Computer Science Engineering Student

Interests:

* Computer Networks
* Operating Systems
* Data Structures & Algorithms
* Artificial Intelligence
* Generative AI
* Machine Learning
* Cybersecurity

---

# 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for the complete license terms.

---

# ⚠️ Disclaimer

This project is intended for **educational purposes**.

It is a simplified simulation designed to demonstrate concepts related to digital communication and computer networks. It should not be considered a complete implementation of the Ethernet protocol or a replacement for real networking hardware and standards.
