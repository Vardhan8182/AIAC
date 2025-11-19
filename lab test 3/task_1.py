import time


"""
Fibonacci: tabulation (dynamic programming) vs naive recursion.
Computes and prints the first 15 Fibonacci numbers using tabulation,
implements a separate recursive Fibonacci, and compares runtimes.
"""



def fib_tab(n: int) -> int:
    """Return the n-th Fibonacci number (0-based) using tabulation."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    table = [0] * (n + 1)
    table[0], table[1] = 0, 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


def fib_tab_sequence(k: int) -> list:
    """Return the first k Fibonacci numbers (starting from F0) using tabulation."""
    if k <= 0:
        return []
    if k == 1:
        return [0]
    seq = [0] * k
    seq[0], seq[1] = 0, 1
    for i in range(2, k):
        seq[i] = seq[i - 1] + seq[i - 2]
    return seq


def fib_rec(n: int) -> int:
    """Naive recursive Fibonacci (0-based)."""
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


if __name__ == "__main__":
    # 1) Compute and print the first 15 Fibonacci numbers using tabulation
    first_15 = fib_tab_sequence(15)
    print("First 15 Fibonacci numbers (F0 ... F14) using tabulation:")
    print(first_15)

    # 2) Compare runtimes of tabulation vs recursion for a chosen n
    n_test = 35  # adjust this to see larger/smaller differences

    t0 = time.perf_counter()
    tab_value = fib_tab(n_test)
    t_tab = time.perf_counter() - t0

    t0 = time.perf_counter()
    rec_value = fib_rec(n_test)
    t_rec = time.perf_counter() - t0

    print(f"\nComputed F{n_test} with tabulation: {tab_value}")
    print(f"Computed F{n_test} with recursion:  {rec_value}")

    print("\nRuntimes:")
    print(f"Tabulation time: {t_tab:.6f} seconds")
    print(f"Recursive time:  {t_rec:.6f} seconds")