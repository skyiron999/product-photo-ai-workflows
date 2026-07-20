# Bộ Knowledge sẵn sàng upload

[English](README.md)

Bốn file đã gom này kết hợp 17 tài liệu workflow có thể phát hành thành một bộ Knowledge gọn nhẹ:

1. [Workflow lõi](knowledge-core.md)
2. [Product Module](knowledge-products.md)
3. [Style Card](knowledge-styles.md)
4. [Output Profile](knowledge-outputs.md)

Bundle Style Card là thư viện dự phòng. Khi người dùng gửi hình tham khảo, workflow tạo Reference Style Profile động từ chính hình đó và không tự chọn một card có tên.

Upload cả bốn file vào khu vực Knowledge của Custom GPT, Gemini Gem hoặc Claude Project. Không upload file README này, các file `_template.md`, hoặc các module nguồn riêng lẻ cùng lúc.

## Tại sao là bốn file

Thư viện nguồn vẫn được chia module để người đóng góp dễ bảo trì, trong khi bộ file đã gom nằm gọn trong giới hạn 10 attachment mỗi lần upload của Gemini. Việc chia theo chức năng cũng giúp bạn chỉ cần thay bundle có thay đổi thay vì quản lý một file khổng lồ.

## Nguồn chính thức

Các file trong `core/`, `products/`, `styles/` và `outputs/` là nguồn chính thức. Bốn Knowledge bundle là file được sinh tự động, không chỉnh sửa trực tiếp.

Sau khi thay đổi file nguồn, hãy tạo lại và kiểm tra bundle:

```bash
python tools/build_bundles.py
python tools/build_bundles.py --check
```

CI sẽ báo lỗi nếu bundle đã commit bị thiếu hoặc không còn đồng bộ.
