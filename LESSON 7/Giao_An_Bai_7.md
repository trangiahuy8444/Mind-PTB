# KẾ HOẠCH BÀI DẠY (GIÁO ÁN 120 PHÚT)
## BÀI 7: VÒNG LẶP VÔ HẠN (WHILE), BREAK & CONTINUE
**Khóa học:** Lập trình Python Cơ Bản (`TT-C4K-PTB30`)  
**Thời lượng:** 120 phút  
**Giáo viên phụ trách:** Thầy Huy Trần  
**Học liệu tương tác đi kèm:** `LESSON 7/index.html` · Mã nguồn mẫu: `LESSON 7/bai7_vong_lap_while.py`

---

## I. MỤC TIÊU BÀI HỌC

### 1. Kiến thức
- Phân biệt rõ **vòng lặp hữu hạn (`for`)** và **vòng lặp theo điều kiện / vô hạn (`while`)**.
- Hiểu cú pháp `while <điều_kiện>:`, cơ chế kiểm tra điều kiện trước mỗi lượt và nguyên nhân gây ra **vòng lặp vô hạn (Infinite Loop)**.
- Thành thạo 2 từ khóa điều khiển luồng: `break` (thoát hẳn khỏi vòng lặp) và `continue` (bỏ qua phần còn lại của lượt hiện tại, quay lại kiểm tra điều kiện).
- Nắm được cấu trúc `while True:` kết hợp `if ...: break` (mô hình Game Loop & kiểm tra nhập liệu) và `while` lồng nhau.
- Đọc và vẽ được **Sơ đồ khối (Flowchart)** của vòng lặp `while`.

### 2. Kỹ năng
- Biết sử dụng tổ hợp phím cứu hộ **`Ctrl + C`** trên Terminal khi chạy nhầm vòng lặp vô hạn.
- Chuyển đổi qua lại giữa `for` và `while` cho các bài toán đếm từ 1 đến n, đồng thời chọn đúng `while` cho bài toán chưa biết trước số lần lặp.
- Trace code từng bước khi có `break` và `continue`, tránh bẫy quên tăng biến đếm trước `continue`.

### 3. Phẩm chất
- Tư duy phòng vệ (Defensive Programming): luôn kiểm tra điều kiện dừng trước khi nhấn Run.
- Kiên trì tìm nguyên nhân logic khi chương trình "treo" hoặc chạy sai số lượt.

---

## II. LIÊN KẾT KIẾN THỨC

| Bài trước / Sau | Sự liên kết với Bài 7 |
| :--- | :--- |
| Bài 3 & Bài 4 – Biểu thức điều kiện `True`/`False`, sơ đồ khối | `while <điều_kiện>:` sử dụng chính các biểu thức so sánh/logic và hình thoi Flowchart đã học |
| Bài 5 – Kiểm tra tính hợp lệ dữ liệu | Dùng `while` bắt người dùng nhập lại khi dữ liệu sai (ví dụ: `kwh < 0`) |
| Bài 6 – Vòng lặp `for` & `range()` | So sánh `for` (biết trước số lần lặp) vs `while` (lặp cho đến khi điều kiện sai) |
| **→ Bài 8** | Vận dụng toàn bộ kiến thức (Biến, Ép kiểu, Toán tử, `if`, `for`, `while True`) vào dự án game **Sinh Tồn Trên Hoang Đảo** |

---

## III. TIẾN TRÌNH DẠY HỌC (120 PHÚT)

