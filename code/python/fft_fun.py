import matplotlib.pyplot as plt
import fft
import math

# define function to run FFT on
def func(x):
    if x < 0 or x > 1:
        return 0
    return 1

# sample function
dt = 1 / 10
window = 2 ** 8
signal = [func(x * dt) for x in range(window)]
times = [n * dt for n in range(window)]

# get FFT
spec = fft.fft(signal)[:window // 2]
spec_mag = [abs(c) for c in spec]
freqs = [k / (window * dt) for k in range(window // 2)]

# plot time and frequency graphs
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,6))

ax1.plot(times, signal)
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Amplitude")

ax2.plot(freqs, spec_mag)
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Magnitude")

plt.tight_layout()
plt.show()
