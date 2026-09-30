#!/usr/bin/env bash

set -euo pipefail

# Make relative project paths work no matter where this script is launched from.
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Generate steering vectors for selected layers.

python3 generate_vectors.py --layers 10 12 13 14 16 --save_activations --model_size "7b"
python3 generate_vectors.py --layers 10 12 13 14 16 --save_activations --model_size "7b" --use_base_model
