# Generate steering vectors for selected layers.

python generate_vectors.py --layers 10 12 13 14 16 --save_activations --model_size "7b"
python generate_vectors.py --layers 10 12 13 14 16 --save_activations --model_size "7b" --use_base_model
