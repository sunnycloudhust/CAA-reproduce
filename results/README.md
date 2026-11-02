# Kết quả thực nghiệm

## CHaRS benchmarks

Nguồn: dataset Hugging Face `sunnycloudhust/CHaRS-activations`, revision `919480a08b5f5a46f90d04540ab4886f3d23ea3d`. Bảng được dựng từ `benchmarks/final_result.csv`; các điểm TinyBench theo task/cấu hình nằm trong từng CSV của model.

- [Bảng nguồn CSV](benchmarks/final_result.csv)
- [Bảng nguồn Markdown](benchmarks/final_result.md)
- [Điểm TinyBench đầy đủ](benchmarks/tinybench_scores_latest.csv)
- [Bảng chi tiết theo model, task và config](benchmarks/by_model/README.md)

## Các kết quả khác

- [Tổng hợp TruthfulQA và Ultrafeedback](TONG_HOP_KET_QUA.md)

## Gemma2-9B-Instruct

| Method | ASR (%) | tinyArc | tinyHella | tinyMMLU | tinyTQA | tinyWino | Avg (%) | Config |
|---|---|---|---|---|---|---|---|---|
| No Steering | — | 69.31 | 80.81 | 76.57 | 54.77 | 76.86 | 71.66 | — |
| ActAdd | 1.92 | 66.57 | 81.67 | 72.06 | 57.31 | 75.29 | 70.58 | K=1, PC=n/a, L=44, α=1 |
| CHaRS AA | 1.92 | 66.57 | 81.67 | 72.06 | 57.29 | 75.29 | 70.58 | K=5, PC=n/a, L=44, α=1 |
| CHaRS-PCT AA | 1.92 | 67.61 | 81.27 | 73.00 | 53.38 | 76.85 | 70.42 | K=5, PC=5, L=44, α=1 |

[Bảng đầy đủ theo task/config (30 dòng)](benchmarks/by_model/Gemma2-9B-Instruct/summary.md) · [CSV](benchmarks/by_model/Gemma2-9B-Instruct/summary.csv) · [Điểm chi tiết](benchmarks/by_model/Gemma2-9B-Instruct/tinybench_scores.csv)

## Llama3.1-8B-Instruct

| Method | ASR (%) | tinyArc | tinyHella | tinyMMLU | tinyTQA | tinyWino | Avg (%) | Config |
|---|---|---|---|---|---|---|---|---|
| No Steering | — | 65.33 | 81.40 | 62.90 | 54.43 | 73.81 | 67.57 | — |
| ActAdd | 89.42 | 29.71 | 55.06 | 29.00 | 44.91 | 60.13 | 43.76 | K=1, PC=n/a, L=25, α=3 |
| CHaRS AA | 93.27 | 34.67 | 38.15 | 27.42 | 46.60 | 51.81 | 39.73 | K=5, PC=n/a, L=25, α=4 |
| CHaRS-PCT AA | 95.19 | 34.67 | 38.15 | 27.42 | 46.62 | 51.81 | 39.73 | K=5, PC=5, L=25, α=4 |

[Bảng đầy đủ theo task/config (60 dòng)](benchmarks/by_model/Llama3.1-8B-Instruct/summary.md) · [CSV](benchmarks/by_model/Llama3.1-8B-Instruct/summary.csv) · [Điểm chi tiết](benchmarks/by_model/Llama3.1-8B-Instruct/tinybench_scores.csv)

## Llama3.2-3B-Instruct

| Method | ASR (%) | tinyArc | tinyHella | tinyMMLU | tinyTQA | tinyWino | Avg (%) | Config |
|---|---|---|---|---|---|---|---|---|
| No Steering | — | 56.16 | 76.69 | 63.68 | 50.32 | 61.56 | 61.68 | — |
| ActAdd | 91.35 | 31.60 | 42.67 | — | 46.23 | 62.17 | — | K=1, PC=n/a, L=28, α=3 |
| CHaRS AA | 92.31 | 31.60 | 41.12 | — | 46.10 | 62.17 | — | K=5, PC=n/a, L=28, α=3 |
| CHaRS-PCT AA | 90.38 | 31.60 | 42.67 | — | 46.19 | 62.17 | — | K=5, PC=5, L=28, α=3 |

