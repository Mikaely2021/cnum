import math
import sys
from decimal import Decimal, getcontext

def exp_series(x, atol=0.0):
    """ Aproxima e^x pela série de Maclaurin com critério de parada numérico. """
    eps = sys.float_info.epsilon
    s = 1.0
    term = 1.0
    n = 0
    tol_abs = max(atol, eps)

    while True:
        n += 1
        term *= x / n
        s += term
        if abs(term) < eps * abs(s) or abs(term) < tol_abs:
            break
        if n > 10_000:
            break
    return s, n, term

def exp_limit(x, atol=0.0):
    eps =  sys.float_info.epsilon
    s = 1.0
    term = 1.0
    n = 0
    tol_abs = max(atol, eps)

    while True:
        n += 1
        term *= x / n
        s += term
        if abs(term) < eps * abs(s) or abs(term) < tol_abs:
            break
        if n > 10_000: # segurança contra loop infinito
            break
    return s, n, term


def exp_series_scaling(x, theta=1.0):
    if x == 0.0:
        return 1.0, 0, 0.0, 0
    k = max(0, math.ceil(math.log2(abs(x)/theta))) if abs(x) > theta else 0
    m = x / (2**k)

    em, n_terms, _ = exp_series(m)
    y = em
    for _ in range(k):
        y *= y

    return y, k, n_terms

def min_terms_for_tol(x, tol=1e-12):
    term = 1.0
    n = 0
    while abs(term) > tol:
        n += 1
        term *= x / n
    return n

def main():
    for val in [1.0, 5.0, -2.0]:
        approx, nterms, last = exp_series(val)
    print(f"x={val:+g} -> e^x ≈ {approx:.16g} (math.exp={math.exp(val):.16g}, termos={nterms})")

    for val in [10.0, -20.0]:
        y, k, n = exp_series_scaling(val, theta=1.0)
    print(f"x={val:+g} -> e^x ≈ {y:.6e} (math.exp={math.exp(val):.6e})  [k={k}, termos série(m)={n}]")

    for val in [1.0, 5.0, -2.0]:
        approx, nterms, last = exp_series_scaling(val)
        print(f"x={val:+g} -> e^x ≈ {approx:.16g} (math.exp={math.exp(val):.16g}, termos={nterms})")

    if __name__ == "__main__":
     main()