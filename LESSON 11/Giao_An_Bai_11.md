# KẾ HOẠCH BÀI DẠY (GIÁO ÁN 120 PHÚT)
## BÀI 11: XÂU KÝ TỰ (STRING) — CẮT CHUỖI & MẬT MÃ ĐIỆP VIÊN
**Khóa học:** Lập trình Python Cơ Bản (`TT-C4K-PTB30`)  
**Thời lượng:** 120 phút  
**Giáo viên phụ trách:** Thầy Huy Trần  
**Học liệu tương tác đi kèm:** `LESSON 11/index.html` · Mã nguồn mẫu: `LESSON 11/bai11_xau_ky_tu.py`

---

## I. MỤC TIÊU BÀI HỌC

### 1. Kiến thức
- Hiểu xâu ký tự (`str`) là một dãy các ký tự có thứ tự (giống List ở việc truy xuất `s[i]`, `len(s)`, `for c in s`, `in`).
- Nắm vững tính **bất biến (Immutable)** của `str`: không thể sửa trực tiếp `s[0] = "K"` (gây `TypeError`), muốn đổi phải tạo chuỗi mới.
- Thành thạo kỹ thuật **cắt lát xâu (Slicing)**: `s[start:stop:step]`, cắt thiếu tham số (`s[:5]`, `s[3:]`) và tuyệt chiêu đảo ngược `s[::-1]`.
- Biết sử dụng các phương thức xử lý văn bản: `.strip()`, `.upper()`, `.lower()`, `.replace()`, `.split()`, `.join()`.
- Hiểu cách chuyển đổi ký tự ↔ mã ASCII với `ord()` và `chr()` để cài đặt **Mật mã Caesar**.

### 2. Kỹ năng
- Cắt chính xác một đoạn xâu con theo chỉ số dương và âm.
- Chuẩn hóa dữ liệu văn bản người dùng nhập (bỏ khoảng trắng thừa, đưa về chữ thường).
- Viết chương trình đếm từ, lọc từ nhạy cảm, kiểm tra xâu đối xứng (Palindrome) và mã hóa/giải mã mật thư.

### 3. Phẩm chất
- Cẩn thận với chỉ số dừng `stop` khi slicing (vẫn giữ quy tắc **không lấy `stop`** như `range()`).
- Thích thú khám phá ứng dụng an toàn thông tin cơ bản qua mật mã học.

---

## II. LIÊN KẾT KIẾN THỨC

| Kiến thức các bài trước / sau | Sự liên kết với Bài 11 |
| :--- | :--- |
| Bài 2 – Kiểu dữ liệu `str` | Mở rộng sâu về các thao tác trên kiểu chuỗi ký tự |
| Bài 6 – `range(start, stop, step)` & `for c in s` | Cú pháp cắt xâu `s[start:stop:step]` dùng chung logic biên `start`, `stop`, `step` với `range()`! |
| Bài 9 & 10 – Danh sách (`list`) | So sánh `list` (Mutable — sửa được tại chỗ) vs `str` (Immutable — bất biến), và kết nối hai kiểu qua `.split()` / `.join()` |
| **→ Bài 12** | Khi các đoạn code mã hóa/xử lý chuỗi dài dần và phải dùng lại nhiều nơi → học **Hàm (`def`)** ở Bài 12 để đóng gói tái sử dụng! |

---

## III. TIẾN TRÌNH DẠY HỌC (120 PHÚT)

