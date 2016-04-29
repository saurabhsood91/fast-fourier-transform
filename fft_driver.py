import time
import matplotlib.pyplot as plt
import numpy as np
from main import *

if __name__ == "__main__":
    i = 2
    exec_times_fft = []
    N_vals = []
    log_vals = []
    while i <= 1024*1024:
        start_time = time.time()
        N_vals.append(i)
        x = np.random.random(i)
        res = fft(x)
        exec_times_fft.append(time.time() - start_time)
        log_vals.append(0.0000007 * i * np.log(i))
        i *= 2
    # plt.semilogx(N_vals, log_vals)
    # plt.semilogx(N_vals, exec_times_fft)
    plt.plot(N_vals, log_vals)
    plt.plot(N_vals, exec_times_fft)
    plt.plot(N_vals, log_vals)
    plt.legend(["Execution Time for FFT", "0.0000007*n*log(n)"])
    plt.xlabel("Vector Length - N")
    plt.ylabel("Execution Time")
    plt.show()
