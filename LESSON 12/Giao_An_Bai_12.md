# KẾ HOẠCH BÀI DẠY (GIÁO ÁN 120 PHÚT)
## BÀI 12: HÀM (FUNCTION) — CHIA NHỎ CÔNG VIỆC
**Khóa học:** Lập trình Python Cơ Bản (`TT-C4K-PTB30`)  
**Thời lượng:** 120 phút  
**Giáo viên phụ trách:** Thầy Huy Trần  
**Học liệu tương tác đi kèm:** `LESSON 12/index.html` · Mã nguồn mẫu: `LESSON 12/bai12_ham_co_ban.py`

---

## I. MỤC TIÊU BÀI HỌC

### 1. Kiến thức
- Hiểu định nghĩa **Hàm (Function)** qua ẩn dụ "Chiếc máy làm bánh / Cỗ máy phép thuật" và triết lý **DRY (Don't Repeat Yourself — Đừng lặp lại chính mình)**.
- Nắm vững cú pháp khai báo hàm: `def ten_ham():` cùng quy tắc dấu hai chấm `:` và thụt lề 4 dấu cách.
- Phân biệt rạch ròi 2 giai đoạn: **Định nghĩa hàm (`def`)** — máy mới chế tạo, chưa chạy; và **Gọi hàm (`ten_ham()`)** — bấm nút kích hoạt.
- Hiểu thứ tự nhảy lệnh của CPU khi gọi hàm và mô hình **hàm gọi hàm** (hàm `combo_huy_diet()` gọi các hàm con).

### 2. Kỹ năng
- Tự khai báo hàm thực hiện 1 công việc rõ ràng (vẽ viền, in menu, tung chiêu thức).
- Phân rã chương trình dài thành nhiều hàm gọn gàng dễ đọc, dễ bảo trì.
- Phát hiện nhanh 3 lỗi kinh điển: quên gọi hàm, quên cặp ngoặc `()` khi gọi hàm (`ten_ham` thay vì `ten_ham()`), và gọi hàm trước khi `def`.

### 3. Phẩm chất
- Tư duy module hóa: chia việc lớn thành các khối chức năng sạch sẽ.

---

## II. LIÊN KẾT KIẾN THỨC

| Kiến thức các bài trước / sau | Sự liên kết với Bài 12 |
| :--- | :--- |
| Bài 1 & 4 – Quy tắc đặt tên, dấu `:` và thụt lề | Tên hàm tuân thủ quy tắc đặt tên biến (`snake_case`); thân hàm dùng cùng quy tắc `:` và thụt lề |
| Bài 6 – Tự động hóa lặp liên tiếp | `for` lặp lại các bước liền kề nhau; còn **Hàm** giúp tái sử dụng đoạn code ở **bất kỳ nơi nào, bất kỳ lúc nào** |
| Bài 8 & 10 – Menu game / Shop | Đóng gói các phần in bảng chỉ số, in menu thành hàm riêng giúp code sạch đẹp |
| **→ Bài 13** | Hàm ở Bài 12 luôn làm đúng 1 kiểu cố định (chưa nhận dữ liệu đầu vào và trả về kết quả). Bài 13 bổ sung **Tham số, Đối số, `return` và Phạm vi biến**! |

---

## III. TIẾN TRÌNH DẠY HỌC (120 PHÚT)

| Thời gian | Hoạt động | Nội dung & Phương pháp | Học liệu |
| :--- | :--- | :--- | :--- |
| **00' – 15'** | **HĐ1: Ẩn dụ Chiếc Máy Làm Bánh Sandwich** | Đặt tình huống phải in khung tiêu đề 4 lần ở 4 chỗ khác nhau trong game. So sánh copy-paste với chế tạo 1 chiếc máy `in_khung()` bấm nút là chạy. Giới thiệu nguyên tắc **DRY**. | Tab 1 mục 1 |
| **15' – 35'** | **HĐ2: Cú pháp `def` & Bẫy Quên Gọi Hàm** | Live code `def chao_mung():`. Cố tình bấm Run khi CHƯA gọi `chao_mung()` để HS thấy màn hình trống trơn → khắc sâu *Định nghĩa ≠ Gọi hàm*. | Tab 1 mục 2 |
| **35' – 55'** | **HĐ3: Function Call Flow Visualizer** | HS mở Tab 2 chạy từng bước 3 kịch bản: (1) Quên gọi hàm, (2) Gọi hàm nhiều lần (DRY), (3) Hàm gọi hàm (`combo_huy_diet()`). Quan sát con trỏ nhảy từ `def` → bỏ qua thân → gặp lời gọi mới nhảy vào thân → quay lại! | Tab 2 – Call Flow |
| **55' – 65'** | Nghỉ giải lao | | |
| **65' – 100'** | **HĐ4: Sprint – Xưởng Phép Thuật Macro Skill** | HS hoàn thành Bài 1 → 4: viết các hàm `danh_thuong()`, `hoi_mau()`, `chieu_cuoi()`, ghép thành `combo_huy_diet()`, và gắn với menu `while True` bấm phím `Q/W/E/R`. | Tab 4 & Code Lab |
| **100' – 112'** | **HĐ5: Trắc nghiệm phản xạ** | HS làm 12 câu trên Tab 3. Chữa lỗi gọi thiếu `()` và gọi hàm trước khi `def`. | Tab 3 |
| **112' – 120'** | **HĐ6: Tổng kết & cầu nối Bài 13** | Đặt câu hỏi: *"Chiêu `danh_thuong()` luôn trừ đúng 20 máu. Làm sao để cùng 1 hàm mà lúc truyền 20 sát thương, lúc truyền 50 sát thương và trả lại máu mới?"* → **Bài 13**! | Tab 1 mục cầu nối |

---

## IV. NỘI DUNG TRỌNG TÂM & LỖI THƯỜNG GẶP

1. Cú pháp: `def ten_ham():` rồi thụt lề khối lệnh bên trong.
2. Khi Python đọc qua khối `def`, nó **chỉ ghi nhớ** hàm chứ **chưa chạy** thân hàm; chỉ khi gặp lời gọi `ten_ham()` thì CPU mới nhảy vào chạy rồi quay lại dòng ngay sau đó.
3. Trong một hàm có thể gọi một hàm khác (Hàm gọi hàm).

| Lỗi thường gặp | Nguyên nhân | Cách khắc phục |
| :--- | :--- | :--- |
| Chạy code không thấy in gì | Chỉ `def ham():` mà quên gọi `ham()` | Thêm dòng gọi hàm ở bên ngoài khối `def` |
| Viết `ten_ham` thiếu ngoặc `()` | Không thực thi hàm (chỉ tham chiếu tới hàm) | Phải viết đủ cặp ngoặc: `ten_ham()` |
| `NameError: name 'ham' is not defined` | Gọi hàm nằm **phía trên** dòng `def ham():` | Đặt phần `def` nằm phía trên lời gọi hàm |

---

## V. BÀI TẬP VỀ NHÀ

1. Viết hàm `ke_vien()` in 30 dấu `-`, và hàm `tieu_de()` gọi `ke_vien()` ở trên và dưới dòng `"BẢNG ĐIỂM HỌC SINH"`.
2. Viết hàm `ve_hinh_vuong()` dùng vòng lặp `for` in hình vuông sao `4x4`. Gọi hàm đó 2 lần.
3. Viết hàm `hien_thi_menu()` in menu 4 lựa chọn cho một ứng dụng máy tính bỏ túi.
4. Viết 2 hàm `loi_chao_sang()` và `loi_chao_toi()`, sau đó nhập giờ hiện tại (0–23) để gọi đúng hàm tương ứng.
5. *(Nâng cao)* Tạo hệ thống **Bàn phím Macro Chiêu Thức**: gồm 3 hàm chiêu (`Q`, `W`, `E`), biến `nang_luong = 100`, lặp cho người chơi bấm phím thi triển (mỗi chiêu tốn năng lượng khác nhau) cho đến khi bấm `X` thoát.