| Thời gian | Hoạt động | Nội dung & Phương pháp | Học liệu |
| :--- | :--- | :--- | :--- |
| **00' – 15'** | **HĐ1: Hook – Giải mã mật thư Sherlock Holmes** | GV chiếu chuỗi `"nohtyP XdniM uêy iôT"` và giải mã chỉ bằng 1 biểu thức `s[::-1]`. Hỏi: *"Ký tự đầu lấy được bằng `s[0]`, vậy sửa `s[0] = 'K'` được không?"* → Demo `TypeError`. | Tab 1 mục 1 |
| **15' – 35'** | **HĐ2: Cắt lát Slicing `s[start:stop:step]`** | Liên hệ `start:stop:step` với `range()` Bài 6. Thực hành trên ví dụ `"MindX Python"`: `s[0:5]`, `s[6:]`, `s[::-1]`. | Tab 1 mục 2 |
| **35' – 55'** | **HĐ3: String Slicer & Mật Mã Caesar Lab** | HS mở Tab 2 thử kéo `start`, `stop`, `step` quan sát ô ký tự sáng lên; thử bộ phương thức `.strip()`, `.split()`, `.replace()` và mã hóa/giải mã thông điệp bằng Caesar Cipher. | Tab 2 – Slicer & Caesar |
| **55' – 65'** | Nghỉ giải lao | | |
| **65' – 100'** | **HĐ4: Sprint – Cyber Security Decoder** | HS hoàn thành Bài 1 → 5 trên Code Lab / VS Code: đếm số từ & ký tự, kiểm tra đối xứng, biến hình chữ `a→@`, bộ lọc từ cấm và mật mã Caesar. | Tab 4 & Code Lab |
| **100' – 112'** | **HĐ5: Trắc nghiệm phản xạ** | HS làm 12 câu trên Tab 3. Chữa kỹ bẫy `str` bất biến và chỉ số `stop` không được lấy khi slicing. | Tab 3 |
| **112' – 120'** | **HĐ6: Tổng kết & cầu nối Bài 12** | Đặt vấn đề: *"Mỗi lần cần mã hóa một câu lại phải chép lại 8 dòng vòng lặp Caesar thì quá dài — làm sao đóng gói thành 1 lệnh gọn như `print()`?"* → **Bài 12: Hàm (`def`)**! | Tab 1 mục cầu nối |

---

## IV. NỘI DUNG TRỌNG TÂM & LỖI THƯỜNG GẶP

1. `str` mang tính **bất biến (Immutable)** — mọi phương thức như `.upper()`, `.replace()` đều **trả về chuỗi mới**, không tự sửa chuỗi cũ nếu không gán lại (`s = s.upper()`).
2. Slicing `s[start:stop:step]`: lấy từ `start` đến `stop - 1`. Khi `step = -1`, đọc ngược từ cuối về đầu (`s[::-1]`).
3. `.split()` tách chuỗi thành **List các từ**; `.join(list)` ghép List thành chuỗi.

| Lỗi thường gặp | Nguyên nhân | Cách khắc phục |
| :--- | :--- | :--- |
| `TypeError: 'str' object does not support item assignment` | Cố tình viết `s[0] = "A"` | Tạo chuỗi mới bằng ghép lát cắt: `s = "A" + s[1:]` |
| Gọi `s.upper()` nhưng in `s` vẫn thấy chữ thường | Quên gán lại kết quả vào biến | Viết `s = s.upper()` hoặc `s_hoa = s.upper()` |
| Cắt bị thiếu ký tự cuối của từ | Nhầm `stop` có được lấy | Cộng thêm `1` vào vị trí `stop` |

---

## V. BÀI TẬP VỀ NHÀ

1. Nhập họ tên đầy đủ còn thừa khoảng trắng 2 đầu (ví dụ `"   nguyễn văn an   "`). Dùng `.strip()` và `.title()` để chuẩn hóa đẹp mắt.
2. Nhập một câu, đếm xem câu đó có bao nhiêu **từ** (dùng `.split()` và `len()`).
3. Kiểm tra xem một từ nhập vào có phải **từ đối xứng** (đọc xuôi ngược giống nhau như `"radar"`, `"madam"`) không, không phân biệt hoa thường.
4. Viết bộ lọc chat: tự động thay thế các từ `"xấu"`, `"tệ"` trong câu thành `"***"`.
5. *(Nâng cao)* Viết chương trình **Mã hóa & Giải mã mật mã Caesar** cho phép người dùng chọn chế độ (1. Mã hóa / 2. Giải mã) và bước dịch `k` bất kỳ.
