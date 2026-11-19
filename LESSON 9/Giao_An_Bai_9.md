# KẾ HOẠCH BÀI DẠY (GIÁO ÁN 120 PHÚT)
## BÀI 9: KIỂM TRA VÒNG LẶP & NHẬP MÔN DANH SÁCH (LIST)
**Khóa học:** Lập trình Python Cơ Bản (`TT-C4K-PTB30`)  
**Thời lượng:** 120 phút  
**Giáo viên phụ trách:** Thầy Huy Trần  
**Học liệu tương tác đi kèm:** `LESSON 9/index.html` · Mã nguồn mẫu: `LESSON 9/bai9_on_vong_lap_va_list.py`

---

## I. MỤC TIÊU BÀI HỌC

### 1. Kiến thức
- Củng cố và kiểm tra năng lực sử dụng vòng lặp `for` / `while`, `break` / `continue` (Checkpoint 2).
- Hiểu định nghĩa **Danh sách (`list`)**: cấu trúc dữ liệu lưu nhiều giá trị có thứ tự trong cặp ngoặc vuông `[...]`.
- Nắm vững quy tắc **chỉ số bắt đầu từ 0 (Zero-based indexing)** và **chỉ số âm (`-1`, `-2`, ...)** đếm từ cuối danh sách.
- Hiểu hàm `len(ds)`, toán tử thành viên `in` / `not in` và nguyên nhân lỗi `IndexError: list index out of range`.
- Phân biệt **2 cách duyệt List bằng `for`**: duyệt trực tiếp phần tử vs duyệt qua chỉ số `range(len(ds))`.

### 2. Kỹ năng
- Khởi tạo danh sách số, chuỗi, danh sách rỗng `[]`.
- Truy xuất đúng phần tử đầu (`ds[0]`), cuối (`ds[-1]`), giữa (`ds[len(ds)//2]`).
- Viết vòng lặp duyệt List để tính tổng, trung bình, tìm phần tử lớn nhất/nhỏ nhất và đếm phần tử thỏa điều kiện.

### 3. Phẩm chất
- Tư duy tổ chức dữ liệu khoa học, tránh đếm nhầm "lệch 1" giữa số thứ tự đời thường (bắt đầu từ 1) và chỉ số lập trình (bắt đầu từ 0).

---

## II. LIÊN KẾT KIẾN THỨC

| Kiến thức các bài trước / sau | Sự liên kết với Bài 9 |
| :--- | :--- |
| Bài 6 & 7 – Vòng lặp `for` & `while` | Đánh giá Checkpoint 2; dùng `for` duyệt từng phần tử trong List |
| Bài 4 – Tìm `max` & câu điều kiện `if` | Tìm giá trị lớn nhất trong cả danh sách nhiều số (`lon_nhat = ds[0]`) |
| Bài 8 – Game Hoang Đảo | Nâng cấp từ biến đơn lẻ sang `balo = [...]` chứa nhiều món đồ |
| **→ Bài 10** | Học cách **Thêm, Xóa, Sửa, Sắp xếp** danh sách động (`.append()`, `.insert()`, `.remove()`, `.pop()`) |

---

## III. TIẾN TRÌNH DẠY HỌC (120 PHÚT)

