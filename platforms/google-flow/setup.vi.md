# Hướng dẫn Google Flow Tool — Tiếng Việt

[English](setup.md) · **Tiếng Việt**

Package này giúp tạo một Tool thay nền sản phẩm có thể dùng lại ngay trong Google Flow. Tài sản chính là [`builder-prompt.md`](builder-prompt.md), không phải prompt Instant Run dành cho hội thoại.

Builder prompt đã tự chứa toàn bộ hợp đồng cần thiết. **Không** upload bốn Knowledge bundle dành cho ChatGPT/Gemini/Claude vào Tool. Nội dung trùng lặp có thể khiến Tool Builder trộn vai trò ảnh hoặc dựng app phức tạp không cần thiết.

## Bạn cần chuẩn bị

- Tài khoản Google có thể mở Google Flow trên web và tạo Tool.
- Đủ Flow credits hiện tại cho một lượt test nhỏ. Phân tích, tạo ảnh, retry và từng output của `BOTH` đều có thể dùng credits.
- Một Product Source và một Style Reference mà bạn có quyền sử dụng cho test đầu tiên.
- Ba sản phẩm có hình dáng khác nhau rõ ràng cho test Batch.
- Quyền upload hình theo chính sách riêng tư của tổ chức hoặc khách hàng.

