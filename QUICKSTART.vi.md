# Bắt đầu nhanh

[English](QUICKSTART.md) · **Tiếng Việt**

Bạn không cần API, không cần đổi tên hàng trăm file và không cần biết lập trình. Hướng dẫn này giúp bạn bắt đầu quy trình thay nền sản phẩm có kiểm soát trong ChatGPT, Gemini, Claude hoặc Google Flow.

## 1. Chọn nền tảng

- [Hướng dẫn ChatGPT bằng tiếng Việt](platforms/chatgpt/setup.vi.md)
- [Hướng dẫn Gemini bằng tiếng Việt](platforms/gemini/setup.vi.md)
- [Hướng dẫn Claude bằng tiếng Việt](platforms/claude/setup.vi.md)
- [Hướng dẫn Google Flow Tool Builder bằng tiếng Việt](platforms/google-flow/setup.vi.md)

Hãy dùng nền tảng bạn đã có tài khoản và quen sử dụng. Bốn package dùng chung nguyên tắc bảo vệ sản phẩm, nhưng không có nghĩa các model sẽ tạo ảnh giống nhau hoặc có cùng khả năng.

Lưu ý riêng với Claude: Claude phải kiểm tra xem giao diện hiện tại có công cụ chỉnh sửa ảnh raster thật hay không. Nếu không có, Claude chỉ được phân tích ảnh, lập Khóa toàn vẹn sản phẩm và viết render brief; không được nói rằng ảnh đã được chỉnh sửa.

## 2. Chọn Instant Run hoặc Install Once

### Instant Run — dùng ngay

Phù hợp để thử workflow hoặc xử lý không thường xuyên:

1. Mở file `instant-run.md` của nền tảng đã chọn.
2. Copy toàn bộ nội dung nằm trong khối `text`.
3. Dán vào tin nhắn đầu tiên của một cuộc trò chuyện mới.
4. Chờ AI xác nhận workflow đã sẵn sàng rồi gửi ảnh.

Prompt runtime được giữ bằng tiếng Anh để ba platform hiểu nhất quán. Bạn vẫn có thể trao đổi, mô tả yêu cầu và nhận giải thích bằng tiếng Việt.

### Install Once — cài một lần để dùng lâu dài

Phù hợp khi bạn xử lý nhiều sản phẩm mỗi tuần:

- ChatGPT: tạo một Custom GPT.
- Gemini: tạo một Gem.
- Claude: tạo một Claude Project.

Bạn dán `installed-instructions.md` vào phần Instructions và upload bốn file đã gom trong [`bundles/`](bundles/README.vi.md) vào Knowledge. Sau đó mỗi lần làm ảnh chỉ cần mở GPT/Gem/Project đã cài.

### Google Flow Tool Builder

Làm theo [hướng dẫn Google Flow tiếng Việt](platforms/google-flow/setup.vi.md), sau đó dán `builder-prompt.md` vào Tool Builder. Không upload bốn Knowledge bundle dành cho hội thoại. Bắt đầu bằng Single; chỉ xem `BATCH EXPERIMENTAL` cho 2–20 job tách biệt là khả năng đã có khi bạn thực sự test được trên runtime hiện tại.

Các phần còn lại của Quickstart này mô tả ba package hội thoại. Người dùng Google Flow tiếp tục theo hướng dẫn cài và [`acceptance-checklist.md`](platforms/google-flow/acceptance-checklist.md); cùng nguyên tắc Product Lock, Reference-first, Strict Match và luôn retry từ ảnh gốc đã được chuyển thành control của Tool.

## 3. Gửi hình tham khảo style

Hình tham khảo chỉ cung cấp nền, bảng màu, ánh sáng, Bóng tiếp xúc, mood và khoảng trống. Nó không cung cấp sản phẩm mới.

Gửi hình tham khảo kèm câu này:

> Use this image as the style reference only. Extract the background, lighting, contact shadow, palette, mood, and spacing. Do not copy its product, props, text, logos, or watermark.

