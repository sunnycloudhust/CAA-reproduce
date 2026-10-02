#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Full form for generate_vectors.py:
#   python generate_vectors.py --layers <layers> --save_activations --use_base_model 
#           --model_size <7b> --behaviors <behavior> ...
# python generate_vectors.py --layers 0 13 18 25 --save_activations --model_size "7b" 
# python generate_vectors.py --layers 0 13 18 25 --model_size "7b" --use_base_model 


python normalize_vectors.py

# Full form for plot_activations.py:
#   python plot_activations.py --layers <layers> --use_base_model --model_size <7b> 
#           --behaviors <behavior> ...
python plot_activations.py --layers 0 13 18 25 --model_size "7b"


python analyze_vectors.py

# Full form for prompting_with_steering.py:
#   python prompting_with_steering.py --layers <layers> --multipliers <number> ... 
#           --behaviors <behavior> ... --type <ab|open_ended|truthful_qa|mmlu> 
#           --system_prompt <pos|neg> --override_vector <layer> 
#           --override_vector_model <model> --use_base_model --model_size <7b> 
#           --override_model_weights_path <path> --overwrite
python prompting_with_steering.py --layers 0 13 18 25 --multipliers -1 0 1 --type ab 
python prompting_with_steering.py --layers 0 13 18 25 --multipliers -1 0 1 --type ab --override_vector_model Llama-2-7b-hf
python prompting_with_steering.py --layers 0 13 18 25 --multipliers -1 0 1 --type ab --override_vector 13

python prompting_with_steering.py --layers 13 --multipliers -1 -0.5 0 0.5 1 --type ab

python prompting_with_steering.py --layers 13 --multipliers -1 -0.5 0 0.5 1 --type ab --system_prompt pos

python prompting_with_steering.py --layers 13 --multipliers -1 -0.5 0 0.5 1 --type ab --system_prompt neg

python prompting_with_steering.py --layers 13 --multipliers -2.0 -1.5 -1 0 1 1.5 2.0 --type open_ended

python prompting_with_steering.py --layers 13 --multipliers -2 -1 0 1 2 --type mmlu

python prompting_with_steering.py --layers 13 --multipliers -2 -1 0 1 2 --type truthful_qa --behaviors sycophancy

# Full form for plot_results.py:
#   python plot_results.py --layers <layers> --multipliers <number> ... --title <text> --behaviors <behavior> ... --type <ab|open_ended|truthful_qa|mmlu> --override_vector <layer> --override_vector_model <model> --use_base_model --model_size <7b> --override_weights <path> <path>
python plot_results.py --layers 0 13 18 25 --multipliers -1 1 --type ab 
python plot_results.py --layers 0 13 18 25 --multipliers -1 1 --type ab --override_vector_model Llama-2-7b-hf --title "CAA transfer from base to chat model"
python plot_results.py --layers 0 13 18 25 --multipliers -1 1 --type ab --override_vector 13 --title "CAA transfer from layer 13 vector to other layers"

python plot_results.py --layers 13 --multipliers -1 -0.5 0 0.5 1 --type ab --title "Layer 13 - Llama 2 7B Chat"

python plot_results.py --layers 13 --multipliers -2 -1 0 1 2 --type mmlu

python plot_results.py --layers 13 --multipliers -2 -1 0 1 2 --type truthful_qa --behaviors sycophancy

# Full form for scoring.py:
#   python scoring.py
python scoring.py

python plot_results.py --layers 13 --multipliers -1.5 -1 0 1 1.5 --type open_ended --title "Layer 13 - Llama 2 7B Chat"