Khả năng tạo Tool, credits, model và control có thể thay đổi theo tài khoản, gói, khu vực và đợt phát hành. Đọc [`limitations.md`](limitations.md) trước khi xử lý hình thương mại. Có thể xem thêm tài liệu hiện hành của Google về [Tools](https://support.google.com/flow/answer/17104535?hl=en), [AI credits](https://support.google.com/flow/answer/16526234?hl=en) và [dữ liệu trong Flow](https://support.google.com/flow/answer/17025472?hl=en).

## 1. Tạo Tool

1. Mở [Google Flow](https://labs.google/fx/tools/flow) bằng trình duyệt máy tính và đăng nhập.
2. Mở **Tools**, sau đó tạo custom Tool mới.
3. Đặt tên tạm, ví dụ **Product Background Studio — Draft**.
4. Mở [`builder-prompt.md`](builder-prompt.md).
5. Copy toàn bộ nội dung nằm trong khối `text` duy nhất. Không chỉ copy vài đoạn rời.
6. Dán vào Tool Builder và chờ Flow tạo hoặc cập nhật Tool.
7. Chưa chạy tạo ảnh ngay.

Lần dựng đầu tiên có thể chưa thực hiện đúng mọi yêu cầu. Câu trả lời “đã làm xong” trong chat của Tool Builder chưa phải bằng chứng; cần kiểm tra Tool được sinh ra.

## 2. Kiểm tra Preview và Code

Trước khi tốn credits, kiểm tra trong Preview:

- ba vùng tách biệt: `PRODUCT SOURCE`, `STYLE REFERENCE`, `GENERATED OUTPUT`;
- Product Analysis và Reference Style Profile là hai card riêng, không phải một “Vision Analysis” trộn chung;
- có `SINGLE` và `BATCH EXPERIMENTAL`;
- có `SAFE` / `FAST`, `REFERENCE-FIRST` / `STRICT MATCH`, `ECOMMERCE` / `SOCIAL` / `BOTH`;
- có Aspect Ratio, Product Scale và Detail Recovery;
- nút chạy bị vô hiệu hóa khi thiếu Product Source hoặc Style Reference;
- mỗi hàng Batch có trạng thái, View, Retry from Source và Download đúng với khả năng thật.

Sau đó kiểm tra Code hoặc developer diagnostics:

- ảnh sản phẩm gốc, reference, Product Lock, Reference Style Profile, output và QA dùng state tách biệt;
- phân tích Product và Reference là hai operation riêng;
- mỗi lần tạo trong Batch chỉ dùng một original Product Source cùng reference chung, không đưa toàn bộ danh sách sản phẩm vào một request;
- retry quay lại immutable original Product Source;
- Download All chỉ tồn tại nếu thực sự export được file.

Nếu thiếu một hợp đồng, chỉ dùng đúng một prompt tương ứng trong [`repair-prompts.md`](repair-prompts.md). Không dán toàn bộ repair prompts và không yêu cầu viết lại tất cả nếu Tool vẫn có thể sửa theo phạm vi nhỏ.

## 3. Chạy smoke test Single

1. Chọn `SINGLE`, `SAFE`, `REFERENCE-FIRST`, `ECOMMERCE`.
2. Thêm một Product Source có chi tiết dễ kiểm như nếp gấp, đường may, sợi vải, họa tiết, chữ, đá, khóa hoặc phản chiếu.
3. Thêm Style Reference chứa một sản phẩm khác biệt rõ với sản phẩm cần sửa.
4. Chọn `ANALYZE`.
5. Kiểm tra Product Analysis chỉ mô tả sản phẩm mục tiêu.
6. Kiểm tra Reference Style Profile chỉ mô tả bề mặt nền, bảng màu, texture, ánh sáng, bóng tiếp xúc, mood, khoảng trống và bố cục tương thích.
7. Kiểm tra sản phẩm, đạo cụ, người, bao bì, chữ, logo, nhãn, brand mark và watermark trong reference đều nằm trong danh sách loại trừ.
8. Kiểm tra Tool hiển thị `Style source: REFERENCE IMAGE` và `Style Card: NONE — reference-driven`.
9. Chỉ duyệt tạo ảnh khi Product Lock đã chính xác.
10. Đặt original Product Source và output cạnh nhau để kiểm tra trước khi chấp nhận QA.

Nếu Product Analysis nhắc đến sản phẩm trong reference, dừng lại và dùng mục **Repair role contamination** trước khi test tiếp.

## 4. Test Strict Match

Giữ nguyên hai ảnh, chọn `STRICT MATCH`, sau đó chạy Safe lại.

Trước khi tạo ảnh, kiểm tra:

- match target bao gồm màu và phân bố sáng tối của nền, bề mặt/finish, tỷ lệ và mật độ texture, gradient hoặc vignette, độ rơi sáng, hướng/độ mềm ánh sáng, contrast, bóng tiếp xúc, mood và khoảng trống;
- vùng nền bị che hoặc mở rộng được ghi là reconstructed;
- Product Lock vẫn có độ ưu tiên cao hơn;
- không có Style Card được chọn;
- hiển thị `Pixel-exact guarantee: NO — generative visual match`.

Sau khi tạo, Strict Match chỉ nhận PASS khi ở độ phân giải kiểm tra không thấy sai khác quan trọng. PASS không bao giờ có nghĩa là giống từng pixel.

## 5. Test Batch Experimental

Không bắt đầu ngay bằng 20 sản phẩm thương mại. Trước tiên test cách ly bằng ba sản phẩm có hình dáng khác biệt rõ và có quyền sử dụng.

1. Chọn `BATCH EXPERIMENTAL`, `SAFE`, `REFERENCE-FIRST`, `ECOMMERCE`.
2. Giữ một Style Reference chung và thêm ba Product Source.
3. Phân tích Batch rồi kiểm tra Product Lock riêng cho từng hàng.
4. Chỉ duyệt những item đã READY.
5. Quan sát queue đến khi mỗi item đạt PASS, WARN, FAIL hoặc BLOCKED.
6. Xác nhận mỗi output chỉ thuộc một source và không phải collage.
7. Xác nhận một item lỗi/bị chặn không xóa hoặc dừng các item không liên quan.
8. Kiểm tra diagnostics: mỗi request chỉ có original Product Source của hàng đó cùng reference chung.
9. Dùng `Retry from Source` cho một item và xác nhận source identifier gốc không đổi.
10. Chỉ tăng số lượng Batch sau khi test ba item pass và đã lưu bằng chứng.

Hãy xem số lượng Batch lớn nhất mà bạn đã chạy thành công là giới hạn thực tế của snapshot Tool đó. Khoảng 2–20 là yêu cầu thiết kế, không phải cam kết rằng mọi tài khoản/runtime đều xử lý ổn định 20 item.

## 6. Mỗi lần chỉ sửa một nhóm lỗi

Mở [`repair-prompts.md`](repair-prompts.md) và chỉ chọn nhóm đang gặp:

- trộn vai trò ảnh;
- Product Lock;
- Reference-first hoặc Strict Match;
- cách ly Single/Batch;
- retry từ ảnh gốc;
- tuyên bố download;
- tách biệt giao diện.

Dán đúng block đó vào chat Tool Builder hiện tại. Sau khi Flow cập nhật, kiểm tra phần Code và Preview đã đổi, chạy lại case acceptance tương ứng, đồng thời chạy lại một smoke test từng pass để phát hiện regression.

## 7. Hoàn thành acceptance trước khi share

Copy [`acceptance-checklist.md`](acceptance-checklist.md) vào hồ sơ test hoặc điền trực tiếp trên working branch. Ghi lại:

- tên Tool và shared snapshot URL;
- bối cảnh tài khoản/gói, thông tin model được Flow hiển thị, ngày test và người test;
- input, thao tác, bằng chứng quan sát và trạng thái của từng case đã chạy;
- số lượng Batch lớn nhất đã quan sát hoạt động;
- warning đã biết và phần bắt buộc con người kiểm tra.

Giữ case chưa chạy ở `NOT RUN`. Test tự động trong repo không biến test hình ảnh thành PASS.

## 8. Download và kiểm tra file

Một thông báo thành công là chưa đủ. Với mỗi download:

1. bấm control Download đang hiển thị;
2. chờ tín hiệu hoàn thành thật từ trình duyệt hoặc Flow;
3. kiểm tra file mong đợi đã tồn tại trên máy;
4. mở file và xác nhận đúng sản phẩm/output đang chọn;
5. lưu tên file nếu hình được đưa vào workflow thương mại.

Nếu Download All hoặc ZIP không khả dụng, tải từng output. Không dựa vào đường dẫn giả, progress mô phỏng hoặc tuyên bố tự lưu chưa được kiểm chứng.

## 9. Share và cập nhật Tool

Chỉ share snapshot đã vượt qua các case cần thiết cho mode được duyệt. Người có link share có thể nhìn thấy tên, thumbnail và code do Tool sinh ra. Không đưa secret, instruction riêng tư, tên file mật hoặc dữ liệu khách hàng vào source của Tool.

Snapshot đã share có thể không tự cập nhật khi Tool gốc được chỉnh sửa. Sau một thay đổi builder/repair quan trọng:

1. chạy lại các acceptance case bị ảnh hưởng;
2. cập nhật ngày test và bằng chứng;
3. tạo snapshot/link mới nếu Flow yêu cầu;
4. ngừng dùng link cũ trong tài liệu nội bộ.

## Cách triển khai vào sản xuất

Bắt đầu bằng `SINGLE` Safe cho sản phẩm rủi ro cao, sau đó pilot Batch ba item. Bắt buộc so ảnh gốc/output bằng mắt đối với mọi hình thương mại. Tăng số lượng Batch từng bước và giữ phương án retouch truyền thống cho FAIL, repair thất bại nhiều lần, yêu cầu màu chính xác, chi tiết không đọc được hoặc sản phẩm không thể tách biên ổn định.
