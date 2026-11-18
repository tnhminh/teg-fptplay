# FPT Play × Tetrate Enterprise Gateway

Một trang web tĩnh trình bày đánh giá đầu tư API Gateway cho FPT Play: Envoy Gateway OSS, TEG Community và TEG Enterprise (Tetrate v1.10.x). Trang có hai tab:

| Tab | Nguồn | Nội dung |
|---|---|---|
| Đánh giá đầu tư (`#danh-gia`) | `src/danh-gia.html` | 5 bài toán Enterprise giải quyết, giá trị, những gì không tự giải quyết, TCO/ROI, 4 phương án |
| Khác biệt ba phiên bản (`#khac-biet`) | `src/khac-biet.html` | Khác biệt thật giữa ba phiên bản: OSS không có, hay OSS làm được nhưng phải tự xây |

## Sửa nội dung

`index.html` là file sinh ra, đừng sửa tay. Sửa file trong `src/` rồi chạy:

```bash
python build.py
```

Script nhúng nguyên từng trang nguồn vào một `<iframe srcdoc>` trong `index.html`, nên CSS và JS của hai tab không đụng nhau. `khac-biet.html` ở gốc chỉ còn là trang chuyển hướng cho link cũ.

## Chạy

Mở trực tiếp `index.html` bằng trình duyệt, hoặc chạy server tĩnh:

```bash
python -m http.server 8000
```

rồi mở http://localhost:8000.

## Triển khai

GitHub Pages phục vụ nhánh `main`, thư mục gốc. Push lên `main` là trang tự cập nhật.

## Ghi chú

- Mọi thứ nằm trong một file `index.html` (CSS và JS nhúng sẵn), chỉ tải font từ Google Fonts. Không có mạng thì trang dùng font hệ thống.
- Số liệu TCO/ROI và số liệu sự cố là giả định minh họa, không phải báo giá Tetrate hay dữ liệu Production.
