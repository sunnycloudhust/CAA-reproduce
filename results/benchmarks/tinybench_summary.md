# TinyBench: kết quả đồng bộ từ Hugging Face

Đã đồng bộ kết quả từ dataset `sunnycloudhust/CHaRS-activations`, gồm năm output CHaRS-PCT AA mới của Qwen2.5-3B (K=5, PC=5, layer=47, alpha=3; chạy ngày 2026-11-01). CSV ghi kết quả theo family/model/task/config; baseline và proxy ActAdd được đánh dấu riêng.

**Ô trống** nghĩa là chưa có output ở cấu hình đó. Baseline được lấy từ bảng người dùng cung cấp và không phụ thuộc steering config. ActAdd proxy là bản sao được đánh dấu của CHaRS AA K=1; đây không phải lần chạy ActAdd độc lập.

## Cấu hình đã chọn, đồng bộ mới nhất

Các dòng phản ánh cấu hình trong `final_result.csv`. PC, K, layer và alpha được khớp chính xác; ô — nghĩa là chưa có output TinyBench.

| Model | Method | Config | tinyArc | tinyHella | tinyMMLU | tinyTQA | tinyWino | Avg |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Gemma2-9B-Instruct | CHaRS AA | K=5, PC=n/a, layer=44, alpha=1 | 66.57 | 81.67 | 72.06 | 57.29 | 75.29 | 70.58 |
| Gemma2-9B-Instruct | CHaRS-PCT AA | K=5, PC=5, layer=44, alpha=1 | 67.61 | 81.27 | 73.00 | 53.38 | 76.85 | 70.42 |
| Llama3.1-8B-Instruct | CHaRS AA | K=5, PC=n/a, layer=25, alpha=4 | 34.67 | 38.15 | 27.42 | 46.60 | 51.81 | 39.73 |
| Llama3.1-8B-Instruct | CHaRS-PCT AA | K=5, PC=5, layer=25, alpha=4 | 34.67 | 38.15 | 27.42 | 46.62 | 51.81 | 39.73 |
| Llama3.2-3B-Instruct | CHaRS AA | K=5, PC=n/a, layer=28, alpha=3 | 31.60 | 41.12 | — | 46.10 | 62.17 | — |
| Llama3.2-3B-Instruct | CHaRS-PCT AA | K=5, PC=5, layer=28, alpha=3 | 31.60 | 42.67 | — | 46.19 | 62.17 | — |
| Qwen2.5-3B-Instruct | CHaRS AA | K=5, PC=n/a, layer=47, alpha=3 | 40.39 | 61.95 | 50.50 | 43.14 | 61.97 | 51.59 |
| Qwen2.5-3B-Instruct | CHaRS-PCT AA | K=5, PC=5, layer=47, alpha=3 | 40.39 | 61.95 | 50.50 | 43.14 | 61.97 | 51.59 |
| Qwen2.5-7B-Instruct | CHaRS AA | K=5, PC=n/a, layer=35, alpha=3.5 | 51.37 | 73.12 | 58.93 | 54.24 | 57.88 | 59.11 |
| Qwen2.5-7B-Instruct | CHaRS-PCT AA | K=5, PC=1, layer=35, alpha=3.5 | 51.37 | 73.12 | 58.93 | 54.33 | 57.88 | 59.13 |
| Qwen2.5-14B-Instruct | CHaRS AA | K=5, PC=n/a, layer=47, alpha=1 | 72.44 | 83.47 | 74.77 | 65.72 | 74.06 | 74.09 |
| Qwen2.5-14B-Instruct | CHaRS-PCT AA | K=5, PC=5, layer=47, alpha=1 | 72.44 | 83.47 | 74.77 | 65.72 | 74.06 | 74.09 |

Các ô thiếu còn lại được liệt kê trong `final_result.md`.
## Kết quả theo task và cấu hình

### tinyArc

