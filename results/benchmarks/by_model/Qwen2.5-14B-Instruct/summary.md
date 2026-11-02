# Qwen2.5-14B-Instruct

## Kết quả tổng hợp

| Method | ASR (%) | tinyArc (%) | tinyHellaswag (%) | tinyMMLU (%) | tinyTruthfulQA (%) | tinyWinogrande (%) | Avg (%) | TinyBench config |
|---|---|---|---|---|---|---|---|---|
| No Steering | — | 73.96 | 82.71 | 75.31 | 65.24 | 74.58 | 74.36 | — |
| ActAdd | 86.54 | 72.44 | 83.47 | 74.77 | 65.74 | 74.06 | 74.10 | K=1, PC=n/a, layer=47, alpha=1 |
| CHaRS AA | 94.23 | 72.44 | 83.47 | 74.77 | 65.72 | 74.06 | 74.09 | K=5, PC=n/a, layer=47, alpha=1 |
| CHaRS-PCT AA | 89.42 | 72.44 | 83.47 | 74.77 | 65.72 | 74.06 | 74.09 | K=5, PC=5, layer=47, alpha=1 |

## Kết quả TinyBench theo task/cấu hình (30 dòng)

| Family | Task | Config | Metric | Score (%) | N | Timestamp |
|---|---|---|---|---|---|---|
| actadd_proxy_chars_aa_k1 | tinyArc | k1_layer47_alpha1 | acc_norm,none | 72.44 | 100 | 2026-10-30T02-51-35.236939 |
| actadd_proxy_chars_aa_k1 | tinyHellaswag | k1_layer47_alpha1 | acc_norm,none | 83.47 | 100 | 2026-10-30T02-50-24.607477 |
| actadd_proxy_chars_aa_k1 | tinyMMLU | k1_layer47_alpha1 | acc_norm,none | 74.77 | 100 | 2026-10-30T02-52-00.950849 |
| actadd_proxy_chars_aa_k1 | tinyTruthfulQA | k1_layer47_alpha1 | acc,none | 65.74 | 100 | 2026-10-30T02-52-37.599690 |
| actadd_proxy_chars_aa_k1 | tinyWinogrande | k1_layer47_alpha1 | acc_norm,none | 74.06 | 100 | 2026-10-30T02-52-56.560768 |
| chars_aa | tinyArc | k1_layer47_alpha1 | acc_norm,none | 72.44 | 100 | 2026-10-30T02-51-35.236939 |
| chars_aa | tinyArc | k5_layer47_alpha1 | acc_norm,none | 72.44 | 100 | 2026-10-30T02-55-21.446057 |
| chars_aa | tinyHellaswag | k1_layer47_alpha1 | acc_norm,none | 83.47 | 100 | 2026-10-30T02-50-24.607477 |
| chars_aa | tinyHellaswag | k5_layer47_alpha1 | acc_norm,none | 83.47 | 100 | 2026-10-30T02-54-10.729819 |
| chars_aa | tinyMMLU | k1_layer47_alpha1 | acc_norm,none | 74.77 | 100 | 2026-10-30T02-52-00.950849 |
| chars_aa | tinyMMLU | k5_layer47_alpha1 | acc_norm,none | 74.77 | 100 | 2026-10-30T02-55-47.156383 |
| chars_aa | tinyTruthfulQA | k1_layer47_alpha1 | acc,none | 65.74 | 100 | 2026-10-30T02-52-37.599690 |
| chars_aa | tinyTruthfulQA | k5_layer47_alpha1 | acc,none | 65.72 | 100 | 2026-10-30T02-56-23.083344 |
| chars_aa | tinyWinogrande | k1_layer47_alpha1 | acc_norm,none | 74.06 | 100 | 2026-10-30T02-52-56.560768 |
| chars_aa | tinyWinogrande | k5_layer47_alpha1 | acc_norm,none | 74.06 | 100 | 2026-10-30T02-56-42.040824 |
| chars_pct_aa | tinyArc | k1_maxpc15_layer47_pc5_alpha1 | acc_norm,none | 72.44 | 100 | 2026-10-30T02-59-06.633912 |
| chars_pct_aa | tinyArc | k5_maxpc15_layer47_pc5_alpha1 | acc_norm,none | 72.44 | 100 | 2026-10-30T03-02-52.640156 |
| chars_pct_aa | tinyHellaswag | k1_maxpc15_layer47_pc5_alpha1 | acc_norm,none | 83.47 | 100 | 2026-10-30T02-57-55.991983 |
| chars_pct_aa | tinyHellaswag | k5_maxpc15_layer47_pc5_alpha1 | acc_norm,none | 83.47 | 100 | 2026-10-30T03-01-41.899312 |
| chars_pct_aa | tinyMMLU | k1_maxpc15_layer47_pc5_alpha1 | acc_norm,none | 74.77 | 100 | 2026-10-30T02-59-32.423152 |
| chars_pct_aa | tinyMMLU | k5_maxpc15_layer47_pc5_alpha1 | acc_norm,none | 74.77 | 100 | 2026-10-30T03-03-18.357043 |
| chars_pct_aa | tinyTruthfulQA | k1_maxpc15_layer47_pc5_alpha1 | acc,none | 65.73 | 100 | 2026-10-30T03-00-08.290056 |
| chars_pct_aa | tinyTruthfulQA | k5_maxpc15_layer47_pc5_alpha1 | acc,none | 65.72 | 100 | 2026-10-30T03-03-53.997774 |
| chars_pct_aa | tinyWinogrande | k1_maxpc15_layer47_pc5_alpha1 | acc_norm,none | 74.06 | 100 | 2026-10-30T03-00-27.329025 |
| chars_pct_aa | tinyWinogrande | k5_maxpc15_layer47_pc5_alpha1 | acc_norm,none | 74.06 | 100 | 2026-10-30T03-04-12.982931 |
| trad_baseline | tinyArc | baseline_user_provided | acc_norm,none | 73.96 | — | — |
| trad_baseline | tinyHellaswag | baseline_user_provided | acc_norm,none | 82.71 | — | — |
| trad_baseline | tinyMMLU | baseline_user_provided | acc_norm,none | 75.31 | — | — |
| trad_baseline | tinyTruthfulQA | baseline_user_provided | acc,none | 65.24 | — | — |
| trad_baseline | tinyWinogrande | baseline_user_provided | acc_norm,none | 74.58 | — | — |