Ý nghĩa: “Chỉ dùng hình này làm tham khảo style. Không lấy sản phẩm, đạo cụ, chữ, logo hoặc watermark từ hình tham khảo.”

Workflow phải tạo **Reference Style Profile động** trực tiếp từ hình này và hiển thị `Style source: REFERENCE IMAGE` cùng `Style Card: NONE — reference-driven`. AI không được quy hình tham khảo về preset có tên gần nhất. Style Card chỉ dùng khi không có hình tham khảo hoặc khi bạn chủ động yêu cầu một card cụ thể.

Muốn nền bám sát hình tham khảo ở mức cao nhất mà AI tạo sinh có thể làm, gửi `SAFE RUN STRICT MATCH ECOMMERCE`. Strict Match bắt buộc dùng reference này; không cho phép sáng tạo lại, đổi bảng màu, dùng Style Card, thêm đạo cụ hoặc trang trí. Trước `CONTINUE`, hãy kiểm tra match target và những vùng nền phải tái tạo. Workflow bắt buộc ghi `Pixel-exact guarantee: NO — generative visual match`; gửi `STRICT MATCH OFF` để trở về Reference-first thông thường.

Bạn có thể dùng một hình tham khảo cho nhiều ảnh sản phẩm trong cùng batch.

## 4. Gửi ảnh sản phẩm cần thay nền

Gửi ảnh sản phẩm gốc kèm câu:

> This is the original product source. Replace only its background. Preserve the complete product and use this image as the source for every edit or repair.

Ý nghĩa: “Đây là ảnh sản phẩm gốc. Chỉ thay nền, giữ nguyên toàn bộ sản phẩm và luôn quay về ảnh này khi edit hoặc sửa lỗi.”

Không cần đổi tên file. Nếu gửi nhiều ảnh không ghi vai trò trong cùng một tin nhắn, AI phải mô tả đặc điểm quan sát được, đề xuất ảnh nào là source/reference và chờ bạn xác nhận trước khi chỉnh sửa. AI không được bịa phần trăm tự tin.

Mỗi ảnh sản phẩm phải tạo một output độc lập. Workflow không tự ghép collage trừ khi bạn yêu cầu rõ.

## 5. Chọn chế độ và mục đích đầu ra

Với sản phẩm đầu tiên hoặc sản phẩm quan trọng, gửi:

```text
SAFE RUN ECOMMERCE
```

`SAFE RUN` buộc AI hiển thị lock sheet trước khi tạo ảnh:

- **Product detected:** AI nhận diện sản phẩm gì và có bao nhiêu món.
- **Locked:** những chi tiết không được thay đổi.
- **Style extracted:** những thuộc tính style được phép lấy.
- **Excluded from reference:** sản phẩm, đạo cụ, chữ, logo và watermark phải loại bỏ.
- **Risks:** vùng khó, chi tiết chưa rõ, nguy cơ Sai lệch màu sản phẩm hoặc giới hạn nền tảng.

Nếu lock sheet đúng, trả lời:

```text
CONTINUE
```

Nếu sai, sửa ngay trước khi gửi `CONTINUE`.

Khi setup đã quen và nhiều ảnh có cấu trúc tương tự, dùng `FAST RUN`. Fast Run vẫn áp dụng cùng Khóa toàn vẹn sản phẩm và QA nhưng không cần dừng ở lock sheet, trừ khi đầu vào có vấn đề.

Chọn một output:

- `ECOMMERCE`: hình catalog tiết chế, không đạo cụ, không chữ tự sinh, ưu tiên độ trung thực và khoảng an toàn quanh sản phẩm.
- `SOCIAL`: cho phép mood nền mạnh hơn và negative space, nhưng không được thay đổi sản phẩm; đạo cụ chỉ được thêm khi bạn yêu cầu.
- `BOTH`: tạo hai output ecommerce và social riêng biệt từ cùng ảnh gốc, không ghép chung.