| Model | K | alpha | Baseline | ActAdd (proxy CHaRS AA K=1) | CHaRS AA | CHaRS-PCT AA (PC=5) |
|---|---:|---:|---:|---:|---:|---:|
| Qwen2.5-3B-Instruct | 1 | 3 | 0.6282 | 0.4039 | 0.4039 | 0.4039 |
| Qwen2.5-3B-Instruct | 5 | 3 | 0.6282 |  | 0.4039 | 0.4039 |
| Qwen2.5-3B-Instruct | 10 | 3 | 0.6282 |  | 0.4039 |  |
| Qwen2.5-7B-Instruct | 1 | 2 | 0.6729 |  | 0.5783 |  |
| Qwen2.5-7B-Instruct | 1 | 3 | 0.6729 | 0.5573 | 0.5573 | 0.5573 |
| Qwen2.5-7B-Instruct | 1 | 4 | 0.6729 |  |  |  |
| Qwen2.5-7B-Instruct | 5 | 2 | 0.6729 |  | 0.5783 |  |
| Qwen2.5-7B-Instruct | 5 | 3 | 0.6729 |  | 0.5573 | 0.5573 |
| Qwen2.5-7B-Instruct | 5 | 4 | 0.6729 |  |  |  |
| Qwen2.5-7B-Instruct | 10 | 2 | 0.6729 |  | 0.5783 |  |
| Qwen2.5-7B-Instruct | 10 | 3 | 0.6729 |  | 0.5573 | 0.5573 |
| Qwen2.5-7B-Instruct | 10 | 4 | 0.6729 |  |  |  |
| Qwen2.5-14B-Instruct | 1 | 1 | 0.7396 | 0.7244 | 0.7244 | 0.7244 |
| Qwen2.5-14B-Instruct | 5 | 1 | 0.7396 |  | 0.7244 | 0.7244 |
| gemma-2-9b-it | 1 | 1 | 0.6931 | 0.6657 | 0.6657 | 0.6761 |
| gemma-2-9b-it | 5 | 1 | 0.6931 |  | 0.6657 | 0.6761 |
| Llama-3.1-8B-Instruct | 1 | 1 | 0.6533 |  | 0.6067 | 0.5880 |
| Llama-3.1-8B-Instruct | 1 | 3 | 0.6533 | 0.2971 | 0.2971 | 0.2971 |
| Llama-3.1-8B-Instruct | 5 | 1 | 0.6533 |  | 0.6021 | 0.6021 |
| Llama-3.1-8B-Instruct | 5 | 3 | 0.6533 |  | 0.2971 | 0.2971 |
| Llama-3.2-3B-Instruct | 1 | 3 | 0.5616 | 0.3160 | 0.3160 | 0.3160 |
| Llama-3.2-3B-Instruct | 5 | 3 | 0.5616 |  | 0.3160 | 0.3160 |
| Llama-3.2-3B-Instruct | 10 | 3 | 0.5616 |  | 0.3160 | 0.3160 |

### tinyHellaswag

| Model | K | alpha | Baseline | ActAdd (proxy CHaRS AA K=1) | CHaRS AA | CHaRS-PCT AA (PC=5) |
|---|---:|---:|---:|---:|---:|---:|
| Qwen2.5-3B-Instruct | 1 | 3 | 0.6990 | 0.6195 | 0.6195 | 0.6195 |
| Qwen2.5-3B-Instruct | 5 | 3 | 0.6990 |  | 0.6195 | 0.6195 |
| Qwen2.5-3B-Instruct | 10 | 3 | 0.6990 |  | 0.6195 |  |
| Qwen2.5-7B-Instruct | 1 | 2 | 0.7556 |  | 0.7393 |  |
| Qwen2.5-7B-Instruct | 1 | 3 | 0.7556 | 0.7338 | 0.7338 | 0.7338 |
| Qwen2.5-7B-Instruct | 1 | 4 | 0.7556 |  |  |  |
| Qwen2.5-7B-Instruct | 5 | 2 | 0.7556 |  | 0.7393 |  |
| Qwen2.5-7B-Instruct | 5 | 3 | 0.7556 |  | 0.7338 | 0.7338 |
| Qwen2.5-7B-Instruct | 5 | 4 | 0.7556 |  |  |  |
| Qwen2.5-7B-Instruct | 10 | 2 | 0.7556 |  | 0.7393 |  |
| Qwen2.5-7B-Instruct | 10 | 3 | 0.7556 |  | 0.7338 | 0.7338 |
| Qwen2.5-7B-Instruct | 10 | 4 | 0.7556 |  |  |  |
| Qwen2.5-14B-Instruct | 1 | 1 | 0.8271 | 0.8347 | 0.8347 | 0.8347 |
| Qwen2.5-14B-Instruct | 5 | 1 | 0.8271 |  | 0.8347 | 0.8347 |
| gemma-2-9b-it | 1 | 1 | 0.8081 | 0.8167 | 0.8167 | 0.8127 |
| gemma-2-9b-it | 5 | 1 | 0.8081 |  | 0.8167 | 0.8127 |
| Llama-3.1-8B-Instruct | 1 | 1 | 0.8140 |  | 0.8072 | 0.8072 |
| Llama-3.1-8B-Instruct | 1 | 3 | 0.8140 | 0.5506 | 0.5506 | 0.5506 |
| Llama-3.1-8B-Instruct | 5 | 1 | 0.8140 |  | 0.8072 | 0.8072 |
| Llama-3.1-8B-Instruct | 5 | 3 | 0.8140 |  | 0.5445 | 0.5412 |
| Llama-3.2-3B-Instruct | 1 | 3 | 0.7669 | 0.4267 | 0.4267 | 0.4267 |
| Llama-3.2-3B-Instruct | 5 | 3 | 0.7669 |  | 0.4112 | 0.4267 |
| Llama-3.2-3B-Instruct | 10 | 3 | 0.7669 |  | 0.4267 | 0.4267 |

