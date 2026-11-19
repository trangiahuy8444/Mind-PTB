# -*- coding: utf-8 -*-
"""
KHÓA HỌC: LẬP TRÌNH PYTHON CƠ BẢN (TT-C4K-PTB30)
BÀI 13: HÀM NÂNG CAO — THAM SỐ, ĐỐI SỐ, RETURN & PHẠM VI BIẾN
Thời lượng: 120 phút
Giáo viên: Thầy Huy Trần
"""

import random


# ==============================================================================
# PHẦN 1: THAM SỐ (PARAMETER) vs ĐỐI SỐ (ARGUMENT) & THAM SỐ MẶC ĐỊNH
# ==============================================================================
def chao_nguoi_choi(ten, danh_hieu="Tân Binh"):
    """ten, danh_hieu là THAM SỐ; danh_hieu có giá trị mặc định 'Tân Binh'."""
    print(f"Chào mừng {danh_hieu} {ten} bước vào đấu trường!")


# ==============================================================================
# PHẦN 2: SỰ KHÁC BIỆT SỐNG CÒN GIỮA PRINT() VÀ RETURN
# ==============================================================================
def gap_doi_chi_print(x):
    print("Bên trong hàm print:", x * 2)  # Không có return -> mặc định trả về None!


def gap_doi_co_return(x):
    return x * 2                         # Trả về kết quả để gán vào biến / tính tiếp


# ==============================================================================
# PHẦN 3: MỘT SỐ HÀM CÓ SẴN HỮU ÍCH TRONG PYTHON
# ==============================================================================
def demo_ham_co_san():
    print("\n--- MỘT SỐ HÀM CÓ SẴN ---")
    print("abs(-25)         =", abs(-25))
    print("round(3.14159,2) =", round(3.14159, 2))
    print("max(4, 9, 2)     =", max(4, 9, 2))
    print("min(4, 9, 2)     =", min(4, 9, 2))
    print("sum([1, 2, 3])   =", sum([1, 2, 3]))
    print("len('Python')    =", len("Python"))


# ==============================================================================
# PHẦN 4: BIẾN CỤC BỘ (LOCAL) vs BIẾN TOÀN CỤC (GLOBAL)
# ==============================================================================
diem_toan_cuc = 100   # Biến toàn cục (Global) - nằm ngoài mọi hàm


def thu_pham_vi():
    diem_cuc_bo = 50  # Biến cục bộ (Local) - chỉ tồn tại bên trong hàm này!
    print(f"Trong hàm đọc được biến toàn cục: {diem_toan_cuc}, biến cục bộ: {diem_cuc_bo}")


# ==============================================================================
# PHẦN 5: DỰ ÁN COMBAT ENGINE — ĐỘNG CƠ ĐẤU BOSS (CHUẨN BỊ HACKATHON BUỔI 14)
# ==============================================================================
def tinh_sat_thuong(cong, giap_quai, ti_le_chi_mang=1.5):
    sat_thuong_goc = max(1, cong - giap_quai)
    if random.randint(1, 5) == 1:
        print("  [CHÍ MẠNG x1.5!]")
        return int(sat_thuong_goc * ti_le_chi_mang)
    return sat_thuong_goc


def hoi_mau(hp_hien_tai, luong_hoi, hp_toi_da=100):
    return min(hp_toi_da, hp_hien_tai + luong_hoi)


def gia_lap_dau_boss():
    random.seed(7)
    hp_boss = 150
    luot = 1
    print("\n--- ĐỘNG CƠ ĐẤU BOSS (COMBAT ENGINE) ---")
    while hp_boss > 0 and luot <= 10:
        dmg = tinh_sat_thuong(35, 10)
        hp_boss = max(0, hp_boss - dmg)
        print(f"Lượt {luot}: Gây {dmg} sát thương -> Boss còn {hp_boss} HP")
        luot += 1
    print("KẾT QUẢ:", "BOSS ĐÃ BỊ HẠ GỤC!" if hp_boss == 0 else "Hết lượt!")


if __name__ == "__main__":
    print("=" * 60)
    print("BÀI 13: THAM SỐ, ĐỐI SỐ, RETURN & PHẠM VI BIẾN")
    print("=" * 60)

    # 1. Tham số & đối số
    chao_nguoi_choi("Gia Huy")
    chao_nguoi_choi("Minh Anh", "Cao Thủ")

    # 2. print vs return
    kq1 = gap_doi_chi_print(5)
    print("Giá trị nhận được từ hàm chỉ print:", kq1)    # None!
    kq2 = gap_doi_co_return(5)
    print("Giá trị nhận được từ hàm return:", kq2, "| Cộng tiếp 10 =", kq2 + 10)

    # 3. Hàm có sẵn & phạm vi biến
    demo_ham_co_san()
    thu_pham_vi()
    print("Ngoài hàm vẫn đọc được diem_toan_cuc:", diem_toan_cuc)

    # 4. Combat Engine
    gia_lap_dau_boss()
