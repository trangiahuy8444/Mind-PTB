# -*- coding: utf-8 -*-
"""
KHÓA HỌC: LẬP TRÌNH PYTHON CƠ BẢN (TT-C4K-PTB30)
BÀI 12: HÀM (FUNCTION) — CHIA NHỎ CÔNG VIỆC & XƯỞNG PHÉP THUẬT
Thời lượng: 120 phút
Giáo viên: Thầy Huy Trần
"""


# ==============================================================================
# PHẦN 1: ĐỊNH NGHĨA HÀM ĐƠN GIẢN (DEF) & TRIẾT LÝ DRY (DON'T REPEAT YOURSELF)
# ==============================================================================
def ke_duong_vien():
    print("=" * 42)


def chao_mung():
    ke_duong_vien()
    print("  CHÀO MỪNG ĐẾN VỚI XƯỞNG PHÉP THUẬT!  ")
    ke_duong_vien()


# ==============================================================================
# PHẦN 2: THƯ VIỆN KỸ NĂNG ANH HÙNG & HÀM GỌI HÀM (COMBO CHIÊU THỨC)
# ==============================================================================
def danh_thuong():
    print("[Chiêu 1] Chém thường gây 20 sát thương!")


def hoi_mau():
    print("[Chiêu 2] Uống bình máu +30 HP!")


def chieu_cuoi():
    print("[Chiêu 3 - ULTIMATE] Bão Lửa Hủy Diệt gây 100 sát thương!")


def combo_huy_diet():
    print("\n--- KÍCH HOẠT COMBO LIÊN HOÀN ---")
    ke_duong_vien()
    danh_thuong()
    danh_thuong()
    hoi_mau()
    chieu_cuoi()
    ke_duong_vien()


# ==============================================================================
# PHẦN 3: BẪY QUÊN GỌI HÀM & THỨ TỰ THỰC THI
# ==============================================================================
def demo_thu_tu_thuc_thi():
    print("\n--- DEMO THỨ TỰ THỰC THI ---")
    print("1. Chương trình bắt đầu")

    def buoc_giua():
        print("2. Bên trong thân hàm buoc_giua()")

    print("1b. Đã định nghĩa hàm xong (chưa chạy thân hàm!)")
    buoc_giua()
    print("3. Quay lại dòng ngay sau lời gọi hàm!")


if __name__ == "__main__":
    print("=" * 60)
    print("BÀI 12: HÀM (FUNCTION) — CHIA NHỎ CÔNG VIỆC")
    print("=" * 60)

    chao_mung()
    combo_huy_diet()
    demo_thu_tu_thuc_thi()
