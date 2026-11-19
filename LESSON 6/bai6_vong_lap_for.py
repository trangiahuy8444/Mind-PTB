# -*- coding: utf-8 -*-
"""
KHÓA HỌC: LẬP TRÌNH PYTHON CƠ BẢN (TT-C4K-PTB30)
BÀI 6: VÒNG LẶP FOR & HÀM RANGE()
Thời lượng: 120 phút
Giáo viên: Thầy Huy Trần

Cách dùng: chạy file này để xem toàn bộ ví dụ mẫu của buổi học.
Các bài tập thực hành (cần nhập dữ liệu) nằm ở cuối file, bỏ dấu # để chạy thử.
"""


# ==============================================================================
# PHẦN 1: NHẮC LẠI BÀI 1 - IN BẢNG CỬU CHƯƠNG 98 "KIỂU CŨ" (10 DÒNG PRINT)
# ==============================================================================
def bang_cuu_chuong_kieu_cu():
    print("98 x 1 =", 98 * 1)
    print("98 x 2 =", 98 * 2)
    print("98 x 3 =", 98 * 3)
    # ... phải gõ tiếp đến dòng thứ 10 -> rất dài và dễ sai!


# ==============================================================================
# PHẦN 2: CÙNG BÀI TOÁN ĐÓ, CHỈ CẦN 2 DÒNG VỚI VÒNG LẶP FOR
# ==============================================================================
def bang_cuu_chuong(n):
    print(f"\n--- BẢNG NHÂN {n} ---")
    for i in range(1, 11):          # i lần lượt nhận 1, 2, 3, ..., 10
        print(n, "x", i, "=", n * i)


# ==============================================================================
# PHẦN 3: BA CÁCH VIẾT HÀM RANGE()
# ==============================================================================
def demo_range():
    print("\n--- DEMO HÀM RANGE() ---")
    print("range(5)          ->", list(range(5)))          # [0, 1, 2, 3, 4]
    print("range(1, 6)       ->", list(range(1, 6)))       # [1, 2, 3, 4, 5]
    print("range(2, 11, 2)   ->", list(range(2, 11, 2)))   # [2, 4, 6, 8, 10]
    print("range(10, 0, -3)  ->", list(range(10, 0, -3)))  # [10, 7, 4, 1]
    print("range(5, 1)       ->", list(range(5, 1)))       # [] (rỗng!)


# ==============================================================================
# PHẦN 4: BIẾN TÍCH LŨY (ACCUMULATOR) - TÍNH TỔNG 1 + 2 + ... + n
# ==============================================================================
def tinh_tong(n):
    tong = 0                         # 1. Khởi tạo "chiếc giỏ" rỗng
    for i in range(1, n + 1):        # 2. Lặp từ 1 đến n (nhớ n + 1!)
        tong = tong + i              # 3. Bỏ thêm i vào giỏ (viết gọn: tong += i)
    return tong                      # 4. Dùng kết quả SAU khi lặp xong


# ==============================================================================
# PHẦN 5: KẾT HỢP FOR + IF (BÀI 4) - ĐẾM SỐ CHẴN
# ==============================================================================
def dem_so_chan(n):
    dem = 0
    for i in range(1, n + 1):
        if i % 2 == 0:               # Toán tử % (Bài 3) + câu điều kiện (Bài 4)
            dem += 1
    return dem


# ==============================================================================
# PHẦN 6: DUYỆT TỪNG KÝ TỰ TRONG CHUỖI
# ==============================================================================
def dem_nguyen_am(chuoi):
    dem = 0
    for ky_tu in chuoi:
        if ky_tu in "aeiouAEIOU":
            dem += 1
    return dem


# ==============================================================================
# PHẦN 7: GIAI THỪA n! = 1 x 2 x ... x n (TÍCH LŨY PHÉP NHÂN)
# ==============================================================================
def giai_thua(n):
    ket_qua = 1                      # Nhân thì khởi tạo bằng 1, KHÔNG phải 0!
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua


# ==============================================================================
# PHẦN 8: VẼ TAM GIÁC SAO
# ==============================================================================
def ve_tam_giac(chieu_cao):
    for i in range(1, chieu_cao + 1):
        print("*" * i)


# ==============================================================================
# PHẦN 9: LIÊN KẾT BÀI 5 - TỔNG TIỀN ĐIỆN CẢ NĂM (TIỀN ĐIỆN 2 BẬC CỦA BÀI 4)
# ==============================================================================
def tien_dien_2_bac(kwh):
    if kwh <= 50:
        return kwh * 1500
    return 50 * 1500 + (kwh - 50) * 2000


def tong_tien_dien_ca_nam(ds_kwh):
    tong = 0
    thang = 1
    for kwh in ds_kwh:
        tien = tien_dien_2_bac(kwh)
        print(f"Tháng {thang:2}: {kwh:4} kWh -> {tien:>9,} đ")
        tong += tien
        thang += 1
    return tong


# ==============================================================================
# CHẠY THỬ TẤT CẢ VÍ DỤ
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("BÀI 6: VÒNG LẶP FOR & HÀM RANGE()")
    print("=" * 60)

    bang_cuu_chuong(98)
    demo_range()

    print("\n--- TÍNH TỔNG ---")
    print("Tổng 1 + 2 + ... + 10  =", tinh_tong(10))     # 55
    print("Tổng 1 + 2 + ... + 100 =", tinh_tong(100))    # 5050

    print("\n--- ĐẾM SỐ CHẴN ---")
    print("Từ 1 đến 10 có", dem_so_chan(10), "số chẵn")  # 5

    print("\n--- ĐẾM NGUYÊN ÂM ---")
    print('"MindX Python" có', dem_nguyen_am("MindX Python"), "nguyên âm")  # 2

    print("\n--- GIAI THỪA ---")
    print("5! =", giai_thua(5))                            # 120

    print("\n--- TAM GIÁC SAO ---")
    ve_tam_giac(5)

    print("\n--- TIỀN ĐIỆN CẢ NĂM ---")
    ds = [45, 60, 80, 120, 150, 200, 210, 190, 130, 90, 70, 55]
    print(f"TỔNG CẢ NĂM: {tong_tien_dien_ca_nam(ds):,} đ")

    # ==========================================================================
    # BÀI TẬP THỰC HÀNH (bỏ dấu # để chạy thử)
    # ==========================================================================
    # n = int(input("Nhập n: "))
    # print("Tổng từ 1 đến", n, "là:", tinh_tong(n))
