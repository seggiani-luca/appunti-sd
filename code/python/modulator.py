import numpy as np
import matplotlib.pyplot as plt

FREQ = 5

# function
def rect(x):
    return np.where(np.abs(x) <= 1, 1, 0)

def modulate(func, freq, t):
    return func(t) * np.cos(2 * np.pi * freq * t)

# parameters
t = np.linspace(-10, 10, 400, endpoint=False)
signal = modulate(rect, FREQ, t) 

# fft
f = np.fft.fftfreq(len(signal), d=t[1]-t[0])
spectrum = np.fft.fft(signal)

# shift fft
f = np.fft.fftshift(f)
spectrum = np.fft.fftshift(spectrum)

# plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,6))

ax1.plot(t, signal)
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Amplitude")

ax2.plot(f, np.abs(spectrum))
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Magnitude")

plt.tight_layout()
plt.show()
plt.show()
