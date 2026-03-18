import cmath

def hann(x):
    ln = len(x)
    def weight(n):
        return 0.5 - 0.5 * cmath.cos(2 * cmath.pi * n / (ln - 1))

    return [y * weight(n) for n, y in enumerate(x)]

def db(x):
    return [20 * cmath.log10(abs(y) + 1e-12) for y in x]

def unwrap(x):
    def unwrap_single(c):
        while c > 3.1:
            c -= 2 * cmath.pi
        while c < -3.1:
            c += 2 * cmath.pi
        return c
    return [unwrap_single(c) for c in x]

def fft(x):
    ln = len(x)
    hln = ln // 2

    if ln == 1:
        # base case 
        return x
    else:
        # calculate even/odd FFTs
        even = fft(x[0::2])
        odd  = fft(x[1::2])

        # merge even/odd FFTS in result
        res = [None] * ln 
        for k in range(0, hln):
            twid = cmath.exp(-2j * cmath.pi * k / ln)
            res[k]       = even[k] + twid * odd[k] 
            res[k + hln] = even[k] - twid * odd[k] 
        return res
