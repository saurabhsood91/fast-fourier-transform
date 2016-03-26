import numpy as np

def dft(x):
    # create M matrix
    N = len(x)
    M = np.fromfunction(lambda k, n: np.exp((-2j * np.pi * k * n) / N), (N, N), dtype=float)
    return np.dot(M, x)

if __name__ == "__main__":
    i = 2
    while i <= 1024:
        # create vector
        x = np.random.random(i)
        res = dft(x)
        i *= 2
