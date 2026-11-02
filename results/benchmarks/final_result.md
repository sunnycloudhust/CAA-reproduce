# Final Results: Attack Success Rate and TinyBenchmark

Điểm tính theo phần trăm. ASR lấy từ evaluator LlamaGuard3. ActAdd được biểu diễn theo quy ước CHaRS AA tại K=1; CHaRS AA và CHaRS-PCT AA dùng K=5. Cấu hình TinyBench được chọn để giữ nhiều điểm khớp nhất. ASR lấy từ evaluator và có thể dùng cấu hình alpha/K/PC khác; cấu hình cho hai loại kết quả được ghi riêng khi có dữ liệu.

| Model | Method | ASR ↑ | tinyArc | tinyHella | tinyMMLU | tinyTQA | tinyWino | Avg |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Gemma2-9B-Instruct | No Steering | — | 69.31 | 80.81 | 76.57 | 54.77 | 76.86 | 71.66 |
| Gemma2-9B-Instruct | ActAdd | 1.92 | 66.57 | 81.67 | 72.06 | 57.31 | 75.29 | 70.58 |
| Gemma2-9B-Instruct | CHaRS AA | 1.92 | 66.57 | 81.67 | 72.06 | 57.29 | 75.29 | 70.58 |
| Gemma2-9B-Instruct | CHaRS-PCT AA | 1.92 | 67.61 | 81.27 | 73.00 | 53.38 | 76.85 | 70.42 |
| Llama3.1-8B-Instruct | No Steering | — | 65.33 | 81.40 | 62.90 | 54.43 | 73.81 | 67.57 |
| Llama3.1-8B-Instruct | ActAdd | 89.42 | 29.71 | 55.06 | 29.00 | 44.91 | 60.13 | 43.76 |
| Llama3.1-8B-Instruct | CHaRS AA | 93.27 | 34.67 | 38.15 | 27.42 | 46.60 | 51.81 | 39.73 |
| Llama3.1-8B-Instruct | CHaRS-PCT AA | 95.19 | 34.67 | 38.15 | 27.42 | 46.62 | 51.81 | 39.73 |
| Llama3.2-3B-Instruct | No Steering | — | 56.16 | 76.69 | 63.68 | 50.32 | 61.56 | 61.68 |
| Llama3.2-3B-Instruct | ActAdd | 91.35 | 31.60 | 42.67 | — | 46.23 | 62.17 | — |
| Llama3.2-3B-Instruct | CHaRS AA | 92.31 | 31.60 | 41.12 | — | 46.10 | 62.17 | — |
| Llama3.2-3B-Instruct | CHaRS-PCT AA | 90.38 | 31.60 | 42.67 | — | 46.19 | 62.17 | — |
| Qwen2.5-3B-Instruct | No Steering | — | 62.82 | 69.90 | 67.98 | 57.23 | 65.90 | 64.77 |
| Qwen2.5-3B-Instruct | ActAdd | 97.12 | 40.39 | 61.95 | 50.50 | 43.15 | 61.97 | 51.59 |
| Qwen2.5-3B-Instruct | CHaRS AA | 97.12 | 40.39 | 61.95 | 50.50 | 43.14 | 61.97 | 51.59 |
| Qwen2.5-3B-Instruct | CHaRS-PCT AA | 98.08 | 40.39 | 61.95 | 50.50 | 43.14 | 61.97 | 51.59 |
| Qwen2.5-7B-Instruct | No Steering | — | 67.29 | 75.56 | 73.21 | 56.01 | 74.26 | 69.27 |
| Qwen2.5-7B-Instruct | ActAdd | 92.31 | 55.73 | 73.38 | 63.19 | 51.64 | 59.65 | 60.72 |
| Qwen2.5-7B-Instruct | CHaRS AA | 97.12 | 51.37 | 73.12 | 58.93 | 54.24 | 57.88 | 59.11 |
| Qwen2.5-7B-Instruct | CHaRS-PCT AA | 97.12 | 51.37 | 73.12 | 58.93 | 54.33 | 57.88 | 59.13 |
| Qwen2.5-14B-Instruct | No Steering | — | 73.96 | 82.71 | 75.31 | 65.24 | 74.58 | 74.36 |
| Qwen2.5-14B-Instruct | ActAdd | 86.54 | 72.44 | 83.47 | 74.77 | 65.74 | 74.06 | 74.10 |
| Qwen2.5-14B-Instruct | CHaRS AA | 94.23 | 72.44 | 83.47 | 74.77 | 65.72 | 74.06 | 74.09 |
| Qwen2.5-14B-Instruct | CHaRS-PCT AA | 89.42 | 72.44 | 83.47 | 74.77 | 65.72 | 74.06 | 74.09 |

