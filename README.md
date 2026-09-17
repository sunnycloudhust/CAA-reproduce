# Uncertainty-aware-ODESteer

Experiment comparing a causal language model with and without activation
steering using the Anthropic HH-RLHF preference dataset.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

The default command downloads `Anthropic/hh-rlhf`, learns a steering vector
from `chosen - rejected`, and evaluates Base LLM versus Activation Steering on
the same conversation prompts:

```bash
python -m src.steering_experiment
```

The default smoke test uses 64 contrast pairs and 16 evaluation prompts. Use
more data for a real experiment:

```bash
python -m src.steering_experiment \
	--model gpt2 \
	--layer 6 \
	--max-contrast 1000 \
	--max-eval 200 \
	--alpha 2.0 \
	--output-file results/hh_rlhf_gpt2_alpha2.jsonl
```

Sweep the steering coefficient with identical data and decoding settings:

```bash
for alpha in -2 -1 0 1 2; do
	python -m src.steering_experiment \
		--model gpt2 --layer 6 --alpha "$alpha" \
		--max-contrast 1000 --max-eval 200 \
		--output-file "results/hh_rlhf_alpha${alpha}.jsonl"
done
```

Outputs are written as JSONL to `results/`, with the prompt, model settings,
baseline generation, and steered generation on each line.

## Method

- **Base LLM**: greedy generation without an activation intervention.
- **Activation Steering**: adds `alpha * steering_vector` to the last-token
	hidden state at the selected transformer layer during generation.
- **Steering vector**: normalized mean of the hidden-state differences between
	each HH-RLHF `chosen` and `rejected` conversation.
- Evaluation prompts are extracted from the chosen conversation before the last
	`Assistant:` turn, so the model must generate the response itself.