### tinyMMLU

| Model | K | alpha | Baseline | ActAdd (proxy CHaRS AA K=1) | CHaRS AA | CHaRS-PCT AA (PC=5) |
|---|---:|---:|---:|---:|---:|---:|
| Qwen2.5-3B-Instruct | 1 | 3 | 0.6798 | 0.5050 | 0.5050 |  |
| Qwen2.5-3B-Instruct | 5 | 3 | 0.6798 |  | 0.5050 | 0.5050 |
| Qwen2.5-3B-Instruct | 10 | 3 | 0.6798 |  | 0.5050 |  |
| Qwen2.5-7B-Instruct | 1 | 2 | 0.7321 |  | 0.7072 |  |
| Qwen2.5-7B-Instruct | 1 | 3 | 0.7321 | 0.6319 | 0.6319 |  |
| Qwen2.5-7B-Instruct | 1 | 4 | 0.7321 |  | 0.4454 |  |
| Qwen2.5-7B-Instruct | 5 | 2 | 0.7321 |  | 0.7072 |  |
| Qwen2.5-7B-Instruct | 5 | 3 | 0.7321 |  | 0.6319 |  |
| Qwen2.5-7B-Instruct | 5 | 4 | 0.7321 |  | 0.4560 |  |
| Qwen2.5-7B-Instruct | 10 | 2 | 0.7321 |  | 0.7072 |  |
| Qwen2.5-7B-Instruct | 10 | 3 | 0.7321 |  | 0.6319 |  |
| Qwen2.5-7B-Instruct | 10 | 4 | 0.7321 |  | 0.4560 |  |
| Qwen2.5-14B-Instruct | 1 | 1 | 0.7531 | 0.7477 | 0.7477 | 0.7477 |
| Qwen2.5-14B-Instruct | 5 | 1 | 0.7531 |  | 0.7477 | 0.7477 |
| gemma-2-9b-it | 1 | 1 | 0.7657 | 0.7206 | 0.7206 | 0.7300 |
| gemma-2-9b-it | 5 | 1 | 0.7657 |  | 0.7206 | 0.7300 |
| Llama-3.1-8B-Instruct | 1 | 1 | 0.6290 |  | 0.6382 | 0.6382 |
| Llama-3.1-8B-Instruct | 1 | 3 | 0.6290 | 0.2900 | 0.2900 | 0.2900 |
| Llama-3.1-8B-Instruct | 5 | 1 | 0.6290 |  | 0.6350 | 0.6350 |
| Llama-3.1-8B-Instruct | 5 | 3 | 0.6290 |  | 0.2900 | 0.2900 |
| Llama-3.2-3B-Instruct | 1 | 3 | 0.6368 |  |  |  |
| Llama-3.2-3B-Instruct | 5 | 3 | 0.6368 |  |  |  |
| Llama-3.2-3B-Instruct | 10 | 3 | 0.6368 |  |  |  |

### tinyTruthfulQA

| Model | K | alpha | Baseline | ActAdd (proxy CHaRS AA K=1) | CHaRS AA | CHaRS-PCT AA (PC=5) |
|---|---:|---:|---:|---:|---:|---:|
| Qwen2.5-3B-Instruct | 1 | 3 | 0.5723 | 0.4315 | 0.4314 |  |
| Qwen2.5-3B-Instruct | 5 | 3 | 0.5723 |  | 0.4313 | 0.4314 |
| Qwen2.5-3B-Instruct | 10 | 3 | 0.5723 |  | 0.4312 |  |
| Qwen2.5-7B-Instruct | 1 | 2 | 0.5601 |  | 0.4991 |  |
| Qwen2.5-7B-Instruct | 1 | 3 | 0.5601 | 0.5164 | 0.5164 | 0.5164 |
| Qwen2.5-7B-Instruct | 1 | 4 | 0.5601 |  |  |  |
| Qwen2.5-7B-Instruct | 5 | 2 | 0.5601 |  | 0.4988 |  |
| Qwen2.5-7B-Instruct | 5 | 3 | 0.5601 |  | 0.5164 | 0.5163 |
| Qwen2.5-7B-Instruct | 5 | 4 | 0.5601 |  |  |  |
| Qwen2.5-7B-Instruct | 10 | 2 | 0.5601 |  | 0.4988 |  |
| Qwen2.5-7B-Instruct | 10 | 3 | 0.5601 |  | 0.5162 | 0.5164 |
| Qwen2.5-7B-Instruct | 10 | 4 | 0.5601 |  |  |  |
| Qwen2.5-14B-Instruct | 1 | 1 | 0.6524 | 0.6574 | 0.6574 | 0.6573 |
| Qwen2.5-14B-Instruct | 5 | 1 | 0.6524 |  | 0.6572 | 0.6572 |
| gemma-2-9b-it | 1 | 1 | 0.5477 | 0.5731 | 0.5731 | 0.5338 |
| gemma-2-9b-it | 5 | 1 | 0.5477 |  | 0.5729 | 0.5338 |
| Llama-3.1-8B-Instruct | 1 | 1 | 0.5443 |  | 0.5006 | 0.5007 |
| Llama-3.1-8B-Instruct | 1 | 3 | 0.5443 | 0.4491 | 0.4491 | 0.4492 |
| Llama-3.1-8B-Instruct | 5 | 1 | 0.5443 |  | 0.5006 | 0.5007 |
| Llama-3.1-8B-Instruct | 5 | 3 | 0.5443 |  | 0.4478 | 0.4477 |
| Llama-3.2-3B-Instruct | 1 | 3 | 0.5032 | 0.4623 | 0.4623 | 0.4628 |
| Llama-3.2-3B-Instruct | 5 | 3 | 0.5032 |  | 0.4610 | 0.4619 |
| Llama-3.2-3B-Instruct | 10 | 3 | 0.5032 |  | 0.4612 | 0.4620 |

