# core.py — Reversible gates + thermal memory

def reversible_gate(a, b):
    return a ^ b  # XOR as reversible logic

def thermal_memory(state, entropy):
    return (state + entropy) % 256  # simple entropy-aware memory cell