| Thời gian | Hoạt động | Nội dung & Phương pháp | Học liệu |
| :--- | :--- | :--- | :--- |
| **00' – 30'** | **HĐ1: Checkpoint 2 – Săn Bug Vòng Lặp** | HS làm 3 câu kiểm tra nhanh: (1) Tổng các số chẵn 1..n, (2) Sửa vòng lặp treo máy, (3) ATM 3 lần sai. GV chấm nhanh & chữa lỗi chung. | Phần Checkpoint Tab 1 |
| **30' – 45'** | **HĐ2: Trò chơi "Toa Tàu Số 0"** | 5–6 HS xếp hàng ngang. GV dán số thứ tự `0, 1, 2, 3, 4` lên trước và `-5..-1` bên dưới để HS hiểu ngay index dương & index âm. Hỏi chỉ số 5 → cả lớp hô *"IndexError!"*. | Tab 1 mục 2 + Tab 2 |
| **45' – 65'** | **HĐ3: List Index Visualizer & 2 Cách Duyệt** | HS mở Tab 2 thử tra cứu `ds[idx]`, cố tình nhập `idx = 10` để quan sát `IndexError`. Chạy bộ mô phỏng 2 cách duyệt `for x in ds` và `for i in range(len(ds))`. | Tab 2 – Visualizer |
| **65' – 70'** | Nghỉ giải lao | | |
| **70' – 100'** | **HĐ4: Thực hành "Thanh Tra Túi Đồ"** | HS làm Bài 1 → 5 trên Code Lab / VS Code: khởi tạo danh sách lớp, in phần tử đầu/giữa/cuối, tính tổng/điểm TB, tìm `max` không dùng hàm `max()`, kiểm tra tồn tại bằng `in`. | Tab 4 & Code Lab |
| **100' – 112'** | **HĐ5: Trắc nghiệm phản xạ** | HS làm 12 câu trên Tab 3. Chữa các câu bẫy chỉ số `len(ds)` vs `len(ds) - 1`. | Tab 3 |
| **112' – 120'** | **HĐ6: Tổng kết & cầu nối Bài 10** | Đặt vấn đề: *"Làm sao khi chơi game nhặt thêm món đồ mới hoặc vứt món cũ ra khỏi `balo`?"* → Hẹn gặp ở **Bài 10**! | Tab 1 mục cầu nối |

---

## IV. NỘI DUNG TRỌNG TÂM & LỖI THƯỜNG GẶP

1. Chỉ số phần tử đầu tiên luôn là `0`; phần tử cuối cùng là `len(ds) - 1` hoặc `-1`.
2. Danh sách có `N` phần tử chỉ có chỉ số dương hợp lệ từ `0` đến `N - 1`.
3. Cách duyệt 1 (`for x in ds:`) dùng khi chỉ cần giá trị; Cách duyệt 2 (`for i in range(len(ds)):`) dùng khi cần cả **vị trí `i`** (ví dụ in số thứ tự hoặc sửa phần tử).

| Lỗi thường gặp | Nguyên nhân | Cách khắc phục |
| :--- | :--- | :--- |
| `IndexError: list index out of range` | Truy cập `ds[len(ds)]` hoặc chỉ số vượt quá độ dài | Chỉ số lớn nhất là `len(ds) - 1` (hoặc dùng `ds[-1]`) |
| Nhầm thứ tự số 1 là `ds[1]` | Quên chỉ số bắt đầu từ `0` | Phần tử đầu tiên là `ds[0]` |
| Khởi tạo `lon_nhat = 0` khi tìm max của list số âm | `[-5, -2, -9]` sẽ ra sai là `0` | Luôn khởi tạo `lon_nhat = ds[0]` |

---

## V. BÀI TẬP VỀ NHÀ

1. Tạo danh sách 5 món ăn yêu thích. In ra món đầu tiên, món ở giữa và món cuối cùng bằng chỉ số âm.
2. Cho danh sách `so = [12, 7, 25, 8, 19, 4]`. Dùng `for` đếm có bao nhiêu số lẻ và tính tổng các số chẵn.
3. Nhập tên một bạn bất kỳ, kiểm tra xem bạn đó có trong danh sách lớp `["An", "Bình", "Chi", "Dũng"]` không (dùng `in`).
4. Tìm phần tử **nhỏ nhất** trong danh sách `[-3, 15, -10, 4, 0]` mà không dùng hàm `min()`.
5. *(Nâng cao)* Duyệt một danh sách số và tạo ra bảng sao nhân đôi giá trị tại chỗ bằng `for i in range(len(ds)): ds[i] = ds[i] * 2`.