### tinyWinogrande

| Model | K | alpha | Baseline | ActAdd (proxy CHaRS AA K=1) | CHaRS AA | CHaRS-PCT AA (PC=5) |
|---|---:|---:|---:|---:|---:|---:|
| Qwen2.5-3B-Instruct | 1 | 3 | 0.6590 | 0.6197 | 0.6197 |  |
| Qwen2.5-3B-Instruct | 5 | 3 | 0.6590 |  | 0.6197 | 0.6197 |
| Qwen2.5-3B-Instruct | 10 | 3 | 0.6590 |  | 0.6123 |  |
| Qwen2.5-7B-Instruct | 1 | 2 | 0.7426 |  | 0.6618 |  |
| Qwen2.5-7B-Instruct | 1 | 3 | 0.7426 | 0.5965 | 0.5965 | 0.5965 |
| Qwen2.5-7B-Instruct | 1 | 4 | 0.7426 |  |  |  |
| Qwen2.5-7B-Instruct | 5 | 2 | 0.7426 |  | 0.6618 |  |
| Qwen2.5-7B-Instruct | 5 | 3 | 0.7426 |  | 0.5965 | 0.5965 |
| Qwen2.5-7B-Instruct | 5 | 4 | 0.7426 |  |  |  |
| Qwen2.5-7B-Instruct | 10 | 2 | 0.7426 |  | 0.6544 |  |
| Qwen2.5-7B-Instruct | 10 | 3 | 0.7426 |  | 0.5965 | 0.5965 |
| Qwen2.5-7B-Instruct | 10 | 4 | 0.7426 |  |  |  |
| Qwen2.5-14B-Instruct | 1 | 1 | 0.7458 | 0.7406 | 0.7406 | 0.7406 |
| Qwen2.5-14B-Instruct | 5 | 1 | 0.7458 |  | 0.7406 | 0.7406 |
| gemma-2-9b-it | 1 | 1 | 0.7686 | 0.7529 | 0.7529 | 0.7740 |
| gemma-2-9b-it | 5 | 1 | 0.7686 |  | 0.7529 | 0.7685 |
| Llama-3.1-8B-Instruct | 1 | 1 | 0.7381 |  | 0.7471 | 0.7471 |
| Llama-3.1-8B-Instruct | 1 | 3 | 0.7381 | 0.6013 | 0.6013 | 0.5894 |
| Llama-3.1-8B-Instruct | 5 | 1 | 0.7381 |  | 0.7471 | 0.7471 |
| Llama-3.1-8B-Instruct | 5 | 3 | 0.7381 |  | 0.6013 | 0.6013 |
| Llama-3.2-3B-Instruct | 1 | 3 | 0.6156 | 0.6217 | 0.6217 | 0.6107 |
| Llama-3.2-3B-Instruct | 5 | 3 | 0.6156 |  | 0.6217 | 0.6217 |
| Llama-3.2-3B-Instruct | 10 | 3 | 0.6156 |  | 0.6216 | 0.6217 |

## Coverage

| Mode | Models with output | Score rows |
|---|---:|---:|
| Baseline (user-provided / benchmark output) | 6/6 | 35 |
| ActAdd (proxy CHaRS AA K=1) | 6/6 | 29 |
| CHaRS AA | 6/6 | 115 |
| CHaRS-PCT AA | 6/6 | 86 |

Nguồn output gốc đã đồng bộ nằm trong `benchmarks/chars_aa/` và `benchmarks/chars_pct_aa/`; baseline và proxy có provenance trong `benchmarks/tinybench_scores_latest.csv`.

