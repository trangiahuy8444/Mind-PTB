# KẾ HOẠCH BÀI DẠY (GIÁO ÁN 120 PHÚT)
## BÀI 10: DANH SÁCH VÀ HƠN THẾ NỮA — THAO TÁC CRUD
**Khóa học:** Lập trình Python Cơ Bản (`TT-C4K-PTB30`)  
**Thời lượng:** 120 phút  
**Giáo viên phụ trách:** Thầy Huy Trần  
**Học liệu tương tác đi kèm:** `LESSON 10/index.html` · Mã nguồn mẫu: `LESSON 10/bai10_thao_tac_list.py`

---

## I. MỤC TIÊU BÀI HỌC

### 1. Kiến thức
- Hiểu mô hình **CRUD** trong quản lý dữ liệu: **Create** (Thêm), **Read** (Đọc/Xem), **Update** (Sửa), **Delete** (Xóa).
- Thành thạo các phương thức biến đổi List:
  - Thêm: `.append(x)` (thêm cuối), `.insert(i, x)` (chèn tại vị trí `i`).
  - Sửa: `ds[i] = gia_tri_moi`.
  - Xóa: `.remove(x)` (xóa theo giá trị), `.pop(i)` (xóa theo chỉ số và trả về phần tử).
  - Sắp xếp & thống kê: `.sort()`, `.sort(reverse=True)`, `.reverse()`, `sum()`, `min()`, `max()`.
- Biết cách phòng vệ tránh lỗi `ValueError: list.remove(x): x not in list` bằng `if x in ds:`.

### 2. Kỹ năng
- Phân biệt khi nào dùng `.remove()` vs `.pop()`, khi nào dùng `.append()` vs `.insert()`.
- Kết hợp vòng lặp `while True` (Bài 7) và `list` để xây dựng phần mềm có Menu CRUD hoàn chỉnh (Quản lý balo / Shop trang bị Minecraft).

### 3. Phẩm chất
- Tư duy phòng lỗi (Defensive Coding): luôn kiểm tra tồn tại và giới hạn kích thước trước khi sửa/xóa dữ liệu.

---

## II. LIÊN KẾT KIẾN THỨC

| Kiến thức các bài trước / sau | Vai trò trong Bài 10 |
| :--- | :--- |
| Bài 7 – Vòng lặp `while True` & `break` | Tạo menu lặp 4–5 chức năng cho người dùng thêm/xóa/sửa nhiều lần |
| Bài 9 – List, chỉ số dương/âm, `in`, `IndexError` | Nền tảng truy cập `ds[i]`, kiểm tra `if mon in balo:` trước khi `.remove()` |
| **→ Bài 11** | Từ danh sách các phần tử chuyển sang **Xâu ký tự (`str`)**: chuỗi có cắt, duyệt được như List không và khác List ở điểm nào (*tính bất biến*)? |

---

## III. TIẾN TRÌNH DẠY HỌC (120 PHÚT)

