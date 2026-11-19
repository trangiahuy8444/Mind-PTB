# -*- coding: utf-8 -*-
"""
KHÓA HỌC: LẬP TRÌNH PYTHON CƠ BẢN (TT-C4K-PTB30)
BÀI 7: VÒNG LẶP VÔ HẠN (WHILE), BREAK & CONTINUE
Thời lượng: 120 phút
Giáo viên: Thầy Huy Trần

Cách dùng: chạy file này để xem các ví dụ minh họa không chặn input().
Phần thực hành tương tác (nhập mật khẩu, đoán số) nằm ở cuối file, bỏ # để thử.
"""


# ==============================================================================
# PHẦN 1: SO SÁNH FOR vs WHILE — ĐẾM TỪ 1 ĐẾN N
# ==============================================================================
def dem_bang_while(n):
    print(f"\n--- Đếm từ 1 đến {n} bằng while ---")
    i = 1                    # 1. Khởi tạo biến đếm
    while i <= n:            # 2. Điều kiện tiếp tục lặp
        print(i, end=" ")
        i += 1               # 3. CẬP NHẬT biến đếm (quên dòng này -> lặp vô hạn!)
    print()


# ==============================================================================
# PHẦN 2: VÒNG LẶP THEO ĐIỀU KIỆN — TÌM SỐ MŨ 2 ĐẦU TIÊN VƯỢT NGƯỠNG
# ==============================================================================
def luy_thua_vuot_nguong(gioi_han):
    print(f"\n--- Lũy thừa của 2 đầu tiên > {gioi_han} ---")
    val = 1
    mu = 0
    while val <= gioi_han:
        val *= 2
        mu += 1
    print(f"2^{mu} = {val} (> {gioi_han})")
    return val


# ==============================================================================
# PHẦN 3: GIẢ LẬP NHẬP MẬT KHẨU ĐẾN KHI ĐÚNG (WHILE + BREAK)
# ==============================================================================
def gia_lap_dang_nhap(ds_thu, mat_khau_dung="Mindx2026"):
    print(f"\n--- Giả lập đăng nhập (mật khẩu đúng: {mat_khau_dung}) ---")
    idx = 0
    while idx < len(ds_thu):
        nhap = ds_thu[idx]
        idx += 1
        print(f"Lần thử {idx}: '{nhap}' -> ", end="")
        if nhap == mat_khau_dung:
            print("Đăng nhập thành công! (thoát bằng break)")
            break
        print("Mật khẩu không chính xác, mời nhập lại.")
    else:
        print("Hết danh sách thử mà chưa đúng.")


# ==============================================================================
# PHẦN 4: BREAK & CONTINUE TRONG VÒNG LẶP
# ==============================================================================
def demo_break(n, dung_o=6):
    print(f"\n--- Demo break: dừng ngay khi gặp i == {dung_o} ---")
    i = 1
    while i <= n:
        if i == dung_o:
            print(f"[Gặp {dung_o} -> break!]")
            break
        print(i, end=" ")
        i += 1
    print()


def demo_continue(n, bo_qua=3):
    print(f"\n--- Demo continue: bỏ qua khi i == {bo_qua} ---")
    i = 0
    while i < n:
        i += 1               # Chú ý: tăng i TRƯỚC continue để tránh lặp vô hạn!
        if i == bo_qua:
            print(f"[Bỏ qua {bo_qua}]", end=" ")
            continue
        print(i, end=" ")
    print()


# ==============================================================================
# PHẦN 5: WHILE LỒNG NHAU — ĐỒNG HỒ PHÚT : GIÂY MINI
# ==============================================================================
def dong_ho_mini(so_phut=2, so_giay=3):
    print(f"\n--- While lồng nhau: {so_phut} phút × {so_giay} giây ---")
    phut = 0
    while phut < so_phut:
        giay = 0
        while giay < so_giay:
            print(f"{phut:02d}:{giay:02d}", end="  ")
            giay += 1
        print()
        phut += 1


# ==============================================================================
# PHẦN 6: GIẢ LẬP GAME ĐOÁN SỐ BÍ MẬT (TỰ ĐỘNG TÌM KIẾM NHỊ PHÂN)
# ==============================================================================
def gia_lap_doan_so(bi_mat=37, toi_da_luot=7):
    print(f"\n--- Giả lập đoán số bí mật ({bi_mat}) trong 1..50 ---")
    low, high = 1, 50
    luot = 0
    while luot < toi_da_luot:
        luot += 1
        doan = (low + high) // 2
        if doan == bi_mat:
            print(f"Lượt {luot}: Đoán {doan} -> CHÍNH XÁC! Thắng cuộc!")
            break
        elif doan < bi_mat:
            print(f"Lượt {luot}: Đoán {doan} -> Số bí mật LỚN hơn!")
            low = doan + 1
        else:
            print(f"Lượt {luot}: Đoán {doan} -> Số bí mật NHỎ hơn!")
            high = doan - 1


if __name__ == "__main__":
    print("=" * 60)
    print("BÀI 7: VÒNG LẶP WHILE, BREAK & CONTINUE")
    print("=" * 60)

    dem_bang_while(8)
    luy_thua_vuot_nguong(1000)
    gia_lap_dang_nhap(["123456", "admin", "Mindx2026", "abc"])
    demo_break(10, 6)
    demo_continue(6, 3)
    dong_ho_mini(2, 4)
    gia_lap_doan_so(37, 7)

    # ==========================================================================
    # BÀI TẬP TƯƠNG TÁC (bỏ dấu # để tự nhập từ bàn phím)
    # ==========================================================================
    # password = "Mindx2026"
    # while True:
    #     nhap = input("Mời nhập password: ")
    #     if nhap == password:
    #         print("Đăng nhập thành công!")
    #         break
    #     print("Mật khẩu không chính xác!")
