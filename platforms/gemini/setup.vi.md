# Hướng dẫn Gemini — Tiếng Việt

[English](setup.md) · **Tiếng Việt**

Workflow chạy trực tiếp trong Gemini và không cần API key. Dùng **Instant Run** để thử nhanh hoặc tạo một **Gem** để cài một lần và dùng lại cho nhiều batch.

## Cách 1 — Instant Run

1. Mở cuộc trò chuyện mới tại [Gemini](https://gemini.google.com/).
2. Mở file `instant-run.md` trong thư mục này.
3. Copy toàn bộ prompt nằm trong khối `text` và dán làm tin nhắn đầu tiên.
4. Upload hình tham khảo, ghi rõ đó chỉ là style reference.
5. Upload một hoặc nhiều ảnh sản phẩm và ghi rõ từng ảnh là original product source.
6. Gửi `SAFE RUN ECOMMERCE` cho sản phẩm đầu tiên.
7. Kiểm tra role mapping và lock sheet trước khi gửi `CONTINUE`.

Khi đã có hình tham khảo, lock sheet phải ghi `Style source: REFERENCE IMAGE` và `Style Card: NONE — reference-driven`. Style Card có tên chỉ dùng khi không có reference hoặc khi bạn chủ động yêu cầu.

Muốn bám sát nền mẫu tối đa, gửi `SAFE RUN STRICT MATCH ECOMMERCE`. Trước khi tiếp tục, kiểm tra Gemini đã ghi match target, vùng nền phải tái tạo và `Pixel-exact guarantee: NO — generative visual match`.

Bạn không cần đổi tên ảnh. Nếu gửi nhiều ảnh cùng lúc nhưng không ghi vai trò, Gemini phải mô tả từng ảnh bằng đặc điểm nhìn thấy được, đề xuất source/reference và chờ bạn xác nhận trước khi edit.

Prompt runtime vẫn bằng tiếng Anh để giữ hành vi nhất quán, nhưng toàn bộ trao đổi làm việc có thể dùng tiếng Việt.

## Cách 2 — Install Once bằng Gem

Gem tùy chỉnh được tạo/chỉnh sửa trên giao diện Gemini web. Khả năng sử dụng Gem, upload Knowledge và image editing có thể phụ thuộc tài khoản hoặc workspace.

1. Mở Gemini trên web.
2. Mở khu vực **Gems** và chọn **New Gem**.
3. Đặt tên, ví dụ **Product Photo Background Studio**.
4. Mở `installed-instructions.md`, copy toàn bộ và dán vào phần Instructions của Gem.
5. Trong phần **Knowledge**, upload đúng bốn file đã gom:
   - [Workflow lõi](../../bundles/knowledge-core.md)
   - [Product Module](../../bundles/knowledge-products.md)
   - [Style Card](../../bundles/knowledge-styles.md)
   - [Output Profile](../../bundles/knowledge-outputs.md)
   Như vậy chỉ dùng 4/10 attachment trong một lần upload. Bundle Style Card chỉ là thư viện dự phòng, không ghi đè hình tham khảo đã upload. Không upload thêm các file nguồn riêng lẻ vì sẽ trùng nội dung.
6. Không thêm `_template.md` nếu Gem chỉ dùng để chỉnh ảnh.
7. Preview bằng một ảnh test có quyền sử dụng.
8. Kiểm tra rằng Gem hỏi lại vai trò khi ảnh không có nhãn và không lấy sản phẩm/đạo cụ từ reference.
9. Lưu Gem.

## Cách dùng sau khi cài

1. Mở Gem vừa tạo.
2. Gửi hình style reference.
3. Gửi một hoặc nhiều product source.
4. Chọn `SAFE RUN` hoặc `FAST RUN`.
5. Chọn `ECOMMERCE`, `SOCIAL` hoặc `BOTH`.
6. Review từng output độc lập; không chấp nhận collage nếu bạn không yêu cầu.
7. Dùng `NEXT PRODUCT` để xóa Product Lock cũ trước món tiếp theo.

Nếu cùng một style áp dụng cho nhiều sản phẩm, có thể giữ reference và thiết lập output. Tuy nhiên, mỗi ảnh sản phẩm vẫn phải có Product Lock và QA riêng.

## Giới hạn cần biết

- Tính năng có thể khác nhau theo ngôn ngữ, quốc gia, độ tuổi, loại tài khoản, plan, workspace và quota.
- Reference không phải mask; thông tin giữa nhiều ảnh có thể bị trộn nếu vai trò không rõ.
- Chữ nhỏ, texture, đá, chấu, mắt xích, độ trong, màu kim loại và phản chiếu cần review thủ công.
- Không suy ra màu Hex/RGB sản xuất chính xác từ ảnh thường.
- Nếu một repair thất bại, quay lại original product source và chạy Safe Run; không dùng ảnh generated làm nguồn mới.

Xem thêm `limitations.md`. Tài liệu chính thức của Google: [tạo và quản lý Gems](https://support.google.com/gemini/answer/15146780?hl=en) và [tạo/chỉnh sửa ảnh với Gemini](https://support.google.com/gemini/answer/14286560?hl=en).

## Cập nhật workflow

Khi module hoặc instructions trong repo thay đổi, tải lại bundle tương ứng trong Knowledge và lưu lại Gem. Test lại một sản phẩm trước khi dùng cho batch tiếp theo.