| Thời gian | Hoạt động | Nội dung & Phương pháp | Học liệu |
| :--- | :--- | :--- | :--- |
| **00' – 15'** | **HĐ1: Khởi động – Trò chơi "Nhặt đồ tiếp sức"** | Chiếu `balo = []`. Từng HS hô 1 món đồ để GV gõ `balo.append(...)`. Đặt tình huống cần nâng cấp vũ khí (Sửa), chèn thuốc lên đầu (`.insert(0, ...)`), vứt đồ nặng (`.remove()` / `.pop()`). | Tab 1 mục 1 |
| **15' – 35'** | **HĐ2: Bộ 4 Tuyệt Chiêu CRUD & Bẫy `ValueError`** | Giải thích `.append()`, `.insert()`, gán `ds[i]`, `.remove()`, `.pop()`. Demo cố ý gọi `balo.remove("Bom")` khi không có "Bom" → `ValueError`, dẫn ra cách phòng vệ `if x in balo:`. | Tab 1 mục 2, 3 |
| **35' – 55'** | **HĐ3: Balo Minecraft CRUD Sandbox** | HS mở Tab 2 thao tác trực tiếp thêm/chèn/sửa/xóa/sắp xếp trên giao diện Balo Minecraft, quan sát chỉ số tự động dịch chuyển và câu lệnh Python sinh ra. | Tab 2 – CRUD Sandbox |
| **55' – 65'** | Nghỉ giải lao + chuẩn bị Sprint | | |
| **65' – 100'** | **HĐ4: Sprint Dự Án "Shop Trang Bị Minecraft"** | HS viết chương trình Menu CRUD kết hợp ví xu: Xem balo, Mua đồ, Bán đồ (nhận lại xu), Sắp xếp, giới hạn tối đa 5 món. | Tab 4 & Code Lab |
| **100' – 112'** | **HĐ5: Trắc nghiệm phản xạ** | HS làm 12 câu trên Tab 3. Chữa kỹ sự khác nhau giữa `.remove()` và `.pop()` và lỗi `print(ds.sort())` in ra `None`. | Tab 3 |
| **112' – 120'** | **HĐ6: Tổng kết & cầu nối Bài 11** | Gợi mở: *"Nếu ta thử gán `s = 'MindX'` rồi sửa `s[0] = 'K'` giống List thì có được không?"* → Khám phá **Bài 11: Xâu Ký Tự (String)**! | Tab 1 mục cầu nối |

---

## IV. NỘI DUNG TRỌNG TÂM & LỖI THƯỜNG GẶP

1. `.append(x)` thêm cuối; `.insert(i, x)` chèn vào vị trí `i` (các phần tử sau dồn sang phải).
2. `.remove(x)` xóa theo **giá trị** (chỉ xóa lần xuất hiện đầu); `.pop(i)` xóa theo **chỉ số** (mặc định cuối nếu bỏ trống `i`).
3. Các phương thức `.append()`, `.sort()`, `.reverse()` **thay đổi trực tiếp danh sách** và trả về `None` — không viết `ds = ds.sort()` hay `print(ds.sort())`.

| Lỗi thường gặp | Nguyên nhân | Cách khắc phục |
| :--- | :--- | :--- |
| `ValueError: x not in list` | Gọi `ds.remove(x)` khi `x` không có trong `ds` | Luôn kiểm tra `if x in ds:` trước khi xóa |
| Danh sách biến thành `None` | Viết `ds = ds.append("A")` hoặc `ds = ds.sort()` | Chỉ viết `ds.append("A")`, `ds.sort()` |
| `IndexError: pop from empty list` | Gọi `.pop()` trên danh sách rỗng `[]` | Kiểm tra `if len(ds) > 0:` trước |

---

## V. BÀI TẬP VỀ NHÀ

1. Tạo danh sách rỗng `mon_hoc = []`. Dùng `for` 5 lần nhập tên 5 môn học thêm vào cuối danh sách, sau đó sắp xếp theo bảng chữ cái A–Z.
2. Cho `so = [4, 2, 7, 2, 9, 2]`. Xóa **tất cả** các số `2` khỏi danh sách (gợi ý: dùng `while 2 in so: so.remove(2)`).
3. Nhập danh sách điểm của cả lớp (nhập `-1` để dừng). Loại bỏ điểm thấp nhất và điểm cao nhất rồi tính điểm trung bình các bạn còn lại.
4. Viết chương trình **Danh sách To-Do hằng ngày** (Menu: 1. Xem việc | 2. Thêm việc | 3. Đánh dấu hoàn thành/xóa theo STT | 0. Thoát).
5. *(Nâng cao)* Hoàn thiện **Shop Trang Bị Minecraft** với ví `150` xu, balo tối đa `5` ô, có chức năng Mua đồ (trừ xu, thêm vào balo) và Bán đồ (xóa khỏi balo, cộng lại 50% xu).
