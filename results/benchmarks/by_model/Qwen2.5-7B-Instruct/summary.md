# Qwen2.5-7B-Instruct

## Kết quả tổng hợp

| Method | ASR (%) | tinyArc (%) | tinyHellaswag (%) | tinyMMLU (%) | tinyTruthfulQA (%) | tinyWinogrande (%) | Avg (%) | TinyBench config |
|---|---|---|---|---|---|---|---|---|
| No Steering | — | 67.29 | 75.56 | 73.21 | 56.01 | 74.26 | 69.27 | — |
| ActAdd | 92.31 | 55.73 | 73.38 | 63.19 | 51.64 | 59.65 | 60.72 | K=1, PC=n/a, layer=35, alpha=3 |
| CHaRS AA | 97.12 | 51.37 | 73.12 | 58.93 | 54.24 | 57.88 | 59.11 | K=5, PC=n/a, layer=35, alpha=3.5 |
| CHaRS-PCT AA | 97.12 | 51.37 | 73.12 | 58.93 | 54.33 | 57.88 | 59.13 | K=5, PC=1, layer=35, alpha=3.5 |

## Kết quả TinyBench theo task/cấu hình (65 dòng)

| Family | Task | Config | Metric | Score (%) | N | Timestamp |
|---|---|---|---|---|---|---|
| actadd_proxy_chars_aa_k1 | tinyArc | k1_layer35_alpha3 | acc_norm,none | 55.73 | 100 | — |
| actadd_proxy_chars_aa_k1 | tinyHellaswag | k1_layer35_alpha3 | acc_norm,none | 73.38 | 100 | — |
| actadd_proxy_chars_aa_k1 | tinyMMLU | k1_layer35_alpha3 | acc_norm,none | 63.19 | 100 | — |
| actadd_proxy_chars_aa_k1 | tinyTruthfulQA | k1_layer35_alpha3 | acc,none | 51.64 | 100 | — |
| actadd_proxy_chars_aa_k1 | tinyWinogrande | k1_layer35_alpha3 | acc_norm,none | 59.65 | 100 | — |
| chars_aa | tinyArc | k10_layer35_alpha2 | acc_norm,none | 57.83 | 100 | 2026-10-30T10-33-14.612372 |
| chars_aa | tinyArc | k10_layer35_alpha3 | acc_norm,none | 55.73 | 100 | 2026-10-30T06-14-50.192249 |
| chars_aa | tinyArc | k1_layer35_alpha2 | acc_norm,none | 57.83 | 100 | 2026-10-30T10-26-48.168520 |
| chars_aa | tinyArc | k1_layer35_alpha3 | acc_norm,none | 55.73 | 100 | 2026-10-30T06-09-45.352943 |
| chars_aa | tinyArc | k5_layer35_alpha2 | acc_norm,none | 57.83 | 100 | 2026-10-30T10-30-38.040299 |
| chars_aa | tinyArc | k5_layer35_alpha3 | acc_norm,none | 55.73 | 100 | 2026-10-30T06-12-19.724825 |
| chars_aa | tinyArc | k5_layer35_alpha3.5 | acc_norm,none | 51.37 | 100 | 2026-10-30T11-26-55.447519 |
| chars_aa | tinyHellaswag | k10_layer35_alpha2 | acc_norm,none | 73.93 | 100 | 2026-10-30T10-32-28.403824 |
| chars_aa | tinyHellaswag | k10_layer35_alpha3 | acc_norm,none | 73.38 | 100 | 2026-10-30T06-14-05.409277 |
| chars_aa | tinyHellaswag | k1_layer35_alpha2 | acc_norm,none | 73.93 | 100 | 2026-10-30T10-25-56.002851 |
| chars_aa | tinyHellaswag | k1_layer35_alpha3 | acc_norm,none | 73.38 | 100 | 2026-10-30T06-08-58.855847 |
| chars_aa | tinyHellaswag | k5_layer35_alpha2 | acc_norm,none | 73.93 | 100 | 2026-10-30T10-29-51.121092 |
| chars_aa | tinyHellaswag | k5_layer35_alpha3 | acc_norm,none | 73.38 | 100 | 2026-10-30T06-11-34.338587 |
| chars_aa | tinyHellaswag | k5_layer35_alpha3.5 | acc_norm,none | 73.12 | 100 | 2026-10-30T11-26-09.978764 |
| chars_aa | tinyMMLU | k10_layer35_alpha2 | acc_norm,none | 70.72 | 100 | 2026-10-30T10-38-56.802676 |
| chars_aa | tinyMMLU | k10_layer35_alpha3 | acc_norm,none | 63.19 | 100 | 2026-10-30T10-40-41.892284 |
| chars_aa | tinyMMLU | k10_layer35_alpha4 | acc_norm,none | 45.60 | 100 | 2026-10-30T10-42-12.455347 |
| chars_aa | tinyMMLU | k1_layer35_alpha2 | acc_norm,none | 70.72 | 100 | 2026-10-30T10-37-24.914493 |
| chars_aa | tinyMMLU | k1_layer35_alpha3 | acc_norm,none | 63.19 | 100 | 2026-10-30T10-40-00.061161 |
| chars_aa | tinyMMLU | k1_layer35_alpha4 | acc_norm,none | 44.54 | 100 | 2026-10-30T10-41-30.673367 |
| chars_aa | tinyMMLU | k5_layer35_alpha2 | acc_norm,none | 70.72 | 100 | 2026-10-30T10-38-35.812381 |
| chars_aa | tinyMMLU | k5_layer35_alpha3 | acc_norm,none | 63.19 | 100 | 2026-10-30T10-40-20.959006 |
| chars_aa | tinyMMLU | k5_layer35_alpha3.5 | acc_norm,none | 58.93 | 100 | 2026-10-30T11-27-15.523889 |
| chars_aa | tinyMMLU | k5_layer35_alpha4 | acc_norm,none | 45.60 | 100 | 2026-10-30T10-41-51.550710 |
| chars_aa | tinyTruthfulQA | k10_layer35_alpha2 | acc,none | 49.88 | 100 | 2026-10-30T10-33-56.059563 |
| chars_aa | tinyTruthfulQA | k10_layer35_alpha3 | acc,none | 51.62 | 100 | 2026-10-30T06-15-30.586190 |
| chars_aa | tinyTruthfulQA | k1_layer35_alpha2 | acc,none | 49.91 | 100 | 2026-10-30T10-27-38.554382 |
| chars_aa | tinyTruthfulQA | k1_layer35_alpha3 | acc,none | 51.64 | 100 | 2026-10-30T06-10-28.553498 |
| chars_aa | tinyTruthfulQA | k5_layer35_alpha2 | acc,none | 49.88 | 100 | 2026-10-30T10-31-20.047273 |
| chars_aa | tinyTruthfulQA | k5_layer35_alpha3 | acc,none | 51.64 | 100 | 2026-10-30T06-13-00.414301 |
| chars_aa | tinyTruthfulQA | k5_layer35_alpha3.5 | acc,none | 54.24 | 100 | 2026-10-30T11-27-41.232545 |
| chars_aa | tinyWinogrande | k10_layer35_alpha2 | acc_norm,none | 65.44 | 100 | 2026-10-30T10-34-13.381350 |
| chars_aa | tinyWinogrande | k10_layer35_alpha3 | acc_norm,none | 59.65 | 100 | 2026-10-30T06-15-46.429415 |
| chars_aa | tinyWinogrande | k1_layer35_alpha2 | acc_norm,none | 66.18 | 100 | 2026-10-30T10-28-01.628133 |
| chars_aa | tinyWinogrande | k1_layer35_alpha3 | acc_norm,none | 59.65 | 100 | 2026-10-30T06-10-46.163190 |
| chars_aa | tinyWinogrande | k5_layer35_alpha2 | acc_norm,none | 66.18 | 100 | 2026-10-30T10-31-37.583692 |
| chars_aa | tinyWinogrande | k5_layer35_alpha3 | acc_norm,none | 59.65 | 100 | 2026-10-30T06-13-16.521392 |
| chars_aa | tinyWinogrande | k5_layer35_alpha3.5 | acc_norm,none | 57.88 | 100 | 2026-10-30T11-27-57.343372 |
| chars_pct_aa | tinyArc | k10_maxpc15_layer35_pc5_alpha3 | acc_norm,none | 55.73 | 100 | 2026-10-30T06-22-57.851845 |
| chars_pct_aa | tinyArc | k1_maxpc15_layer35_pc5_alpha3 | acc_norm,none | 55.73 | 100 | 2026-10-30T06-17-58.428814 |
| chars_pct_aa | tinyArc | k5_maxpc15_layer35_pc1_alpha3.5 | acc_norm,none | 51.37 | 100 | 2026-10-30T11-30-43.023923 |
| chars_pct_aa | tinyArc | k5_maxpc15_layer35_pc5_alpha3 | acc_norm,none | 55.73 | 100 | 2026-10-30T06-20-28.724330 |
| chars_pct_aa | tinyHellaswag | k10_maxpc15_layer35_pc5_alpha3 | acc_norm,none | 73.38 | 100 | 2026-10-30T06-22-12.608869 |
| chars_pct_aa | tinyHellaswag | k1_maxpc15_layer35_pc5_alpha3 | acc_norm,none | 73.38 | 100 | 2026-10-30T06-17-13.524700 |
| chars_pct_aa | tinyHellaswag | k5_maxpc15_layer35_pc1_alpha3.5 | acc_norm,none | 73.12 | 100 | 2026-10-30T11-29-57.471193 |
| chars_pct_aa | tinyHellaswag | k5_maxpc15_layer35_pc5_alpha3 | acc_norm,none | 73.38 | 100 | 2026-10-30T06-19-43.450401 |
| chars_pct_aa | tinyMMLU | k5_maxpc15_layer35_pc1_alpha3.5 | acc_norm,none | 58.93 | 100 | 2026-10-30T11-31-03.526235 |
| chars_pct_aa | tinyTruthfulQA | k10_maxpc15_layer35_pc5_alpha3 | acc,none | 51.64 | 100 | 2026-10-30T06-23-39.037574 |
| chars_pct_aa | tinyTruthfulQA | k1_maxpc15_layer35_pc5_alpha3 | acc,none | 51.64 | 100 | 2026-10-30T06-18-39.581303 |
| chars_pct_aa | tinyTruthfulQA | k5_maxpc15_layer35_pc1_alpha3.5 | acc,none | 54.33 | 100 | 2026-10-30T11-31-29.116011 |
| chars_pct_aa | tinyTruthfulQA | k5_maxpc15_layer35_pc5_alpha3 | acc,none | 51.63 | 100 | 2026-10-30T06-21-09.108266 |
| chars_pct_aa | tinyWinogrande | k10_maxpc15_layer35_pc5_alpha3 | acc_norm,none | 59.65 | 100 | 2026-10-30T06-23-55.045647 |
| chars_pct_aa | tinyWinogrande | k1_maxpc15_layer35_pc5_alpha3 | acc_norm,none | 59.65 | 100 | 2026-10-30T06-18-55.429987 |
| chars_pct_aa | tinyWinogrande | k5_maxpc15_layer35_pc1_alpha3.5 | acc_norm,none | 57.88 | 100 | 2026-10-30T11-31-45.344922 |
| chars_pct_aa | tinyWinogrande | k5_maxpc15_layer35_pc5_alpha3 | acc_norm,none | 59.65 | 100 | 2026-10-30T06-21-24.552580 |
| trad_baseline | tinyArc | baseline_user_provided | acc_norm,none | 67.29 | — | — |
| trad_baseline | tinyHellaswag | baseline_user_provided | acc_norm,none | 75.56 | — | — |
| trad_baseline | tinyMMLU | baseline_user_provided | acc_norm,none | 73.21 | — | — |
| trad_baseline | tinyTruthfulQA | baseline_user_provided | acc,none | 56.01 | — | — |
| trad_baseline | tinyWinogrande | baseline_user_provided | acc_norm,none | 74.26 | — | — |
