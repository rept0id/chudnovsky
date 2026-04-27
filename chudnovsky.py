import sys
from mpmath import mp, mpf

def _mpf_fixed_length(x: mpf, digits: int) -> mpf:
    mp.dps = digits*2
    return int(x * 10**digits) / mp.mpf(10**digits)

def chudnovsky(n: int) -> mpf:
    if n <= 0:
        raise ValueError("Error: <n> must be integer and greater than 0")

    n_rounding_correction = n + 1  # rounding error of last digit correction

    mp.dps = n*2

    # Start of : chudnovsky formula

    C = 426880 * mp.sqrt(10005)
    K = mp.mpf(6)
    M = mp.mpf(1)
    L = mp.mpf(13591409)
    X = mp.mpf(1)
    S = L

    for i in range(1, n_rounding_correction // 14 + 2):
        M = (K**3 - 16 * K) * M / (i**3)
        L += 545140134
        X *= -262537412640768000
        S += M * L / X
        K += 12

    pi = C / S

    # End of : chudnovsky formula

    pi = _mpf_fixed_length(pi, n)  # fixed length due to float and rounding error of last digit correction

    return pi

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python main.py <n>")

    try:
        n = int(sys.argv[1])
    except ValueError as err:
        sys.exit("Error: <n> must be an integer." + f" ({err})")

    try:
        pi = chudnovsky(n)
    except ValueError as err:
        sys.exit(f"{err}")

    print(pi)