## Cấu hình đã chọn

| Model | ActAdd proxy | CHaRS AA | CHaRS-PCT AA | TinyBench khớp |
|---|---|---|---|---|
| Gemma2-9B-Instruct | ActAdd: K=1, alpha=1, layer=44 | CHaRS AA: K=5, alpha=1, layer=44 | CHaRS-PCT AA: K=5, PC=5, alpha=1, layer=44 | ActAdd 5/5; CHaRS AA 5/5; CHaRS-PCT AA 5/5 |
| Llama3.1-8B-Instruct | ActAdd: K=1, alpha=3, layer=25 | CHaRS AA: K=5, alpha=4, layer=25 | CHaRS-PCT AA: K=5, PC=5, alpha=4, layer=25 | ActAdd 5/5; CHaRS AA 5/5; CHaRS-PCT AA 5/5 |
| Llama3.2-3B-Instruct | ActAdd: K=1, alpha=3, layer=28 | CHaRS AA: K=5, alpha=3, layer=28 | CHaRS-PCT AA: K=5, PC=5, alpha=3, layer=28 | ActAdd 4/5; CHaRS AA 4/5; CHaRS-PCT AA 4/5 |
| Qwen2.5-3B-Instruct | ActAdd: K=1, alpha=3, layer=47 | CHaRS AA: K=5, alpha=3, layer=47 | CHaRS-PCT AA: K=5, PC=5, alpha=3, layer=47 | ActAdd 5/5; CHaRS AA 5/5; CHaRS-PCT AA 0/5 |
| Qwen2.5-7B-Instruct | ActAdd: K=1, alpha=3, layer=35 | CHaRS AA: K=5, alpha=3.5, layer=35 | CHaRS-PCT AA: K=5, PC=3, alpha=3.5, layer=35 | ActAdd 5/5; CHaRS AA 5/5; CHaRS-PCT AA 5/5 |
| Qwen2.5-14B-Instruct | ActAdd: K=1, alpha=1, layer=47 | CHaRS AA: K=5, alpha=1, layer=47 | CHaRS-PCT AA: K=5, PC=5, alpha=1, layer=47 | ActAdd 5/5; CHaRS AA 5/5; CHaRS-PCT AA 5/5 |

## Cần chạy thêm

### TinyBench

- Qwen2.5-3B CHaRS-PCT AA: K=5, PC=5, layer=47, alpha=3; cần đủ 5 task.
- Llama3.2-3B tại K=1/K=5, layer=28, alpha=3: tinyMMLU cho ActAdd proxy, CHaRS AA và CHaRS-PCT AA.

### Ghi chú ASR

ASR của Gemma2-9B tại alpha=1 là 1.92% cho cả ba phương pháp; Qwen2.5-3B tại alpha=3 đạt 97.12% (ActAdd/AA) và 98.08% (PCT); Qwen2.5-14B lần lượt đạt 86.54% (ActAdd), 94.23% (CHaRS AA) và 89.42% (CHaRS-PCT AA).

Riêng Qwen2.5-14B: TinyBench dùng α=1; ASR 86.54% (ActAdd proxy, K=1, α=4), 94.23% (CHaRS AA, K=1, α=4.5) và 89.42% (CHaRS-PCT AA, K=1, PC=5, α=4). Vì vậy các ASR này không dùng cùng alpha với TinyBench. Baseline lấy từ số liệu bạn cung cấp. ActAdd là proxy CHaRS AA K=1, không phải lần chạy ActAdd độc lập. Nguồn TinyBench: `benchmarks/tinybench_scores_latest.csv`; nguồn ASR: các file evaluator trong `output/`.
