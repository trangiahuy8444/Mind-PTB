# KẾ HOẠCH BÀI DẠY (GIÁO ÁN 120 PHÚT)
## BÀI 13: HÀM NÂNG CAO — THAM SỐ, ĐỐI SỐ, RETURN & PHẠM VI BIẾN
**Khóa học:** Lập trình Python Cơ Bản (`TT-C4K-PTB30`)  
**Thời lượng:** 120 phút  
**Giáo viên phụ trách:** Thầy Huy Trần  
**Học liệu tương tác đi kèm:** `LESSON 13/index.html` · Mã nguồn mẫu: `LESSON 13/bai13_ham_tham_so_pham_vi.py`

---

## I. MỤC TIÊU BÀI HỌC

### 1. Kiến thức
- Phân biệt rõ **Tham số (Parameter)** — tên biến đặt ở dòng `def` và **Đối số (Argument)** — giá trị thật truyền vào khi gọi hàm; biết sử dụng **tham số mặc định** (Default Parameter).
- Hiểu bản chất và sự khác biệt giữa **`print()`** (in ra màn hình rồi biến mất, hàm trả về `None`) và **`return`** (trả kết quả về để lưu vào biến hoặc tính toán tiếp).
- Thành thạo một số hàm tích hợp sẵn trong Python: `len()`, `abs()`, `round()`, `max()`, `min()`, `sum()`.
- Phân biệt rõ phạm vi biến: **Biến cục bộ (Local Variable)** — sống bên trong hàm và **Biến toàn cục (Global Variable)** — sống bên ngoài mọi hàm.

### 2. Kỹ năng
- Thiết kế hàm nhận dữ liệu đầu vào qua tham số và trả kết quả đầu ra bằng `return`.
- Phát hiện và sửa lỗi `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'` khi quên `return`, hoặc `NameError` khi gọi biến cục bộ ở ngoài hàm.
- Xây dựng hệ thống hàm cho **Động cơ Đấu Boss (Combat Engine)** làm bước đệm trực tiếp cho **Hackathon Buổi 14**.

### 3. Phẩm chất
- Tư duy thiết kế hàm độc lập, hạn chế lạm dụng biến toàn cục; chủ động lên ý tưởng cho dự án cuối khóa.

---

## II. LIÊN KẾT KIẾN THỨC

| Kiến thức các bài trước / sau | Sự liên kết với Bài 13 |
| :--- | :--- |
| Bài 1 & 2 – Biến & kiểu `NoneType` | Gặp lại hiện tượng không có `return` thì kết quả trả về là `None` |
| Bài 5 – Hàm `tinh_tien_dien_evn(kwh)` | Hiểu trọn vẹn ý nghĩa `def tinh_tien_dien_evn(kwh): ... return tong_cong` trong `bai5_on_tap.py`! |
| Bài 12 – Định nghĩa & gọi hàm cơ bản | Nâng cấp hàm từ không có đầu vào/đầu ra lên hàm có **Tham số + `return`** |
| **→ Buổi 14 (Hackathon Cuối Khóa)** | Hội tụ toàn bộ 13 bài (Biến, Ép kiểu, Toán tử, `if`, `for`/`while`, `list`, `str`, Hàm có tham số & `return`) để hoàn thành sản phẩm Demo Day! |

---

## III. TIẾN TRÌNH DẠY HỌC (120 PHÚT)

