# KẾ HOẠCH BÀI DẠY (GIÁO ÁN 120 PHÚT)
## BÀI 8: LẬP TRÌNH GIẢI QUYẾT VẤN ĐỀ — DỰ ÁN "SINH TỒN TRÊN HOANG ĐẢO"
**Khóa học:** Lập trình Python Cơ Bản (`TT-C4K-PTB30`)  
**Thời lượng:** 120 phút  
**Giáo viên phụ trách:** Thầy Huy Trần  
**Học liệu tương tác đi kèm:** `LESSON 8/index.html` · Mã nguồn mẫu: `LESSON 8/bai8_giai_quyet_van_de.py`

---

## I. MỤC TIÊU BÀI HỌC

### 1. Kiến thức
- Nắm vững **quy trình 4 bước giải quyết vấn đề** bằng lập trình: (1) Hiểu đề & xác định Input/Output, (2) Phân rã bài toán lớn thành các bước nhỏ (Decomposition), (3) Thiết kế khung sườn mã nguồn & trạng thái (Skeleton & State), (4) Lắp ghép code, kiểm thử và sửa lỗi.
- Hiểu mô hình **Game Loop & Quản lý trạng thái (Game State)**: duy trì các biến `mau`, `thuc_an`, `nuoc_uong`, `ngay` trong vòng lặp `while True`.
- Biết cách sử dụng thư viện `random` (`random.randint()`) để tạo yếu tố ngẫu nhiên.

### 2. Kỹ năng
- Tổng hợp thành thạo kiến thức từ Bài 1 đến Bài 7 (Biến, Ép kiểu, Toán tử, `if-elif-else`, `for`, `while`, `break`, `continue`) để giải quyết một bài toán thực tế hoàn chỉnh.
- Thiết kế khung sườn chương trình (Skeleton Code) trước khi viết chi tiết từng nhánh, tránh rối logic.
- Chạy thử các tình huống biên (máu về 0, chỉ số vượt 100, nhập lựa chọn sai) để debug.

### 3. Phẩm chất
- Tư duy hệ thống, không hoảng sợ trước đề bài dài.
- Tinh thần hợp tác, kiểm thử chéo và phản biện tích cực sản phẩm của bạn.

---

## II. LIÊN KẾT KIẾN THỨC

| Kiến thức các bài trước | Vai trò trong Bài 8 |
| :--- | :--- |
| Bài 1 & 2 – Biến, `input()`, `int()` | Lưu trữ chỉ số nhân vật & đọc lựa chọn từ menu người chơi |
| Bài 3 – Toán tử `//`, `%`, logic `and`/`or` | Tính toán cộng/trừ chỉ số, kiểm tra điều kiện chết (`mau <= 0 or nuoc <= 0`) |
| Bài 4 – `if - elif - else` | Rẽ nhánh 4 hành động (Săn bắn, Tìm nước, Nghỉ ngơi, Đóng bè) |
| Bài 6 & 7 – `while True`, `break`, `continue` | Vòng lặp ngày trôi qua, nhập sai menu thì `continue`, thắng/thua thì `break` |
| **→ Bài 9** | Kiểm tra Vòng lặp (Checkpoint 2) & học **Danh sách (`list`)** để lưu cả **balo nhiều vật phẩm** thay vì từng biến lẻ! |

---

## III. TIẾN TRÌNH DẠY HỌC (120 PHÚT)

