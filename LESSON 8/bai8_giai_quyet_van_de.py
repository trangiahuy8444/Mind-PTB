# -*- coding: utf-8 -*-
"""
KHÓA HỌC: LẬP TRÌNH PYTHON CƠ BẢN (TT-C4K-PTB30)
BÀI 8: LẬP TRÌNH GIẢI QUYẾT VẤN ĐỀ — DỰ ÁN "SINH TỒN TRÊN HOANG ĐẢO"
Thời lượng: 120 phút
Giáo viên: Thầy Huy Trần

Vận dụng tổng hợp 7 buổi đã học: Biến (B1), Ép kiểu (B2), Toán tử (B3),
if-elif-else (B4), Tư duy chia nhỏ bài toán (B5), for (B6) và while True (B7).
"""

import random


# ==============================================================================
# BƯỚC 1: KHỞI TẠO TRẠNG THÁI GAME (GAME STATE)
# ==============================================================================
def tao_trang_thai():
    return {
        "ngay": 1,
        "mau": 100,
        "thuc_an": 80,
        "nuoc_uong": 80,
        "go": 0,
    }


# ==============================================================================
# BƯỚC 2: XỬ LÝ MỘT LƯỢT CHƠI (1 NGÀY TRÔI QUA)
# ==============================================================================
def xu_ly_hanh_dong(state, lua_chon, ngau_nhien=True):
    """Cập nhật chỉ số sau 1 hành động: 1=Săn bắn, 2=Tìm nước, 3=Nghỉ ngơi, 4=Kiếm gỗ."""
    if lua_chon == 1:
        state["thuc_an"] += 30
        state["nuoc_uong"] -= 15
        ket_qua = "Săn bắn: +30 Thức ăn, -15 Nước"
    elif lua_chon == 2:
        state["nuoc_uong"] += 35
        state["thuc_an"] -= 10
        ket_qua = "Tìm suối: +35 Nước, -10 Thức ăn"
    elif lua_chon == 3:
        state["mau"] += 20
        state["thuc_an"] -= 15
        state["nuoc_uong"] -= 15
        ket_qua = "Nghỉ ngơi: +20 Máu, -15 Thức ăn, -15 Nước"
    elif lua_chon == 4:
        state["go"] += 1
        state["mau"] -= 10
        state["thuc_an"] -= 15
        ket_qua = "Chặt gỗ đóng bè: +1 Gỗ, -10 Máu, -15 Thức ăn"
    else:
        ket_qua = "Hành động không hợp lệ!"

    # Sự kiện bất ngờ (20% gặp bão nhiệt đới)
    if ngau_nhien and random.randint(1, 5) == 1:
        state["mau"] -= 15
        ket_qua += " | BÃO TỐ! (-15 Máu)"

    # Hao hụt tự nhiên cuối ngày & giới hạn tối đa 100
    state["thuc_an"] = max(0, min(100, state["thuc_an"] - 5))
    state["nuoc_uong"] = max(0, min(100, state["nuoc_uong"] - 5))
    if state["thuc_an"] == 0 or state["nuoc_uong"] == 0:
        state["mau"] -= 25
    state["mau"] = max(0, min(100, state["mau"]))
    state["ngay"] += 1
    return ket_qua


# ==============================================================================
# BƯỚC 3: KIỂM TRA ĐIỀU KIỆN THẮNG / THUA
# ==============================================================================
def kiem_tra_ket_thuc(state):
    if state["mau"] <= 0:
        return "THUA: Nhân vật đã kiệt sức!"
    if state["go"] >= 4:
        return "THẮNG SỚM: Đóng xong bè gỗ vượt biển thành công!"
    if state["ngay"] > 7:
        return "THẮNG: Sống sót trọn vẹn 7 ngày chờ tàu cứu hộ!"
    return None


# ==============================================================================
# BƯỚC 4: CHẠY MÔ PHỎNG TỰ ĐỘNG 7 NGÀY (KHÔNG CẦN INPUT)
# ==============================================================================
def chay_mo_phong_tu_dong():
    random.seed(42)
    state = tao_trang_thai()
    print("--- MÔ PHỎNG VÒNG LẶP GAME SINH TỒN 7 NGÀY ---")
    while True:
        # AI đơn giản chọn hành động dựa trên chỉ số thấp nhất
        if state["mau"] < 50:
            chon = 3
        elif state["nuoc_uong"] < 40:
            chon = 2
        elif state["thuc_an"] < 40:
            chon = 1
        else:
            chon = 4

        ngay_hien_tai = state["ngay"]
        msg = xu_ly_hanh_dong(state, chon, ngau_nhien=True)
        print(
            f"Ngày {ngay_hien_tai}: {msg} -> "
            f"[Máu:{state['mau']}, Ăn:{state['thuc_an']}, Nước:{state['nuoc_uong']}, Gỗ:{state['go']}]"
        )
        ket_thuc = kiem_tra_ket_thuc(state)
        if ket_thuc is not None:
            print("KẾT QUẢ:", ket_thuc)
            break


# ==============================================================================
# BÀI TOÁN TƯ DUY PHÂN RÃ KHÁC: ĐỔI GIÂY -> GIỜ : PHÚT : GIÂY
# ==============================================================================
def doi_giay(tong_giay):
    gio = tong_giay // 3600
    phan_du = tong_giay % 3600
    phut = phan_du // 60
    giay = phan_du % 60
    return f"{gio:02d}:{phut:02d}:{giay:02d}"


if __name__ == "__main__":
    print("=" * 60)
    print("BÀI 8: LẬP TRÌNH GIẢI QUYẾT VẤN ĐỀ")
    print("=" * 60)

    chay_mo_phong_tu_dong()
    print("\n--- ĐỔI ĐƠN VỊ THỜI GIAN ---")
    print("3665 giây =", doi_giay(3665))
    print("7322 giây =", doi_giay(7322))