| Thời gian | Hoạt động | Nội dung & Phương pháp | Học liệu |
| :--- | :--- | :--- | :--- |
| **00' – 15'** | **HĐ1: Thí nghiệm "Máy Ép Hoa Quả" (`print` vs `return`)** | So sánh: `print()` giống như *nói to giá tiền*, còn `return` giống như *đưa chai nước ép cầm mang đi dùng tiếp*. Thử `kq = ham_chi_print(5)` → `kq + 10` bị `TypeError` với `NoneType`! | Tab 1 mục 1, 2 |
| **15' – 35'** | **HĐ2: Tham số, Đối số & Biến Cục Bộ / Toàn Cục** | Ẩn dụ: Biến toàn cục như *Tivi ngoài phòng khách* (ai cũng xem được); Biến cục bộ như *Bí mật trong balo của riêng hàm* (ra ngoài hàm là biến mất!). | Tab 1 mục 3, 4 |
| **35' – 55'** | **HĐ3: Scope & Return Visualizer** | HS mở Tab 2 chạy từng bước mô phỏng 2 vùng nhớ (Phòng khách Global & Balo Local) và so sánh trực tiếp `print` vs `return`. | Tab 2 – Scope Visualizer |
| **55' – 65'** | Nghỉ giải lao | | |
| **65' – 95'** | **HĐ4: Sprint – "Boss Battle Engine"** | HS viết 3 hàm `tinh_sat_thuong(cong, giap)`, `hoi_mau(hp, luong_hoi)` có `return` và ghép vào vòng lặp đấu Boss Rồng. | Tab 4 & Code Lab |
| **95' – 107'** | **HĐ5: Trắc nghiệm phản xạ** | HS làm 12 câu trên Tab 3. Chữa kỹ câu `NoneType`, tham số mặc định và shadowing biến cục bộ/toàn cục. | Tab 3 |
| **107' – 120'** | **HĐ6: Tổng kết toàn khóa & Công bố Hackathon Buổi 14** | Phổ biến 3 chủ đề dự án cuối khóa (Text-RPG / Chatbot / Shop Tycoon) và 4 tiêu chí chấm điểm Demo Day. | Tab 1 mục cầu nối |

---

## IV. NỘI DUNG TRỌNG TÂM & LỖI THƯỜNG GẶP

1. **Tham số (Parameter)** là biến khai báo trong `def ten_ham(a, b):`; **Đối số (Argument)** là giá trị thật truyền vào khi gọi `ten_ham(3, 5)`.
2. Hàm **không có `return`** (hoặc chỉ có `print`) mặc định trả về `None`. Nếu lấy kết quả đó đi cộng/nhân sẽ bị lỗi `TypeError`.
3. Mọi câu lệnh bên dưới `return` trong cùng một nhánh **không bao giờ chạy** (vì `return` thoát khỏi hàm ngay).
4. **Biến cục bộ (Local)** tạo bên trong hàm sẽ biến mất ngay khi hàm kết thúc — bên ngoài không gọi được.

| Lỗi thường gặp | Nguyên nhân | Cách khắc phục |
| :--- | :--- | :--- |
| `TypeError: unsupported operand for NoneType` | Lấy kết quả từ hàm chỉ dùng `print()` đem đi tính toán | Đổi `print(...)` bên trong hàm thành `return ...` |
| `NameError` khi in biến trong hàm ở ngoài hàm | Nhầm biến cục bộ là biến toàn cục | Trả giá trị đó ra ngoài bằng `return` |
| `SyntaxError: non-default argument follows default argument` | Đặt tham số mặc định đứng **trước** tham số bắt buộc | Tham số mặc định luôn đặt ở **phía sau cùng** |

---

## V. BÀI TẬP VỀ NHÀ & CHUẨN BỊ HACKATHON BUỔI 14

1. Viết hàm `kiem_tra_chan_le(n)` nhận số nguyên `n` và `return True` nếu chẵn, `False` nếu lẻ.
2. Viết hàm `tinh_dien_tich_hcn(dai, rong=1)` trả về `dai * rong`. Gọi thử cả trường hợp truyền 2 đối số và chỉ truyền 1 đối số.
3. Viết hàm `xep_loai(diem)` trả về chuỗi `"Gioi"`, `"Kha"`, `"Trung binh"`, hoặc `"Yeu"`.
4. Viết hàm `tinh_tien_dien(kwh)` dùng biểu giá 2 bậc (50 số đầu 1500đ, vượt 50 là 2000đ), `return` tổng tiền.
5. **Chuẩn bị Hackathon Buổi 14:** Chọn 1 trong 3 ý tưởng: *(1) Game Text-RPG Đấu Boss, (2) Trợ lý Chatbot thông minh, (3) Shop Quản Lý Cửa Hàng*, vẽ sơ đồ các hàm sẽ dùng vào vở!
