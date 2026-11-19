# -*- coding: utf-8 -*-
"""
KHÓA HỌC: LẬP TRÌNH PYTHON CƠ BẢN (TT-C4K-PTB30)
BÀI 9: KIỂM TRA VÒNG LẶP & NHẬP MÔN DANH SÁCH (LIST)
Thời lượng: 120 phút
Giáo viên: Thầy Huy Trần
"""


# ==============================================================================
# PHẦN 1: ÔN TẬP CHECKPOINT 2 (VÒNG LẶP)
# ==============================================================================
def tong_chan(n):
    tong = 0
    for i in range(2, n + 1, 2):
        tong += i
    return tong


def mo_phong_atm_3_lan(ds_pin, pin_dung="2468"):
    lan = 0
    while lan < len(ds_pin) and lan < 3:
        pin = ds_pin[lan]
        lan += 1
        if pin == pin_dung:
            return f"Mở khóa thành công ở lần thứ {lan}"
    return "Thẻ đã bị khóa do sai quá 3 lần!"


# ==============================================================================
# PHẦN 2: KHỞI TẠO DANH SÁCH (LIST) & CHỈ SỐ DƯƠNG / ÂM
# ==============================================================================
def demo_khoi_tao_va_index():
    ds_so = [10, 25, 30, 45]
    ds_hoc_sinh = ["Tuấn Kiệt", "Công Long", "Quý Anh", "Quang Anh", "Gia Bảo"]
    ds_hon_hop = ["MindX", 2026, 9.5, True]

    print("\n--- KHỞI TẠO & CHỈ SỐ LIST ---")
    print("Danh sách học sinh:", ds_hoc_sinh)
    print("Số lượng phần tử len():", len(ds_hoc_sinh))
    print("Bạn đầu tiên ds[0]:", ds_hoc_sinh[0])
    print("Bạn thứ ba ds[2]:", ds_hoc_sinh[2])
    print("Bạn cuối cùng ds[-1]:", ds_hoc_sinh[-1])
    print("Bạn kế cuối ds[-2]:", ds_hoc_sinh[-2])
    print("Ví dụ list hỗn hợp:", ds_hon_hop, "| tổng ds_so:", sum(ds_so))


# ==============================================================================
# PHẦN 3: HAI CÁCH DUYỆT DANH SÁCH BẰNG FOR
# ==============================================================================
def demo_2_cach_duyet():
    tui_do = ["Dao găm", "Bật lửa", "Cá nướng", "Bản đồ"]
    print("\n--- CÁCH 1: Duyệt trực tiếp phần tử (for item in list) ---")
    for mon in tui_do:
        print(" - Món đồ:", mon)

    print("\n--- CÁCH 2: Duyệt theo chỉ số (for i in range(len(list))) ---")
    for i in range(len(tui_do)):
        print(f" Ngăn [{i}] (STT {i + 1}): {tui_do[i]}")


# ==============================================================================
# PHẦN 4: ỨNG DỤNG TÍNH TỔNG, TÌM MAX & KIỂM TRA TỒN TẠI (IN)
# ==============================================================================
def phan_tich_diem(ds_diem):
    print("\n--- PHÂN TÍCH DANH SÁCH ĐIỂM:", ds_diem, "---")
    tong = 0
    lon_nhat = ds_diem[0]
    for d in ds_diem:
        tong += d
        if d > lon_nhat:
            lon_nhat = d
    diem_tb = tong / len(ds_diem)
    print(f"Tổng điểm: {tong} | Điểm TB: {diem_tb:.2f} | Cao nhất: {lon_nhat}")

    if 10 in ds_diem:
        print("Có bạn đạt điểm 10 tuyệt đối!")
    else:
        print("Chưa có điểm 10.")


if __name__ == "__main__":
    print("=" * 60)
    print("BÀI 9: KIỂM TRA VÒNG LẶP & NHẬP MÔN DANH SÁCH (LIST)")
    print("=" * 60)

    print("Tổng số chẵn 1..10 =", tong_chan(10))
    print("ATM thử ['1111', '2222', '2468'] ->", mo_phong_atm_3_lan(["1111", "2222", "2468"]))
    demo_khoi_tao_va_index()
    demo_2_cach_duyet()
    phan_tich_diem([7.5, 9.0, 6.5, 10.0, 8.0])
