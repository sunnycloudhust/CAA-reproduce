# Tổng hợp kết quả thực nghiệm

Phạm vi tổng hợp: các file thống kê hiện có trong `results/**/eval_results/stat_results/`, seed 42. TruthfulQA có 817 mẫu mỗi cấu hình; UltrafeedbackBinarized có 500 mẫu mỗi cấu hình (đếm số bản ghi JSONL).

## TruthfulQA

Các chỉ số `True * Info`, `Truthfulness`, `Informativeness` càng cao càng tốt. `Perplexity` càng thấp thường cho thấy câu trả lời dễ dự đoán hơn; `Dist-1/2/3` đo độ đa dạng n-gram.

| Model (layer) | Phương pháp | True × Info | Truthfulness | Informativeness | Perplexity | Dist-1 | Dist-2 | Dist-3 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Falcon-7B (14) | NoSteer | 0.271 | 0.307 | 0.955 | 154.452 | 0.938 | 0.827 | 0.751 |
| Falcon-7B (14) | CAA T=1.0 | 0.335 | 0.366 | 0.961 | 105.058 | 0.919 | 0.853 | 0.799 |
| Falcon-7B (14) | ODESteer T=5.0 | 0.318 | 0.348 | **0.963** | 135.965 | **0.926** | 0.843 | 0.779 |
| Qwen2.5-7B (13) | NoSteer | 0.656 | 0.799 | 0.853 | 23.255 | 0.903 | 0.978 | 0.982 |
| Qwen2.5-7B (13) | CAA T=1.0 | 0.662 | 0.807 | 0.849 | 23.350 | 0.909 | 0.980 | 0.982 |
| Qwen2.5-7B (13) | ODESteer T=5.0 | **0.685** | **0.812** | **0.869** | **23.199** | **0.910** | **0.983** | **0.986** |
| Mistral-7B (15) | NoSteer | 0.375 | 0.415 | **0.957** | 211.105 | **0.956** | 0.885 | 0.825 |
| Mistral-7B (15) | CAA T=1.0 | 0.461 | 0.513 | 0.947 | 170.978 | 0.948 | 0.900 | 0.852 |
| Mistral-7B (15) | ODESteer T=5.0 | **0.556** | **0.805** | 0.744 | **48.999** | 0.901 | **0.959** | **0.962** |

### So sánh nhanh với NoSteer

- **Falcon:** CAA tăng `True × Info` từ 0.271 lên 0.335 (+0.065); ODESteer đạt 0.318 (+0.048). ODESteer có Informativeness cao nhất (0.963), còn CAA có Truthfulness cao nhất (0.366) trong ba cấu hình.
- **Qwen:** ODESteer dẫn đầu cả ba chỉ số chất lượng chính: `True × Info` +0.029, Truthfulness +0.012, Informativeness +0.016; Perplexity giảm nhẹ 0.057.
- **Mistral:** ODESteer tăng `True × Info` +0.181 và Truthfulness +0.390, đồng thời giảm Perplexity khoảng 162.106. Informativeness giảm 0.213 so với NoSteer, nên điểm tổng hợp cao hơn đi kèm câu trả lời ít informative hơn theo metric này.

## UltrafeedbackBinarized

| Model (layer) | Phương pháp | RM Mean | RM P90 | RM Win-Rate vs NoSteer |
|---|---|---:|---:|---:|
| Llama3.1-8B (13) | NoSteer | -10.218 | 0.187 | 0.500 |
| Llama3.1-8B (13) | CAA T=1.0 | **-9.808** | **0.267** | **0.547** |

CAA tăng RM Mean 0.410 điểm, RM P90 0.081 điểm và win-rate 4.7 điểm phần trăm so với NoSteer. Trong thư mục hiện tại không có hàng thống kê hoặc kết quả chi tiết Ultrafeedback cho ODESteer.

## Phạm vi và lưu ý

- Có thống kê TruthfulQA cho Falcon-7B layer 14, Qwen2.5-7B layer 13 và Mistral-7B layer 15; mỗi model có NoSteer, CAA và ODESteer.
- Có thống kê UltrafeedbackBinarized cho Llama3.1-8B layer 13 với NoSteer và CAA.
- Các bảng trên chép và làm tròn từ CSV thống kê đã lưu, không tính lại metric từ raw output. Chỉ có seed 42 nên chưa thể đánh giá độ biến thiên giữa các lần chạy.
- Dấu **đậm** đánh dấu giá trị tốt nhất theo từng cột trong nhóm model tương ứng (Perplexity lấy thấp nhất). `True × Info` là chỉ số tổng hợp được lưu trong CSV.
