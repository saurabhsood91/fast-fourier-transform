import time
import matplotlib.pyplot as plt
import numpy as np
from main import *

if __name__ == "__main__":
    i = 2
    exec_times_dft = []
    N_vals = []
    n_2_vals = []
    while i <= 1024:
        N_vals.append(i)
        start_time = time.time()
        # create vector
        x = np.random.random(i)
        res = dft(x)
        exec_times_dft.append(time.time() - start_time)
        n_2_vals.append(0.0000002*(i**2))
        i *= 2
    # plt.semilogx(N_vals, exec_times_dft, 'g')
    # plt.semilogx(N_vals, n_2_vals, 'r')
    plt.plot(N_vals, exec_times_dft, 'g')
    plt.plot(N_vals, n_2_vals, 'r')
    plt.legend(["Execution Time for DFT", "0.0000002*n*log(n)"])
    plt.xlabel("Vector Length - N")
    plt.ylabel("Execution Time")
    plt.show()
