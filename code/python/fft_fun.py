import matplotlib.pyplot as plt
import fft
import cmath

# define function to run fft on
T = 1
def step(t):
    return 1 if t > 0 else 0
def func(t):
    return cmath.exp(-t / T) * step(t)  

# sample function
dt = 1 / 10
window = 2 ** 8
offs = window // 2
signal = [func((n - offs) * dt) for n in range(window)]
times = [(n - offs) * dt for n in range(window)]

# get fft
spec = fft.fft(signal)
spec = spec[window // 2:] + spec[:window // 2]

spec = [c if i % 2 == 0 else -c for i, c in enumerate(spec)]

spec_mag = [abs(c) for c in spec]
spec_arg = [cmath.phase(c) for c in spec]
# spec_arg = fft.unwrap(spec_arg)
freqs = [(k - offs) / (window * dt) for k in range(window)]

# plot time and frequency graphs
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8,6))

ax1.plot(times, signal)
ax1.set_xlabel("time (s)")
ax1.set_ylabel("amplitude")

ax2.plot(freqs, spec_mag)
ax2.set_xlabel("frequency (hz)")
ax2.set_ylabel("magnitude")

# ax3.plot(freqs, spec_arg)
ax3.plot(freqs, spec_arg)
ax3.set_xlabel("frequency (hz)")
ax3.set_ylabel("phase")

plt.tight_layout()
plt.show()
