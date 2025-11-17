# drift.py — Sovereign grammar loader

def load_grammar(capsule_name):
    grammar = {
        "Entropy-Core.v2": "entropy/timestamp",
        "Thermoputer-Finality.v1": "invocation/finality",
        "Thermoputer-Continuum.v1": "drift/legacy"
    }
    return grammar.get(capsule_name, "unknown")
