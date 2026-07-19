# Hướng dẫn Claude — Tiếng Việt

[English](setup.md) · **Tiếng Việt**

Claude có thể đọc và phân tích ảnh, nhưng việc chỉnh sửa trực tiếp file ảnh phụ thuộc vào công cụ thật sự có trong giao diện bạn đang dùng. Workflow này bắt buộc Claude kiểm tra capability trước khi nói rằng ảnh đã được edit.

## Điều quan trọng trước khi bắt đầu

Nếu Claude không có image-editing tool trong cuộc trò chuyện hiện tại, Claude vẫn có thể:

- xác định vai trò ảnh;
- phân tích sản phẩm;
- tạo Khóa toàn vẹn sản phẩm;
- tách style được phép dùng;
- chọn Product Module và Output Profile;
- viết source-first render brief;
- QA một output thật do bạn upload sau đó.

Claude không được giả vờ rằng raster edit đã xảy ra. Khi thiếu tool, trạng thái phải là `ANALYSIS ONLY` hoặc `UNSUPPORTED`, không phải `PASS`.

## Cách 1 — Instant Run

1. Mở một cuộc trò chuyện Claude mới.
2. Mở file `instant-run.md` trong thư mục này.
3. Copy toàn bộ nội dung trong khối `text` và dán làm tin nhắn đầu tiên.
4. Upload hình tham khảo và ghi rõ vai trò style reference.
5. Upload ảnh sản phẩm và ghi rõ original product source.
6. Gửi `SAFE RUN ECOMMERCE` hoặc chế độ bạn muốn.
7. Đọc capability statement của Claude trước khi kỳ vọng một output ảnh.

Prompt runtime được giữ bằng tiếng Anh để giữ nguyên các lệnh và điều kiện capability. Bạn có thể làm việc bằng tiếng Việt trong các tin nhắn tiếp theo.

## Cách 2 — Install Once bằng Claude Project

1. Mở [Claude Projects](https://claude.ai/projects).
2. Tạo project mới và đặt tên, ví dụ **Product Photo Background Studio**.
3. Chọn **Set project instructions**.
4. Mở `installed-instructions.md`, copy toàn bộ nội dung, dán vào Project Instructions và lưu.
5. Thêm các file sau vào Project Knowledge:
   - toàn bộ core workflow trong `core/`;
   - Product Module trong `products/`;
   - Style Card trong `styles/`;
   - Output Profile trong `outputs/`.
6. Không thêm `_template.md` trừ khi project dùng để phát triển module.
7. Mở chat mới trong project và thử bằng một ảnh không quan trọng.
8. Xác nhận Claude nói rõ có hay không có công cụ image editing.

## Cách dùng sau khi cài

1. Gửi style reference và product source với vai trò rõ ràng.
2. Dùng `SAFE RUN` cho lần đầu hoặc trường hợp nhiều rủi ro.
3. Nếu Claude có tool edit thật, tiếp tục `CONTINUE`, tạo ảnh và QA.
4. Nếu không có tool, nhận lock sheet và render brief để dùng như tài liệu phân tích.
5. Khi có output thật từ một quy trình khác, upload lại để Claude so source/reference/output và QA.
6. Dùng `NEXT PRODUCT` để xóa Product Lock cũ trước món tiếp theo.

Claude không tự động xuất prompt sang model khác, không tự chuyển bạn sang nền tảng khác và không được nói rằng prompt sẽ cho kết quả giống nhau ở các model.

## Giới hạn cần biết

- Upload/vision capability không đồng nghĩa với khả năng edit raster.
- Khả năng có thể khác theo giao diện, tài khoản, plan, workspace policy, connected tool và thời điểm.
- Phân tích ảnh có thể bỏ sót chữ nhỏ, texture, chi tiết trang sức, độ trong, Sai lệch màu sản phẩm và lỗi phản chiếu.
- Không suy ra màu sản xuất Hex/RGB chính xác từ ảnh thường.
- Nếu có integration chỉnh ảnh, generative edit vẫn có thể thay đổi nhiều hơn phần nền.
- Repair phải quay về ảnh gốc. Sau một repair và một Safe Run vẫn sai thì chuyển `MANUAL REVIEW`.

Xem thêm `limitations.md`. Tài liệu chính thức của Anthropic: [tạo và quản lý Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) và [upload file/ảnh vào Claude](https://support.claude.com/en/articles/8241126-upload-files-to-claude).

## Cập nhật workflow

Khi repo thay đổi, cập nhật file tương ứng trong Project Knowledge. Nếu `installed-instructions.md` đổi, thay lại Project Instructions. Kiểm tra capability và chạy thử một case trước khi dùng cho batch thật.
