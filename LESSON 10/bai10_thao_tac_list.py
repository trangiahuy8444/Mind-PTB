# -*- coding: utf-8 -*-
"""
KHÓA HỌC: LẬP TRÌNH PYTHON CƠ BẢN (TT-C4K-PTB30)
BÀI 10: DANH SÁCH VÀ HƠN THẾ NỮA — THAO TÁC CRUD (THÊM, XÓA, SỬA)
Thời lượng: 120 phút
Giáo viên: Thầy Huy Trần
"""


# ==============================================================================
# PHẦN 1: THÊM PHẦN TỬ (.append, .insert) & SỬA PHẦN TỬ (ds[i] = ...)
# ==============================================================================
def demo_them_va_sua():
    balo = ["Kiếm gỗ", "Bánh mì"]
    print("Ban đầu:", balo)

    # 1. append(): luôn thêm vào CUỐI danh sách
    balo.append("Đuốc")
    print("Sau append('Đuốc'):", balo)

    # 2. insert(vị_trí, giá_trị): chèn vào vị trí bất kỳ
    balo.insert(1, "Khiên sắt")
    print("Sau insert(1, 'Khiên sắt'):", balo)

    # 3. Sửa phần tử theo chỉ số
    balo[0] = "Kiếm kim cương"
    print("Sau balo[0] = 'Kiếm kim cương':", balo)
    return balo


# ==============================================================================
# PHẦN 2: XÓA PHẦN TỬ (.remove, .pop) & PHÒNG CHỐNG LỖI VALUEERROR
# ==============================================================================
def demo_xoa_an_toan():
    balo = ["Kiếm kim cương", "Khiên sắt", "Bánh mì", "Đuốc"]
    print("\n--- DEMO XÓA PHẦN TỬ ---")
    print("Trước khi xóa:", balo)

    # 1. remove(gia_tri): xóa theo TÊN giá trị (chỉ xóa phần tử đầu tiên khớp)
    mon_can_vut = "Bánh mì"
    if mon_can_vut in balo:
        balo.remove(mon_can_vut)
        print(f"Đã xóa '{mon_can_vut}':", balo)

    # Kiểm tra trước khi xóa món không có -> tránh ValueError!
    mon_la = "Bom"
    if mon_la in balo:
        balo.remove(mon_la)
    else:
        print(f"Cảnh báo an toàn: '{mon_la}' không có trong balo -> tránh được ValueError!")

    # 2. pop(index): xóa theo VỊ TRÍ và trả về giá trị vừa lấy ra
    mon_cuoi = balo.pop()
    print(f"Đã pop() món cuối '{mon_cuoi}', balo còn:", balo)


# ==============================================================================
# PHẦN 3: SẮP XẾP & THỐNG KÊ (.sort, .reverse, sum, min, max)
# ==============================================================================
def demo_sap_xep_thong_ke():
    diem = [7.5, 9.0, 6.0, 10.0, 8.5]
    print("\n--- SẮP XẾP & THỐNG KÊ ---")
    print("Gốc:", diem)

    diem.sort()
    print("Tăng dần sort():", diem)

    diem.sort(reverse=True)
    print("Giảm dần sort(reverse=True):", diem)

    diem.reverse()
    print("Đảo ngược lại reverse():", diem)

    print(f"Tổng: {sum(diem)} | Nhỏ nhất: {min(diem)} | Lớn nhất: {max(diem)}")


# ==============================================================================
# PHẦN 4: MÔ PHỎNG CỬA HÀNG MINECRAFT (MUA / BÁN BẰNG LIST + VÍ XU)
# ==============================================================================
def mo_phong_shop_minecraft():
    print("\n--- MÔ PHỎNG SHOP MINECRAFT ---")
    xu = 100
    balo = ["Táo"]
    gia_shop = {"Kiếm sắt": 40, "Cung tên": 35, "Giáp vàng": 70}

    for mon, gia in [("Kiếm sắt", gia_shop["Kiếm sắt"]), ("Giáp vàng", gia_shop["Giáp vàng"]), ("Cung tên", gia_shop["Cung tên"])]:
        if len(balo) >= 5:
            print("Balo đã đầy!")
        elif xu >= gia:
            xu -= gia
            balo.append(mon)
            print(f"Mua thành công {mon} (-{gia} xu) -> Ví: {xu} xu | Balo: {balo}")
        else:
            print(f"Không đủ xu mua {mon} (cần {gia}, có {xu})!")


if __name__ == "__main__":
    print("=" * 60)
    print("BÀI 10: DANH SÁCH & THAO TÁC CRUD (THÊM, XÓA, SỬA)")
    print("=" * 60)

    demo_them_va_sua()
    demo_xoa_an_toan()
    demo_sap_xep_thong_ke()
    mo_phong_shop_minecraft()
