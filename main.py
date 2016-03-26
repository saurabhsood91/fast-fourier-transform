import numpy as np
import time
import matplotlib.pyplot as plt

def dft(x):
    # create M matrix
    N = len(x)
    M = np.fromfunction(lambda k, n: np.exp((-2j * np.pi * k * n) / N), (N, N), dtype=float)
    return np.dot(M, x)

def fft(x):
    N = len(x)
    print N
    if N%2 > 0:
        raise ValueError("Size should be a power of 2")
    elif N <= 32:
        return dft(x)
    else:
        even = fft(x[::2])
        odd = fft(x[1::2])

        M = np.exp((-2j * np.pi * np.arange(N) / N))
        return np.concatenate([even + M[:N/2] * odd, even + M[N/2:] * odd])

if __name__ == "__main__":
    i = 2
    exec_times_dft = []
    exec_times_fft = []
    N_vals = []
    while i <= 1024:
        N_vals.append(i)
        start_time = time.time()
        # create vector
        x = np.random.random(i)
        res = dft(x)
        exec_times_dft.append(time.time() - start_time)
        i *= 2
    i = 2
    while i <= 1024:
        start_time = time.time()
        x = np.random.random(i)
        res = fft(x)
        exec_times_fft.append(time.time() - start_time)
        i *= 2
    plt.plot(N_vals, exec_times_dft)
    plt.plot(N_vals, exec_times_fft)
    plt.show()