[Bảng đầy đủ theo task/config (43 dòng)](benchmarks/by_model/Llama3.2-3B-Instruct/summary.md) · [CSV](benchmarks/by_model/Llama3.2-3B-Instruct/summary.csv) · [Điểm chi tiết](benchmarks/by_model/Llama3.2-3B-Instruct/tinybench_scores.csv)

## Qwen2.5-14B-Instruct

| Method | ASR (%) | tinyArc | tinyHella | tinyMMLU | tinyTQA | tinyWino | Avg (%) | Config |
|---|---|---|---|---|---|---|---|---|
| No Steering | — | 73.96 | 82.71 | 75.31 | 65.24 | 74.58 | 74.36 | — |
| ActAdd | 86.54 | 72.44 | 83.47 | 74.77 | 65.74 | 74.06 | 74.10 | K=1, PC=n/a, L=47, α=1 |
| CHaRS AA | 94.23 | 72.44 | 83.47 | 74.77 | 65.72 | 74.06 | 74.09 | K=5, PC=n/a, L=47, α=1 |
| CHaRS-PCT AA | 89.42 | 72.44 | 83.47 | 74.77 | 65.72 | 74.06 | 74.09 | K=5, PC=5, L=47, α=1 |

[Bảng đầy đủ theo task/config (30 dòng)](benchmarks/by_model/Qwen2.5-14B-Instruct/summary.md) · [CSV](benchmarks/by_model/Qwen2.5-14B-Instruct/summary.csv) · [Điểm chi tiết](benchmarks/by_model/Qwen2.5-14B-Instruct/tinybench_scores.csv)

## Qwen2.5-3B-Instruct

| Method | ASR (%) | tinyArc | tinyHella | tinyMMLU | tinyTQA | tinyWino | Avg (%) | Config |
|---|---|---|---|---|---|---|---|---|
| No Steering | — | 62.82 | 69.90 | 67.98 | 57.23 | 65.90 | 64.77 | — |
| ActAdd | 97.12 | 40.39 | 61.95 | 50.50 | 43.15 | 61.97 | 51.59 | K=1, PC=n/a, L=47, α=3 |
| CHaRS AA | 97.12 | 40.39 | 61.95 | 50.50 | 43.14 | 61.97 | 51.59 | K=5, PC=n/a, L=47, α=3 |
| CHaRS-PCT AA | 98.08 | 40.39 | 61.95 | 50.50 | 43.14 | 61.97 | 51.59 | K=5, PC=5, L=47, α=3 |

[Bảng đầy đủ theo task/config (37 dòng)](benchmarks/by_model/Qwen2.5-3B-Instruct/summary.md) · [CSV](benchmarks/by_model/Qwen2.5-3B-Instruct/summary.csv) · [Điểm chi tiết](benchmarks/by_model/Qwen2.5-3B-Instruct/tinybench_scores.csv)

## Qwen2.5-7B-Instruct

| Method | ASR (%) | tinyArc | tinyHella | tinyMMLU | tinyTQA | tinyWino | Avg (%) | Config |
|---|---|---|---|---|---|---|---|---|
| No Steering | — | 67.29 | 75.56 | 73.21 | 56.01 | 74.26 | 69.27 | — |
| ActAdd | 92.31 | 55.73 | 73.38 | 63.19 | 51.64 | 59.65 | 60.72 | K=1, PC=n/a, L=35, α=3 |
| CHaRS AA | 97.12 | 51.37 | 73.12 | 58.93 | 54.24 | 57.88 | 59.11 | K=5, PC=n/a, L=35, α=3.5 |
| CHaRS-PCT AA | 97.12 | 51.37 | 73.12 | 58.93 | 54.33 | 57.88 | 59.13 | K=5, PC=1, L=35, α=3.5 |

[Bảng đầy đủ theo task/config (65 dòng)](benchmarks/by_model/Qwen2.5-7B-Instruct/summary.md) · [CSV](benchmarks/by_model/Qwen2.5-7B-Instruct/summary.csv) · [Điểm chi tiết](benchmarks/by_model/Qwen2.5-7B-Instruct/tinybench_scores.csv)
