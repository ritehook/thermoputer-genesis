# core.py — Reversible gates + thermal memory + entropy core

import hashlib
from datetime import datetime

def reversible_gate(a, b):
    return a ^ b  # XOR as reversible logic

def thermal_memory(state, entropy):
    return (state + entropy) % 256  # entropy-aware memory cell

def entropy_encode(message):
    entropy = hashlib.sha256(message.encode()).hexdigest()
    return entropy

def timestamp_seal():
    return datetime.utcnow().isoformat() + "Z"

def emit_entropy_capsule(message):
    return {
        "capsule": "Entropy-Core.v2",
        "entropy": entropy_encode(message),
        "timestamp": timestamp_seal(),
        "validator": "PhiLock-Q",
        "status": "sealed"
    }
