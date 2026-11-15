# KẾ HOẠCH BÀI DẠY (GIÁO ÁN 60 PHÚT)
## BÀI 5: ÔN TẬP TỔNG HỢP (BIẾN, KIỂU DỮ LIỆU, TOÁN TỬ & CÂU ĐIỀU KIỆN)
**Khóa học:** Lập trình Python Cơ Bản (`TT-C4K-PTB30`)  
**Thời lượng:** 60 phút  
**Giáo viên phụ trách:** Thầy Huy Trần  
**Học liệu tương tác đi kèm:** [interactive_review_lesson5.html](file:///Users/huytran/Library/CloudStorage/GoogleDrive-trangiahuy8444@gmail.com/My%20Drive/01_Giang_day/TT-C4K-PTB30/LESSON%205/interactive_review_lesson5.html) (hoặc `index.html`)

---

## I. MỤC TIÊU BÀI HỌC

### 1. Kiến thức
- Khắc sâu bản chất **4 trụ cột nền tảng**: Biến & gán giá trị (`=`), các kiểu dữ liệu cơ bản (`int`, `float`, `str`, `bool`), hệ thống toán tử (số học, so sánh `==`, logic `and`/`or`/`not`) và các dạng cấu trúc rẽ nhánh (`if`, `if-else`, `if-elif-else`).
- Thành thạo đọc, vẽ và phân tích **Sơ đồ khối (Flowchart)** theo tiêu chuẩn quốc tế: Khối Oval (Bắt đầu/Kết thúc), Hình bình hành (Nhập/Xuất), Hình thoi (Điều kiện), Hình chữ nhật (Tính toán).
- Làm chủ phương pháp giải **Bài toán tính tiền điện sinh hoạt bậc thang EVN** (Bài toán kinh điển kết hợp toán học thực tế và tư duy lập trình lũy tiến).

### 2. Kỹ năng
- Nhận diện và sửa ngay 3 lỗi kinh điển: Quên ép kiểu với `input()`, nhầm `=` với `==`, và lỗi thụt lề `IndentationError`.
- Kỹ năng "Trace code" (lần vết thực thi từng dòng lệnh) kết hợp quan sát biến động của giá trị trong bộ nhớ RAM và luồng di chuyển trên sơ đồ khối.
- Kỹ năng tư duy giải quyết vấn đề thực tiễn thông qua việc chia nhỏ bài toán bậc thang.

### 3. Phẩm chất & Thái độ
- Phát triển tư duy logic chặt chẽ, tính cẩn thận, chính xác khi viết cú pháp code.
- Hứng thú và chủ động khám phá qua công cụ tương tác trực quan (Interactive Web Simulator).

---

## II. THỜI LƯỢNG & TIẾN TRÌNH DẠY HỌC (60 PHÚT)

| Mốc thời gian | Hoạt động | Nội dung & Phương pháp sư phạm | Học liệu / Công cụ |
| :--- | :--- | :--- | :--- |
| **00' - 10'** (10 phút) | **Hoạt động 1: Khởi động & Rà soát 4 trụ cột** | - Chiếu bản đồ 4 trụ cột kiến thức trên web app.<br>- Đặt câu hỏi gợi mở nhanh: Tại sao `a = "10" + "20"` lại ra `"1020"` chứ không phải `30`?<br>- Rà soát 3 cạm bẫy học sinh hay mắc. | Tab 1: *Lý Thuyết & Trọng Tâm* |
| **10' - 25'** (15 phút) | **Hoạt động 2: Mổ xẻ Sơ đồ khối & Bài toán Tiền Điện EVN** | - Giới thiệu 4 ký hiệu sơ đồ khối tiêu chuẩn.<br>- **Phân tích thực tế:** Tại sao tiền điện không nhân cào bằng? (Mô hình xô nước bậc thang).<br>- Phân tích công thức lũy tiến cho từng bậc: Bậc 1 (<=50), Bậc 2 (<=100), Bậc 3 (<=200), Bậc 4 (<=300), Bậc 5 (>300).<br>- Thử nghiệm nhanh trên công cụ tính tiền điện trực quan. | Bảng biểu giá điện & *Mô hình xô nước bậc thang* |
| **25' - 45'** (20 phút) | **Hoạt động 3: Thực hành mô phỏng (Simulator Lab)** | - Giáo viên hướng dẫn học sinh mở Tab 2: *Mô Phỏng Sơ Đồ Khối & Code*.<br>- Học sinh chạy trace code từng bước với bài toán tiền điện (thử các test: 35 kWh, 80 kWh, 125 kWh, 250 kWh, 350 kWh).<br>- Quan sát đồng bộ: Sơ đồ khối sáng viền -> Code nhảy dòng -> Bộ nhớ RAM cập nhật -> Lời thầy giảng giải xuất hiện.<br>- Thử nghiệm các bài toán bổ trợ: Chẵn lẻ âm dương, Xếp loại học lực, Tam giác logic. | Tab 2: *Mô Phỏng Tương Tác Sơ Đồ Khối & Code* |
| **45' - 55'** (10 phút) | **Hoạt động 4: Thử thách phản xạ trắc nghiệm** | - Học sinh tự làm 8 câu hỏi trắc nghiệm tương tác trên Tab 3.<br>- Xem phản hồi đúng/sai và lời giải thích bản chất tức thì.<br>- Giáo viên giải đáp các câu học sinh sai nhiều nhất (đặc biệt câu bẫy thứ tự elif và bẫy tính tiền điện 70 kWh). | Tab 3: *Thử Thách & Trắc Nghiệm* |
| **55' - 60'** (5 phút) | **Hoạt động 5: Tổng kết & Dặn dò về nhà** | - Nhắc lại thông điệp: "Luôn vẽ sơ đồ khối trước khi code bài toán rẽ nhánh phức tạp".<br>- Giao bài tập về nhà trong file `bai5_on_tap.py`. | Slide / Web / File code mẫu |

---

## III. CHI TIẾT NỘI DUNG GIẢNG DẠY BÀI TOÁN TÍNH TIỀN ĐIỆN BẬC THANG

### 1. Bảng giá điện sinh hoạt EVN quy chuẩn:
- **Bậc 1 (0 - 50 kWh):** 1.806 đồng/kWh (Tối đa 50 kWh đầu: $50 \times 1.806 = 90.300$ đ)
- **Bậc 2 (51 - 100 kWh):** 1.866 đồng/kWh (Tối đa 50 kWh kế: $50 \times 1.866 = 93.300$ đ)
- **Bậc 3 (101 - 200 kWh):** 2.167 đồng/kWh (Tối đa 100 kWh kế: $100 \times 2.167 = 216.700$ đ)
- **Bậc 4 (201 - 300 kWh):** 2.729 đồng/kWh (Tối đa 100 kWh kế: $100 \times 2.729 = 272.900$ đ)
- **Bậc 5 (Trên 300 kWh):** 3.050 đồng/kWh
- **Thuế VAT:** 8%

### 2. Ví dụ mẫu giảng giải cho học sinh (Trường hợp 125 kWh):
1. **Lỗi học sinh hay làm:** $125 \times 2.167 = 270.875$ đ $\rightarrow$ **SAI!**
2. **Cách tính lũy tiến chuẩn:**
   - 50 kWh đầu hưởng Bậc 1: $50 \times 1.806 = 90.300$ đ
   - 50 kWh kế hưởng Bậc 2: $50 \times 1.866 = 93.300$ đ
   - $125 - 100 = 25$ kWh còn lại hưởng Bậc 3: $25 \times 2.167 = 54.175$ đ
   - **Tổng tiền chưa thuế:** $90.300 + 93.300 + 54.175 = 237.775$ đ
   - **Thuế VAT (8%):** $237.775 \times 0.08 = 19.022$ đ
   - **Tổng thanh toán:** $237.775 + 19.022 = 256.797$ đ

---

## IV. BẢN MÃ NGUỒN PYTHON CHUẨN ĐỂ HỌC SINH THỰC HÀNH

Tệp mã nguồn hoàn chỉnh đã được lưu tại:  
`LESSON 5/bai5_on_tap.py`

Học sinh có thể mở tệp này bằng bất kỳ trình soạn thảo nào (IDLE, VS Code, Thonny, PyCharm) để chạy thử nghiệm các bộ test case.
