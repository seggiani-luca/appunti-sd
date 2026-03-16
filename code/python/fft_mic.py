import sounddevice as sd
import matplotlib.pyplot as plt
import fft
import math

# ---- sampling ----
samplerate = 11025
delta = 1 / samplerate 
window = 2 ** 12
half_window = window // 2

# ---- graph constants ----
times = [n * delta for n in range(window)]
freqs = [k / (window * delta) for k in range(half_window)]
notes = [
    ("A0", 27.5),
    ("A1", 55),
    ("A2", 110),
    ("A3", 220),
    ("A4", 440),
    ("A5", 880),
    ("A6", 1760),
    ("A7", 3520),
    ("A8", 7040)
]

# --- graph setup ----
plt.ion()
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(8,6))

def set_graphs():
    ax1.clear()
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Amplitude (V)")
    ax1.set_xlim(0, window * delta)
    ax1.set_ylim(-1.5, 1.5)
        
    ax2.clear()
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("Magnitude (dB)")
    ax2.set_xlim(20, samplerate / 2)
    ax2.set_ylim(-40, 80) 
    ax2.set_xscale("log")
    for name, f in notes:
        if 20 <= f <= samplerate / 2:
            ax2.axvline(f, color="gray", linewidth=0.5, alpha=0.3)
            ax2.text(f, 0.95, name, rotation=90, fontsize=7, 
                     transform=ax2.get_xaxis_transform(),
                     va='top', ha='center', alpha=0.7)    

    plt.tight_layout()

# ---- stream initialization ----
signal_buffer = [0] * window 

def audio_callback(indata, frames, time, status):
    global signal_buffer
    signal_buffer = indata[:,0].copy()

stream = sd.InputStream(channels=1, samplerate=samplerate, blocksize=window, callback=audio_callback)
stream.start()
print("Streaming... Press Ctrl+C to stop")

try:
    while True:
        # get last buffer
        signal = signal_buffer.copy()
        signal = fft.hann(signal)

        # calculate FFT
        spec = fft.fft(signal)
        spec = spec[:half_window]
        spec_mag = fft.db(spec)

        # update plots
        set_graphs()
        ax1.plot(times, signal)
        ax2.plot(freqs, spec_mag)

        plt.pause(0.001)
except KeyboardInterrupt:
    print("Stopped")
finally:
    stream.stop()
    stream.close()
