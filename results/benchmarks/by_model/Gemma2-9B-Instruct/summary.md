# Gemma2-9B-Instruct

## Kết quả tổng hợp

| Method | ASR (%) | tinyArc (%) | tinyHellaswag (%) | tinyMMLU (%) | tinyTruthfulQA (%) | tinyWinogrande (%) | Avg (%) | TinyBench config |
|---|---|---|---|---|---|---|---|---|
| No Steering | — | 69.31 | 80.81 | 76.57 | 54.77 | 76.86 | 71.66 | — |
| ActAdd | 1.92 | 66.57 | 81.67 | 72.06 | 57.31 | 75.29 | 70.58 | K=1, PC=n/a, layer=44, alpha=1 |
| CHaRS AA | 1.92 | 66.57 | 81.67 | 72.06 | 57.29 | 75.29 | 70.58 | K=5, PC=n/a, layer=44, alpha=1 |
| CHaRS-PCT AA | 1.92 | 67.61 | 81.27 | 73.00 | 53.38 | 76.85 | 70.42 | K=5, PC=5, layer=44, alpha=1 |

## Kết quả TinyBench theo task/cấu hình (30 dòng)

| Family | Task | Config | Metric | Score (%) | N | Timestamp |
|---|---|---|---|---|---|---|
| actadd_proxy_chars_aa_k1 | tinyArc | k1_layer44_alpha1 | acc_norm,none | 66.57 | 100 | 2026-10-30T02-30-45.576952 |
| actadd_proxy_chars_aa_k1 | tinyHellaswag | k1_layer44_alpha1 | acc_norm,none | 81.67 | 100 | 2026-10-30T02-29-44.961175 |
| actadd_proxy_chars_aa_k1 | tinyMMLU | k1_layer44_alpha1 | acc_norm,none | 72.06 | 100 | 2026-10-30T02-32-16.143574 |
| actadd_proxy_chars_aa_k1 | tinyTruthfulQA | k1_layer44_alpha1 | acc,none | 57.31 | 100 | 2026-10-30T02-32-49.610386 |
| actadd_proxy_chars_aa_k1 | tinyWinogrande | k1_layer44_alpha1 | acc_norm,none | 75.29 | 100 | 2026-10-30T02-33-11.228788 |
| chars_aa | tinyArc | k1_layer44_alpha1 | acc_norm,none | 66.57 | 100 | 2026-10-30T02-30-45.576952 |
| chars_aa | tinyArc | k5_layer44_alpha1 | acc_norm,none | 66.57 | 100 | 2026-10-30T02-35-14.397309 |
| chars_aa | tinyHellaswag | k1_layer44_alpha1 | acc_norm,none | 81.67 | 100 | 2026-10-30T02-29-44.961175 |
| chars_aa | tinyHellaswag | k5_layer44_alpha1 | acc_norm,none | 81.67 | 100 | 2026-10-30T02-34-14.710068 |
| chars_aa | tinyMMLU | k1_layer44_alpha1 | acc_norm,none | 72.06 | 100 | 2026-10-30T02-32-16.143574 |
| chars_aa | tinyMMLU | k5_layer44_alpha1 | acc_norm,none | 72.06 | 100 | 2026-10-30T02-35-37.239479 |
| chars_aa | tinyTruthfulQA | k1_layer44_alpha1 | acc,none | 57.31 | 100 | 2026-10-30T02-32-49.610386 |
| chars_aa | tinyTruthfulQA | k5_layer44_alpha1 | acc,none | 57.29 | 100 | 2026-10-30T02-36-10.977534 |
| chars_aa | tinyWinogrande | k1_layer44_alpha1 | acc_norm,none | 75.29 | 100 | 2026-10-30T02-33-11.228788 |
| chars_aa | tinyWinogrande | k5_layer44_alpha1 | acc_norm,none | 75.29 | 100 | 2026-10-30T02-36-30.360214 |
| chars_pct_aa | tinyArc | k1_maxpc15_layer44_pc5_alpha1 | acc_norm,none | 67.61 | 100 | 2026-10-30T02-38-33.134186 |
| chars_pct_aa | tinyArc | k5_maxpc15_layer44_pc5_alpha1 | acc_norm,none | 67.61 | 100 | 2026-10-30T02-41-52.244168 |
| chars_pct_aa | tinyHellaswag | k1_maxpc15_layer44_pc5_alpha1 | acc_norm,none | 81.27 | 100 | 2026-10-30T02-37-33.811435 |
| chars_pct_aa | tinyHellaswag | k5_maxpc15_layer44_pc5_alpha1 | acc_norm,none | 81.27 | 100 | 2026-10-30T02-40-52.888286 |
| chars_pct_aa | tinyMMLU | k1_maxpc15_layer44_pc5_alpha1 | acc_norm,none | 73.00 | 100 | 2026-10-30T02-38-56.066460 |
| chars_pct_aa | tinyMMLU | k5_maxpc15_layer44_pc5_alpha1 | acc_norm,none | 73.00 | 100 | 2026-10-30T02-42-15.302277 |
| chars_pct_aa | tinyTruthfulQA | k1_maxpc15_layer44_pc5_alpha1 | acc,none | 53.38 | 100 | 2026-10-30T02-39-30.033490 |
| chars_pct_aa | tinyTruthfulQA | k5_maxpc15_layer44_pc5_alpha1 | acc,none | 53.38 | 100 | 2026-10-30T02-42-49.121026 |
| chars_pct_aa | tinyWinogrande | k1_maxpc15_layer44_pc5_alpha1 | acc_norm,none | 77.40 | 100 | 2026-10-30T02-39-49.043556 |
| chars_pct_aa | tinyWinogrande | k5_maxpc15_layer44_pc5_alpha1 | acc_norm,none | 76.85 | 100 | 2026-10-30T02-43-08.494790 |
| trad_baseline | tinyArc | baseline_user_provided | acc_norm,none | 69.31 | — | — |
| trad_baseline | tinyHellaswag | baseline_user_provided | acc_norm,none | 80.81 | — | — |
| trad_baseline | tinyMMLU | baseline_user_provided | acc_norm,none | 76.57 | — | — |
| trad_baseline | tinyTruthfulQA | baseline_user_provided | acc,none | 54.77 | — | — |
| trad_baseline | tinyWinogrande | baseline_user_provided | acc_norm,none | 76.86 | — | — |