| Thời gian | Hoạt động | Nội dung & Phương pháp | Học liệu |
| :--- | :--- | :--- | :--- |
| **00' – 15'** | **HĐ1: Cuộc họp Studio & Trải nghiệm mẫu** | HS chơi thử bản mô phỏng **Sinh Tồn Trên Hoang Đảo** trên Tab 2 để hiểu luật chơi, các biến trạng thái và xem code Python chạy song song. | Tab 2 – Survival Simulator |
| **15' – 35'** | **HĐ2: Phân tích & Phân rã bài toán (4 bước)** | GV hướng dẫn HS điền bảng phân rã: **Biến trạng thái** là gì? **Menu hành động** gồm gì? **Điều kiện Thắng/Thua** là gì? Giải thích kỹ thuật viết **Skeleton Code** trước. | Tab 1 mục 1, 2 |
| **35' – 65'** | **HĐ3: Sprint 1 – Dựng khung sườn & Phiên bản Cơ bản** | HS tự gõ khung vòng lặp `while True`, menu 3 hành động và điều kiện sống qua 7 ngày trên VS Code / Code Lab. | Tab 1 mục 3 & Code Lab |
| **65' – 70'** | Nghỉ giải lao | | |
| **70' – 100'** | **HĐ4: Sprint 2 – Nâng cấp (Bão tố random & Đóng bè)** | Phân hóa theo 3 mức: Cơ bản (3 hành động + sống 7 ngày) → Nâng cấp (thêm `random.randint` bão tố & chặn chỉ số `0..100`) → Thử thách (thu thập 4 gỗ đóng bè thoát sớm). | Tab 4 & VS Code |
| **100' – 112'** | **HĐ5: Chơi thử chéo & Trắc nghiệm** | HS làm 10 câu trắc nghiệm tổng hợp tư duy giải quyết vấn đề trên Tab 3. | Tab 3 |
| **112' – 120'** | **HĐ6: Tổng kết & cầu nối Bài 9** | Đặt câu hỏi mở: *"Nếu nhân vật nhặt được 10 món đồ khác nhau (dao, bật lửa, cá, gỗ, thuốc...), chẳng lẽ tạo 10 biến?"* → Mở ra **Bài 9: Danh sách (`list`)**! | Tab 1 mục cầu nối |

---

## IV. NỘI DUNG TRỌNG TÂM & LỖI THƯỜNG GẶP

1. **4 bước giải quyết vấn đề:** Hiểu bài toán → Phân rã thành từng phần nhỏ → Dựng khung sườn (Skeleton) → Cài đặt & kiểm thử.
2. **Quản lý trạng thái (State):** Tập hợp tất cả biến mô tả tình huống tại một thời điểm (ví dụ `ngay`, `mau`, `thuc_an`, `nuoc_uong`).
3. **Kẹp biên giá trị:** Không để máu hoặc thức ăn vượt quá `100` hoặc âm dưới `0` (dùng `if mau > 100: mau = 100` hoặc `min(100, ...)`).

| Lỗi thường gặp | Nguyên nhân | Cách khắc phục |
| :--- | :--- | :--- |
| Nhập menu sai vẫn bị tính trôi qua 1 ngày | Không dùng `continue` khi `chon` không thuộc `1..4` | Kiểm tra hợp lệ trước, sai thì thông báo và `continue` |
| Quên kiểm tra thua khi `thuc_an == 0` | Chỉ trừ thức ăn mà quên liên hệ sang máu | Nếu `thuc_an == 0` hoặc `nuoc_uong == 0` thì trừ mạnh `mau` |
| Máu tăng lên 140 khi nghỉ ngơi nhiều | Quên giới hạn trần `100` | Sau khi cộng, thêm `if mau > 100: mau = 100` |

---

## V. BÀI TẬP VỀ NHÀ

1. Thêm hành động thứ 5 vào game Hoang Đảo: **Câu cá** (tăng ngẫu nhiên 15–35 thức ăn).
2. Viết chương trình **Máy bán nước tự động**: người dùng nạp tiền, chọn nước (Coca 10k, Trà xanh 12k, Nước suối 6k), kiểm tra đủ tiền, trả tiền thừa, hỏi mua tiếp hay thoát.
3. Viết chương trình **Đổi số giây** bất kỳ (ví dụ `3665`) thành định dạng `Giờ : Phút : Giây` (`01:01:05`).
4. Viết trò chơi **Kéo – Búa – Bao** đấu với máy (5 hiệp, tính tỉ số Thắng / Hòa / Thua).
5. *(Nâng cao)* Thiết kế một **Mini ATM** hoàn chỉnh: đăng nhập mã PIN (tối đa 3 lần), menu 4 chức năng (Xem số dư, Nạp tiền, Rút tiền có kiểm tra số dư, Thoát).
