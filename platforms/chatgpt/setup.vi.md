# Hướng dẫn ChatGPT — Tiếng Việt

[English](setup.md) · **Tiếng Việt**

Bạn có thể dùng workflow hoàn toàn trong giao diện ChatGPT, không cần API key. Chọn **Instant Run** nếu muốn thử ngay hoặc **Install Once** nếu thường xuyên xử lý nhiều ảnh.

## Cách 1 — Instant Run

1. Mở một cuộc trò chuyện ChatGPT mới có thể upload và tạo/chỉnh sửa ảnh.
2. Mở file `instant-run.md` trong thư mục này.
3. Copy toàn bộ nội dung nằm trong khối `text` và dán làm tin nhắn đầu tiên.
4. ChatGPT sẽ xác nhận workflow đã sẵn sàng.
5. Upload hình tham khảo và ghi rõ: `Use this image as the style reference only.`
6. Upload ảnh sản phẩm cần sửa và ghi rõ: `This is the original product source. Replace only its background.`
7. Gửi `SAFE RUN ECOMMERCE` cho lần đầu. Kiểm tra lock sheet rồi gửi `CONTINUE`.

Prompt runtime được giữ bằng tiếng Anh để hành vi ổn định, nhưng bạn có thể trao đổi mọi yêu cầu tiếp theo bằng tiếng Việt.

Instant Run phù hợp khi thử bộ workflow hoặc làm ảnh không thường xuyên. Nếu cuộc trò chuyện bắt đầu nhầm sản phẩm cũ với sản phẩm mới, hãy mở chat mới hoặc dùng `NEXT PRODUCT` đúng quy trình.

## Cách 2 — Install Once bằng Custom GPT

Việc tạo hoặc chỉnh sửa Custom GPT phụ thuộc plan ChatGPT và quyền của workspace. Thao tác tạo GPT được thực hiện trên giao diện web.

1. Mở [GPT editor](https://chatgpt.com/gpts/editor).
2. Tạo GPT mới và đặt tên dễ nhớ, ví dụ **Product Photo Background Studio**.
3. Mở file `installed-instructions.md`, copy toàn bộ nội dung và dán vào phần **Instructions**.
4. Trong phần capabilities, bật **Image Generation**.
5. Thêm đúng bốn file đã gom sau vào **Knowledge**:
   - [Workflow lõi](../../bundles/knowledge-core.md)
   - [Product Module](../../bundles/knowledge-products.md)
   - [Style Card](../../bundles/knowledge-styles.md)
   - [Output Profile](../../bundles/knowledge-outputs.md)
   Không upload đồng thời bundle và các file nguồn riêng lẻ vì nội dung sẽ bị trùng.
6. Không cần upload các file `_template.md` trừ khi bạn muốn GPT hỗ trợ viết module mới.
7. Thêm conversation starters như `SAFE RUN ECOMMERCE`, `FAST RUN SOCIAL` hoặc `FAST RUN BOTH`.
8. Test bằng một sản phẩm không quá quan trọng trước khi đưa vào batch thật.
9. Lưu GPT theo quyền riêng tư hoặc chia sẻ phù hợp với chính sách workspace.

## Cách dùng sau khi cài

1. Mở Custom GPT vừa tạo.
2. Gửi hình tham khảo style một lần.
3. Gửi ảnh sản phẩm gốc.
4. Chọn Safe/Fast Run và Ecommerce/Social/Both.
5. Review QA, sửa đúng một lỗi nếu cần.
6. Gửi `NEXT PRODUCT` rồi upload món tiếp theo.

Mỗi sản phẩm phải tạo Khóa toàn vẹn sản phẩm mới. Không dùng output của sản phẩm trước làm nguồn cho sản phẩm sau.

## Giới hạn cần biết

- Vùng chọn trong ChatGPT không phải mask chính xác tuyệt đối; edit có thể lan ra ngoài vùng đã đánh dấu.
- AI không đảm bảo giữ đúng mọi pixel, chữ nhỏ, đường may, texture hoặc chi tiết trang sức.
- Ảnh chụp thường không cung cấp màu Hex/RGB chính xác nếu không có dữ liệu hiệu chỉnh.
- Hạn mức upload và tạo ảnh có thể thay đổi theo plan, workspace và thời điểm.
- Nếu repair thất bại, phải quay về ảnh gốc; không tiếp tục sửa trên output đã sinh.

Xem chi tiết kỹ thuật tại `limitations.md`. Tài liệu chính thức hiện hành của OpenAI: [tạo và chỉnh sửa GPT](https://help.openai.com/en/articles/8554397-creating-a-gpt) và [tạo/chỉnh sửa ảnh trong ChatGPT](https://help.openai.com/en/articles/11084440-images-in-chatgpt).

## Cập nhật workflow

Khi repo có phiên bản mới, tải lại và thay bốn bundle bị ảnh hưởng. Nếu `installed-instructions.md` thay đổi, cập nhật lại phần Instructions. Sau mỗi lần cập nhật, test một ảnh trước khi tiếp tục batch sản xuất.
