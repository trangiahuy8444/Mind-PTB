# KẾ HOẠCH BÀI DẠY (GIÁO ÁN 120 PHÚT)
## BÀI 6: VÒNG LẶP FOR & HÀM RANGE()
**Khóa học:** Lập trình Python Cơ Bản (`TT-C4K-PTB30`)  
**Thời lượng:** 120 phút  
**Giáo viên phụ trách:** Thầy Huy Trần  
**Học liệu tương tác đi kèm:** `LESSON 6/index.html` · Mã nguồn mẫu: `LESSON 6/bai6_vong_lap_for.py`

---

## I. MỤC TIÊU BÀI HỌC

### 1. Kiến thức
- Hiểu khái niệm **vòng lặp** và **lượt lặp (iteration)**; biết khi nào cần dùng vòng lặp thay cho việc lặp lại code thủ công.
- Nắm vững cú pháp `for <biến> in <dãy>:` cùng quy tắc **dấu hai chấm** và **thụt lề** (liên hệ trực tiếp với `if` ở Bài 4).
- Thành thạo **3 dạng** `range(stop)`, `range(start, stop)`, `range(start, stop, step)`, kể cả step âm; nhớ quy tắc **"không lấy stop"**.
- Hiểu và sử dụng **biến tích lũy**: tổng (khởi tạo `0`), đếm (khởi tạo `0`), tích (khởi tạo `1`) cùng các toán tử `+=`, `*=`.
- Biết duyệt từng ký tự của chuỗi bằng `for`.

### 2. Kỹ năng
- Trace code từng lượt lặp: theo dõi giá trị biến lặp `i` và biến tích lũy trong RAM.
- Kết hợp `for` + `if` để lọc/đếm theo điều kiện.
- Nhận diện và sửa các lỗi: hụt 1 (`range(1, n)`), dãy rỗng (`range(5, 1)`), `step = 0`, khởi tạo biến tích lũy sai chỗ, thụt lề `print` sai.

### 3. Phẩm chất
- Tư duy tự động hóa: "Việc lặp lại → để máy làm".
- Cẩn thận với biên của dãy số, kiên nhẫn khi trace code.

---

## II. LIÊN KẾT KIẾN THỨC

| Bài trước | Được dùng lại trong Bài 6 |
| :--- | :--- |
| Bài 1 – `print()`, biến, bảng cửu chương 98 | Bài toán mở đầu: 10 dòng `print` → 2 dòng `for` |
| Bài 2 – `int()`, `float()`, chuỗi `str` | Nhập `n`, nhập kWh; duyệt từng ký tự chuỗi |
| Bài 3 – Toán tử `%`, `*`, `+` | `i % 2 == 0`, `"*" * i`, `tong + i` |
| Bài 4 – `if`, dấu `:`, thụt lề, tìm max | `for` + `if`, cùng quy tắc cú pháp, tìm tháng tốn tiền nhất |
| Bài 5 – Bài toán tiền điện bậc thang | Tính tổng tiền điện 12 tháng |
| **→ Bài 7** | `while`, `break`, `continue` – lặp khi **không biết trước số lần** |

---

## III. TIẾN TRÌNH DẠY HỌC (120 PHÚT)

