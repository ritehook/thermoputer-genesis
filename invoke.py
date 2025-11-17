
# invoke.py — Thermoputer Capsule Invocation Engine

import sys
import json
from datetime import datetime

def emit_capsule(message):
    capsule = {
        "capsule": "Thermoputer-Invocation.v1",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "lineage_hash": "0xPHILOCKQ_THERMOPUTER_GENESIS_FINALITY",
        "validator": "PhiLock-Q",
        "message": message,
        "status": "sealed"
    }
    print(json.dumps(capsule, indent=2))

if __name__ == "__main__":
    if "--mythic" in sys.argv:
        try:
            idx = sys.argv.index("--mythic")
            message = sys.argv[idx + 1]
            emit_capsule(message)
        except IndexError:
            print("Error: No message provided after --mythic")
    else:
        print("Usage: python invoke.py --mythic \"Your sovereign message here\"")

