# -*- coding: utf-8 -*-
"""
KHÓA HỌC: LẬP TRÌNH PYTHON CƠ BẢN (TT-C4K-PTB30)
BÀI 5: ÔN TẬP TỔNG HỢP (BIẾN, KIỂU DỮ LIỆU, TOÁN TỬ & CÂU ĐIỀU KIỆN)
Thời lượng: 60 Phút
Giáo viên: Thầy Huy Trần
"""

# ==============================================================================
# BÀI TOÁN TRỌNG TÂM: TÍNH TIỀN ĐIỆN SINH HOẠT BẬC THANG (EVN)
# ==============================================================================
def tinh_tien_dien_evn(kwh):
    """
    Hàm tính tiền điện sinh hoạt theo biểu giá lũy tiến bậc thang EVN:
    - Bậc 1: Cho kWh từ 0 - 50      : 1.806 đ/kWh
    - Bậc 2: Cho kWh từ 51 - 100    : 1.866 đ/kWh
    - Bậc 3: Cho kWh từ 101 - 200   : 2.167 đ/kWh
    - Bậc 4: Cho kWh từ 201 - 300   : 2.729 đ/kWh
    - Bậc 5: Cho kWh từ 301 trở lên : 3.050 đ/kWh
    Thuế VAT: 8%
    """
    print(f"\n--- BẢNG KÊ HÓA ĐƠN TIỀN ĐIỆN CHO {kwh} kWh ---")
    
    if kwh < 0:
        print("Lỗi: Số điện tiêu thụ không thể là số âm!")
        return None
    
    # Định mức tiền tối đa tích lũy của từng bậc đầy
    TIEN_BAC_1 = 50 * 1806                           # 90.300 đ
    TIEN_BAC_2 = TIEN_BAC_1 + 50 * 1866              # 90.300 + 93.300 = 183.600 đ
    TIEN_BAC_3 = TIEN_BAC_2 + 100 * 2167             # 183.600 + 216.700 = 400.300 đ
    TIEN_BAC_4 = TIEN_BAC_3 + 100 * 2729             # 400.300 + 272.900 = 673.200 đ
    
    tien_chua_thue = 0.0
    bac_hien_tai = ""
    
    if kwh <= 50:
        bac_hien_tai = "Bậc 1 (0 - 50 kWh)"
        tien_chua_thue = kwh * 1806
    elif kwh <= 100:
        bac_hien_tai = "Bậc 2 (51 - 100 kWh)"
        tien_chua_thue = TIEN_BAC_1 + (kwh - 50) * 1866
    elif kwh <= 200:
        bac_hien_tai = "Bậc 3 (101 - 200 kWh)"
        tien_chua_thue = TIEN_BAC_2 + (kwh - 100) * 2167
    elif kwh <= 300:
        bac_hien_tai = "Bậc 4 (201 - 300 kWh)"
        tien_chua_thue = TIEN_BAC_3 + (kwh - 200) * 2729
    else:
        bac_hien_tai = "Bậc 5 (> 300 kWh)"
        tien_chua_thue = TIEN_BAC_4 + (kwh - 300) * 3050

    vat = tien_chua_thue * 0.08
    tong_cong = tien_chua_thue + vat
    
    print(f"Mức tiêu thụ đạt tới  : {bac_hien_tai}")
    print(f"Tiền điện chưa thuế   : {tien_chua_thue:,.0f} VNĐ")
    print(f"Thuế GTGT (VAT 8%)    : {vat:,.0f} VNĐ")
    print(f"Tổng tiền thanh toán  : {tong_cong:,.0f} VNĐ")
    return tong_cong


# ==============================================================================
# BÀI TOÁN 1: KIỂM TRA SỐ CHẴN / LẺ VÀ ÂM / DƯƠNG / KHÔNG
# ==============================================================================
def kiem_tra_so(n):
    print(f"\n--- Phân tích số nguyên n = {n} ---")
    if n == 0:
        print("Kết quả: Số 0 (Không âm, không dương)")
    else:
        loai_chan_le = "Chẵn" if n % 2 == 0 else "Lẻ"
        loai_dau = "Dương" if n > 0 else "Âm"
        print(f"Kết quả: {n} là số {loai_chan_le} {loai_dau}")


# ==============================================================================
# BÀI TOÁN 2: XẾP LOẠI HỌC LỰC HỌC SINH (LỖI THỨ TỰ ELIF)
# ==============================================================================
def xep_loai_hoc_luc(diem):
    print(f"\n--- Xếp loại học lực cho điểm: {diem} ---")
    if diem < 0 or diem > 10:
        print("Điểm không hợp lệ! Chỉ xét thang điểm từ 0.0 đến 10.0")
        return
        
    # QUY TẮC: Luôn kiểm tra từ điều kiện khắt khe nhất (từ cao xuống thấp)
    if diem >= 8.0:
        xep_loai = "Giỏi"
    elif diem >= 6.5:
        xep_loai = "Khá"
    elif diem >= 5.0:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"
    
    print(f"Điểm số: {diem} -> Xếp loại: {xep_loai}")


# ==============================================================================
# BÀI TOÁN 3: KIỂM TRA 3 CẠNH TAM GIÁC & TOÁN TỬ LOGIC
# ==============================================================================
def kiem_tra_tam_giac(a, b, c):
    print(f"\n--- Kiểm tra 3 cạnh ({a}, {b}, {c}) ---")
    # Điều kiện bất đẳng thức tam giác: dùng toán tử 'and'
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            loai = "Tam giác ĐỀU"
        elif a == b or b == c or a == c:
            loai = "Tam giác CÂN"
        elif (abs(a**2 + b**2 - c**2) < 1e-5 or 
              abs(a**2 + c**2 - b**2) < 1e-5 or 
              abs(b**2 + c**2 - a**2) < 1e-5):
            loai = "Tam giác VUÔNG"
        else:
            loai = "Tam giác THƯỜNG"
        print(f"Kết quả: Hợp lệ -> {loai}")
    else:
        print("Kết quả: Không thể tạo thành 3 cạnh của một tam giác!")


# ==============================================================================
# CHẠY THỬ NGHIỆM TẤT CẢ CÁC BỘ TEST TRONG TIẾT HỌC
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("CHÀO MỪNG CÁC EM ĐẾN VỚI BÀI 5: ÔN TẬP TỔNG HỢP PYTHON")
    print("=" * 60)
    
    # 1. Thử nghiệm bài toán tiền điện với các mức kWh khác nhau:
    tinh_tien_dien_evn(35)   # Bậc 1
    tinh_tien_dien_evn(80)   # Bậc 2
    tinh_tien_dien_evn(125)  # Bậc 3 (Ví dụ kinh điển)
    tinh_tien_dien_evn(250)  # Bậc 4
    tinh_tien_dien_evn(350)  # Bậc 5
    tinh_tien_dien_evn(-10)  # Trường hợp lỗi
    
    # 2. Thử nghiệm phân tích số:
    kiem_tra_so(8)
    kiem_tra_so(-7)
    kiem_tra_so(0)
    
    # 3. Thử nghiệm xếp loại điểm:
    xep_loai_hoc_luc(9.2)
    xep_loai_hoc_luc(7.0)
    xep_loai_hoc_luc(4.5)
    
    # 4. Thử nghiệm tam giác:
    kiem_tra_tam_giac(3, 4, 5)
    kiem_tra_tam_giac(5, 5, 5)
    kiem_tra_tam_giac(1, 2, 8)
    
    print("\n" + "=" * 60)
    print("HOÀN THÀNH BÀI ÔN TẬP!")
    print("=" * 60)
