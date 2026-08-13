import matplotlib.pyplot as plt
import turtle
import time

# -------- Matplotlib --------
def plot_results(original, encoded, waveform, recovered, noisy_waveform=None, spp=50):
    fig, axs = plt.subplots(2, 3, figsize=(15, 8))

    # ---- Sender Side ----
    axs[0,0].step(range(len(original)), original, where='post')
    axs[0,0].set_title("Sender: Original Bits")
    axs[0,1].step(range(len(encoded)), encoded, where='post')
    axs[0,1].set_title("Sender: 4B/5B Encoded")
    axs[0,2].plot(waveform[:spp*50])
    axs[0,2].set_title("Sender: Modulated Waveform")

    # ---- Receiver Side ----
    if noisy_waveform is not None:
        axs[1,0].plot(noisy_waveform[:spp*50])
        axs[1,0].set_title("Receiver: Noisy Waveform")
    else:
        axs[1,0].plot(waveform[:spp*50])
        axs[1,0].set_title("Receiver: Received Waveform")

    axs[1,1].step(range(len(recovered)), recovered, where='post')
    axs[1,1].set_title("Receiver: Demodulated / Decoded Bits")
    axs[1,2].step(range(len(original)), original, where='post', label="Original")
    axs[1,2].step(range(len(recovered)), recovered, where='post', linestyle='--', label="Recovered")
    axs[1,2].set_title("Receiver: Comparison")
    axs[1,2].legend()

    plt.tight_layout()
    plt.show()

# -------- Turtle Live Animation --------
def turtle_sender_receiver(bits, recovered, original_text="", recovered_text=""):
    wn = turtle.Screen()
    wn.title("Ethernet Live Simulation: Sender ↔ Receiver")
    wn.bgcolor("black")
    wn.setup(width=1200, height=700)

    # ---- Label ----
    title = turtle.Turtle()
    title.hideturtle()
    title.color("white")
    title.penup()
    title.goto(0, 300)
    title.write("LIVE SIMULATION - Ethernet 100Mbps MLT-3 Transmission", align="center", font=("Courier", 16, "bold"))

    # ---- Sender Setup ----
    sender = turtle.Turtle()
    sender.color("cyan")
    sender.width(3)
    sender.speed(0)
    sender.penup()
    sender.goto(-550, 150)
    sender.pendown()

    # ---- Receiver Setup ----
    receiver = turtle.Turtle()
    receiver.color("orange")
    receiver.width(3)
    receiver.speed(0)
    receiver.penup()
    receiver.goto(-550, -150)
    receiver.pendown()

    # ---- Text Labels ----
    text_writer = turtle.Turtle()
    text_writer.hideturtle()
    text_writer.color("white")
    text_writer.penup()
    text_writer.goto(-500, 230)

    recv_text_writer = turtle.Turtle()
    recv_text_writer.hideturtle()
    recv_text_writer.color("white")
    recv_text_writer.penup()
    recv_text_writer.goto(-500, -50)

    # ---- Transmission Logic ----
    step = 25
    levels = [0, 50, 0, -50]  # MLT-3 Levels
    idx_s, level_s = 0, 0
    idx_r, level_r = 0, 0
    x_s, x_r = -550, -550

    text_writer.write(f"Sending: {original_text[:50]}...", font=("Courier", 14, "bold"))
    recv_text_writer.write("Receiving...", font=("Courier", 14, "bold"))

    for i, bit in enumerate(bits):
        # ---- Sender Movement ----
        if bit == 1:
            idx_s = (idx_s + 1) % len(levels)
            level_s = levels[idx_s]
        sender.goto(x_s + step, 150 + level_s)
        x_s += step

        # ---- Receiver Movement ----
        if i < len(recovered):
            if recovered[i] == 1:
                idx_r = (idx_r + 1) % len(levels)
                level_r = levels[idx_r]
            receiver.goto(x_r + step, -150 + level_r)
            x_r += step

        # Live bit update on screen
        title.clear()
        title.write(f"Transmitting bit {i+1}/{len(bits)} → {bit}", align="center", font=("Courier", 16, "bold"))
        time.sleep(0.1)

    # ---- Final Output ----
    title.clear()
    title.write("Transmission Complete ✅", align="center", font=("Courier", 16, "bold"))
    recv_text_writer.clear()
    recv_text_writer.write(f"Recovered Text: {recovered_text[:60]}...", font=("Courier", 14, "bold"))

    wn.mainloop()