import numpy as np

def dft(x):
    # create M matrix
    N = len(x)
    M = np.fromfunction(lambda k, n: np.exp((-2j * np.pi * k * n) / N), (N, N), dtype=float)
    return np.dot(M, x)

def fft(x):
    N = len(x)
    # print N
    if N == 1:
        return x
    if N%2 > 0:
        raise ValueError("Size should be a power of 2")
    # elif N <= 32:
    #     return dft(x)
    else:
        even = fft(x[::2])
        odd = fft(x[1::2])

        M = np.exp((-2j * np.pi * np.arange(N) / N))
        return np.concatenate([even + M[:N/2] * odd, even + M[N/2:] * odd])