Khi đổi tỷ lệ khung hình, AI phải mở rộng nền trước. Không kéo giãn, bóp, cắt hoặc thay đổi tỷ lệ sản phẩm để ép vào khung.

## 6. Kiểm tra kết quả QA

Đặt ảnh gốc và output cạnh nhau, phóng to ở mức đủ thấy chi tiết. Kiểm tra:

- Phom dáng và đường biên sản phẩm;
- nếp gấp, đường may, cổ, tay áo, nút và khóa;
- texture, độ dày, độ trong và họa tiết lặp;
- màu sản phẩm, đặc biệt vùng trắng hoặc trung tính dễ nhiễm màu nền;
- chữ, logo và nhãn trên chính sản phẩm;
- viên đá, chấu, móc, mắt xích, charm và clasp;
- mép cắt, halo, chi tiết mảnh và vùng rỗng;
- Vùng bắt sáng bề mặt, phản chiếu và Bóng tiếp xúc;
- padding, crop, tỷ lệ khung và vật thể lạ lấy từ hình tham khảo.

Ý nghĩa trạng thái:

- `PASS`: mọi chi tiết có thể quan sát và quy tắc output đều đạt.
- `WARN`: chưa thấy lỗi chắc chắn nhưng có chi tiết không thể xác minh; AI phải nói rõ chi tiết đó.
- `FAIL`: có lỗi nhìn thấy được và cần một lần sửa đúng nhóm.
- `MANUAL REVIEW`: đã hết số lần sửa an toàn hoặc khả năng nền tảng không đủ.
- `UNSUPPORTED`: giao diện đã thử không có công cụ raster edit cần thiết.

Không chấp nhận `PASS` chỉ vì tổng thể ảnh đẹp.

## 7. Sửa lỗi hoặc chuyển sản phẩm tiếp theo

Chọn đúng một lệnh phù hợp với lỗi:

- `REPAIR PRODUCT`: sai sản phẩm, số lượng, phom hoặc bố cục các món.
- `REPAIR COLOR`: sản phẩm bị đổi hoặc nhiễm màu.
- `REPAIR DETAILS`: mất đường may, texture, chữ, logo, đá, khóa hoặc linh kiện.
- `REPAIR EDGES`: viền bị halo, lẹm, mất chi tiết hoặc sinh đường biên mới.
- `REPAIR BACKGROUND`: nền sai style, có vật thể hoặc chữ không mong muốn.
- `REPAIR LIGHTING`: Bóng tiếp xúc hoặc ánh sáng nền sai nhưng không được relight sản phẩm.
- `REPAIR COMPOSITION`: sai canvas, padding, vị trí hoặc crop.

Mọi lần repair phải quay về ảnh sản phẩm gốc. Không dùng output AI vừa sinh làm source cho lần sửa tiếp theo.

Nếu lần sửa có mục tiêu vẫn thất bại, chạy lại `SAFE RUN` từ ảnh gốc. Nếu vẫn sai, dừng ở `MANUAL REVIEW` và chuyển sang retouch truyền thống hoặc chụp lại.

Khi ảnh đã được duyệt, gửi:

```text
NEXT PRODUCT
```

Lệnh này xóa ảnh gốc và Khóa toàn vẹn sản phẩm của món trước, nhưng giữ lại Reference Style Profile, chế độ nền đang bật—kể cả Strict Match—run mode và output đã chọn cho batch tiếp theo.

## Công thức chạy thử đầu tiên

1. Mở hướng dẫn nền tảng tiếng Việt ở đầu trang.
2. Dùng Instant Run.
3. Gửi một hình tham khảo style.
4. Gửi một ảnh sản phẩm gốc.
5. Gửi `SAFE RUN ECOMMERCE`.
6. Kiểm tra lock sheet rồi gửi `CONTINUE`.
7. So ảnh gốc/output và chỉ chấp nhận nếu sản phẩm thật sự được giữ nguyên.
