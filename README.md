# FPT Play × Tetrate Enterprise Gateway

Hai trang web tĩnh trình bày đánh giá đầu tư API Gateway cho FPT Play: Envoy Gateway OSS, TEG Community và TEG Enterprise (Tetrate v1.10.x).

| File | Nội dung |
|---|---|
| `index.html` | Đánh giá đầu tư: 5 bài toán Enterprise giải quyết, giá trị, những gì không tự giải quyết, TCO/ROI, 4 phương án |
| `khac-biet.html` | Khác biệt thật giữa ba phiên bản: OSS không có, hay OSS làm được nhưng phải tự xây |

## Chạy

Không cần build. Mở trực tiếp `index.html` bằng trình duyệt, hoặc chạy server tĩnh:

```bash
python3 -m http.server 8000
```

rồi mở http://localhost:8000. Hai trang có liên kết qua lại ở thanh trên cùng.

## Triển khai GitHub Pages

```bash
git init && git add . && git commit -m "TEG evaluation pages"
git remote add origin https://github.com/<org>/<repo>.git
git push -u origin main
```

Sau đó bật Pages trong Settings → Pages, chọn branch `main`, thư mục `/ (root)`.

## Ghi chú

- Mỗi trang là một file HTML tự chứa (CSS và JS nhúng sẵn), chỉ tải font từ Google Fonts. Không có mạng thì trang dùng font hệ thống.
- Số liệu TCO/ROI và số liệu sự cố là giả định minh họa, không phải báo giá Tetrate hay dữ liệu Production.
