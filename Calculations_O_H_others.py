


from math import log10

data = [
    (10, 0.35, 0.003, 0.04, 0.06),
    (40, 0.22, 0.009, 0.065, 0.08),
    (100, 0.20, 0.012, 0.07, 0.07),
]

# Values of f for which we want to calculate O_H
fs = [1, 10, 50, 100, 200, 500, 1000]

# Iterating through each case in the data list
for entry in data:
    percentage, X_H, X_C, X_N, X_O = entry
    log_X_N_X_O = log10(X_N / X_O)
    log_X_C_X_O = log10(X_C / X_O)

    print(f"For {percentage}%:")
    print(f"log10(X_N/X_O) = {log_X_N_X_O:.4f}")
    print(f"log10(X_C/X_O) = {log_X_C_X_O:.4f}\n")

    # Calculating O_H for each value of f
    for f in fs:
        O_H = log10(X_O / ((X_H + 0.7516 * f)*16)) + 12.0
        print(f"For f = {f}, O_H = {O_H:.4f}")
    print("\n")
