import numpy as np
import time
import matplotlib.pyplot as plt

def dft(x):
    # create M matrix
    N = len(x)
    M = np.fromfunction(lambda k, n: np.exp((-2j * np.pi * k * n) / N), (N, N), dtype=float)
    return np.dot(M, x)

if __name__ == "__main__":
    i = 2
    exec_times = []
    N_vals = []
    while i <= 1024:
        N_vals.append(i)
        start_time = time.time()
        # create vector
        x = np.random.random(i)
        res = dft(x)
        exec_times.append(time.time() - start_time)
        i *= 2
    plt.plot(N_vals, exec_times)
    plt.show()