| Thời gian | Hoạt động | Nội dung & Phương pháp | Học liệu |
| :--- | :--- | :--- | :--- |
| **00' – 15'** | **HĐ1: Khởi động – "Virus treo máy" & Ctrl+C** | GV chạy thử đoạn `while True: print("MindX")` trên máy chiếu để HS thấy màn hình chạy liên tục, sau đó dạy phím cứu hộ `Ctrl + C`. Đặt vấn đề so sánh với `for` Bài 6: *"Nhập mật khẩu đến khi đúng dùng `for` được không?"* | Terminal + Tab 1 mục 1 |
| **15' – 35'** | **HĐ2: Cú pháp `while` & Sơ đồ khối** | Phân tích 3 mảnh ghép sống còn của `while`: **Khởi tạo – Điều kiện – Cập nhật**. Vẽ Flowchart vòng quay từ thân lệnh quay ngược lên hình thoi điều kiện. | Tab 1 mục 2, 3 |
| **35' – 55'** | **HĐ3: `break`, `continue` & While-Loop Tracer** | Mở Tab 2 chạy While Tracer ở 4 chế độ (`count`, `password`, `break`, `continue`). Chỉ ra điểm khác biệt giữa `break` và `continue`, đặc biệt bẫy `continue` đứng trước `i += 1`. | Tab 2 – Tracer |
| **55' – 65'** | **HĐ4: Thử thách Mini Game Đoán Số** | HS chơi thử Game Đoán Số 1–50 ngay trên Tab 2, sau đó đọc xem Game Loop dùng `while True:` và `break` ra sao. | Tab 2 – Mini Game |
| **65' – 70'** | Nghỉ giải lao | | |
| **70' – 100'** | **HĐ5: Thực hành có hướng dẫn** | HS làm Bài 1 → 5 trên Code Lab / VS Code: nhập đến `-1` thì dừng, đăng nhập mật khẩu giới hạn 3 lần, tính tổng các số nhập vào, kiểm tra số nguyên dương hợp lệ. | Tab 4 & Code Lab |
| **100' – 112'** | **HĐ6: Trắc nghiệm phản xạ** | HS làm 12 câu trên Tab 3. GV chữa các câu hay nhầm giữa `break`/`continue` và vòng lặp vô hạn. | Tab 3 |
| **112' – 120'** | **HĐ7: Tổng kết & cầu nối Bài 8** | Chốt bảng chọn `for` vs `while`. Giới thiệu dự án Studio Game **Sinh Tồn Trên Hoang Đảo** ở Bài 8. | Tab 1 mục cầu nối |

---

## IV. NỘI DUNG TRỌNG TÂM & LỖI THƯỜNG GẶP

1. `while <điều_kiện>:` lặp **chừng nào điều kiện còn `True`**. Khi điều kiện thành `False`, vòng lặp kết thúc.
2. `while True:` tạo vòng lặp vô hạn có chủ đích — **bắt buộc** phải có nhánh `if ...: break` ở bên trong để thoát ra.
3. `break`: nhảy ra **khỏi hẳn** vòng lặp ngay lập tức.
4. `continue`: bỏ qua các dòng còn lại **của lượt hiện tại**, nhảy lên kiểm tra lại điều kiện `while` cho lượt mới.

| Lỗi thường gặp | Nguyên nhân | Cách khắc phục |
| :--- | :--- | :--- |
| Chương trình chạy mãi không dừng | Quên cập nhật biến điều kiện (`i += 1`) hoặc điều kiện luôn `True` | Nhấn `Ctrl + C`; kiểm tra lại câu lệnh làm thay đổi biến điều kiện |
| Treo máy khi dùng `continue` | Đặt `continue` nằm **trước** dòng `i += 1` | Luôn cập nhật biến `i += 1` trước khi gọi `continue` |
| Nhầm `=` và `==` trong điều kiện `while` | Viết `while n = 0:` | Sửa thành `while n == 0:` hoặc `while n != 0:` |
| Quên ép kiểu khi nhập điều kiện dừng | `n = input()` so sánh với `-1` (`"-1" != -1` luôn `True`) | Bọc `int(input())` |

---

## V. BÀI TẬP VỀ NHÀ

1. Dùng `while` in tất cả các số chia hết cho 3 từ 1 đến `n`.
2. Viết chương trình máy tính cộng dồn: liên tục yêu cầu người dùng nhập số, cộng vào tổng; khi nhập `0` thì dừng và in tổng cuối cùng.
3. Viết chương trình yêu cầu nhập điểm thi hợp lệ (từ `0` đến `10`). Nếu nhập sai (âm hoặc `> 10`), thông báo lỗi và bắt nhập lại cho đến khi hợp lệ.
4. Viết hệ thống khóa thẻ ATM: mật khẩu đúng là `"2468"`. Cho phép nhập tối đa 3 lần; đúng thì in `"Mở khóa thành công"`, sai hết 3 lần thì in `"Thẻ đã bị khóa!"`.
5. *(Nâng cao)* Viết game Đoán Số Bí Mật (từ 1 đến 100) với tối đa 7 lượt đoán, gợi ý `"Lớn hơn"` hoặc `"Nhỏ hơn"` sau mỗi lượt.
