import cmath
import math

def fft(x):
    """
    Recursive implementation of the Cooley–Tukey FFT algorithm.
    Input:  x -> list of complex numbers (length must be power of 2)
    Output: list of complex numbers (FFT result)
    """
    N = len(x)
    if N <= 1:
        return x
    
    # Split even and odd elements
    even = fft(x[0::2])
    odd = fft(x[1::2])
    
    # Combine results
    result = [0] * N
    for k in range(N // 2):
        t = cmath.exp(-2j * math.pi * k / N) * odd[k]
        result[k] = even[k] + t
        result[k + N // 2] = even[k] - t
    
    return result


# Example usage
if __name__ == "__main__":
    # Sample signal (must be length = power of 2, e.g., 8)
    signal = [0, 1, 2, 3, 4, 3, 2, 1]
    fft_result = fft([complex(s, 0) for s in signal])

    print("FFT Result:")
    for r in fft_result:
        print(r)