| Thời gian | Hoạt động | Nội dung & Phương pháp | Học liệu |
| :--- | :--- | :--- | :--- |
| **00' – 10'** | **HĐ1: Khởi động – "Thử thách 1000 dòng"** | Chiếu lại code bảng cửu chương 98 của Bài 1. Hỏi: *"Nếu in đến 98 × 1000 thì sao?"* → Học sinh nhận ra nhu cầu lặp. Giới thiệu đáp án 2 dòng `for`. | Tab 1 – mục 1 |
| **10' – 30'** | **HĐ2: Giải phẫu cú pháp & `range()`** | Phân tích từng thành phần `for i in range(1, 11):`. So sánh dấu `:` & thụt lề với `if`. Bảng 3 dạng `range()`; cho học sinh đoán nhanh dãy số của 5 ví dụ trước khi xem đáp án. Nhấn mạnh 3 bẫy. | Tab 1 – mục 2, 3 |
| **30' – 50'** | **HĐ3: Mô phỏng For-Loop Tracer** | Học sinh mở Tab 2, chạy chương trình "In ra từng giá trị i" với `range(1, 6, 1)`, rồi thử: `range(0, 10, 3)`, `range(10, 0, -2)`, `range(5, 1, 1)` (dãy rỗng), `step = 0` (lỗi). Quan sát ô sáng trên dãy, dòng code sáng, RAM, màn hình. | Tab 2 – Tracer |
| **50' – 65'** | **HĐ4: Biến tích lũy** | Ẩn dụ "chiếc giỏ": khởi tạo – cập nhật – dùng kết quả. Trace chương trình "Tính tổng" và "Đếm số chẵn" trên Tracer. Thảo luận: đặt `tong = 0` trong vòng lặp thì sao? Tại sao tích phải khởi tạo `1`? | Tab 1 – mục 4; Tab 2 |
| **65' – 70'** | Nghỉ giải lao | | |
| **70' – 100'** | **HĐ5: Thực hành có hướng dẫn** | Học sinh làm Bài 1 → 5 trên Code Lab hoặc Thonny/VS Code. GV đi kèm, chữa lỗi thường gặp. Học sinh khá làm thêm Bài 6 (tiền điện cả năm). | Tab 4; Tab 2 – Code Lab |
| **100' – 112'** | **HĐ6: Trắc nghiệm phản xạ** | Học sinh làm 12 câu trên Tab 3. GV chữa các câu sai nhiều (thường là câu 2, 6, 7, 8). | Tab 3 |
| **112' – 120'** | **HĐ7: Tổng kết & cầu nối Bài 7** | Chốt: *for = lặp khi biết trước số lần*. Đặt vấn đề: *"Nhập mật khẩu đến khi đúng thì làm sao?"* → Bài 7 `while`. Giao bài tập về nhà. | Tab 1 – mục cầu nối |

---

## IV. NỘI DUNG TRỌNG TÂM CẦN CHỐT

1. `for i in range(a, b, c):` — `i` lần lượt nhận các giá trị từ `a`, cộng thêm `c` mỗi lần, **dừng trước `b`**.
2. Muốn chạy từ 1 đến n: `range(1, n + 1)`.
3. Dòng **thụt lề** chạy mỗi lượt; dòng **không thụt lề** chạy 1 lần sau vòng lặp.
4. Biến tích lũy: khởi tạo **trước** vòng lặp, cập nhật **trong**, dùng kết quả **sau**.
5. Tổng/đếm khởi tạo `0`; tích khởi tạo `1`.

### Lỗi thường gặp & cách sửa

| Lỗi | Ví dụ sai | Sửa |
| :--- | :--- | :--- |
| Quên dấu `:` | `for i in range(5)` | `for i in range(5):` |
| Hụt 1 | `range(1, n)` khi cần đến n | `range(1, n + 1)` |
| Khởi tạo trong vòng lặp | `for ...: tong = 0; tong += i` | Đưa `tong = 0` lên trước `for` |
| `print` kết quả bị thụt lề | In ra nhiều tổng dở dang | Bỏ thụt lề dòng `print` |
| Đếm ngược thiếu step âm | `range(10, 0)` → rỗng | `range(10, 0, -1)` |
| Tích khởi tạo 0 | `tich = 0` → luôn ra 0 | `tich = 1` |

---

## V. BÀI TẬP VỀ NHÀ

1. In tất cả số lẻ từ 1 đến 99 trên cùng một dòng (gợi ý: `print(i, end=" ")`).
2. Nhập `n`, tính tổng các số chia hết cho 3 **hoặc** 5 từ 1 đến n (`n = 10` → `3+5+6+9+10 = 33`).
3. Nhập một chuỗi, đếm số chữ `a` (cả hoa lẫn thường) trong chuỗi.
4. Nhập điểm của 5 bạn, in điểm trung bình và số bạn đạt từ 8.0 trở lên.
5. *(Nâng cao)* In tam giác sao ngược chiều cao h (dòng đầu h sao, dòng cuối 1 sao) bằng `range` với step âm.
