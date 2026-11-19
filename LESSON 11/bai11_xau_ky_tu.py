# -*- coding: utf-8 -*-
"""
KHÓA HỌC: LẬP TRÌNH PYTHON CƠ BẢN (TT-C4K-PTB30)
BÀI 11: XÂU KÝ TỰ (STRING) — CẮT CHUỖI & MẬT MÃ ĐIỆP VIÊN
Thời lượng: 120 phút
Giáo viên: Thầy Huy Trần
"""


# ==============================================================================
# PHẦN 1: CHỈ SỐ & CẮT XÂU (SLICING) & TÍNH BẤT BIẾN (IMMUTABLE)
# ==============================================================================
def demo_slicing():
    s = "MindX Python"
    print("Chuỗi gốc:", repr(s), "| Độ dài len(s):", len(s))
    print("s[0]:", s[0], "| s[-1]:", s[-1])
    print("s[0:5]  ->", repr(s[0:5]))      # 'MindX'
    print("s[6:]   ->", repr(s[6:]))       # 'Python'
    print("s[:5]   ->", repr(s[:5]))       # 'MindX'
    print("s[::2]  ->", repr(s[::2]))      # Lấy cách 1 ký tự
    print("s[::-1] ->", repr(s[::-1]))     # Đảo ngược chuỗi

    # Lưu ý: s[0] = 'K' sẽ gây TypeError vì str là bất biến!
    # Cách tạo chuỗi mới thay thế:
    s_moi = "K" + s[1:]
    print("Tạo chuỗi mới thay chữ đầu:", s_moi)


# ==============================================================================
# PHẦN 2: CÁC PHƯƠNG THỨC XỬ LÝ VĂN BẢN THÔNG DỤNG
# ==============================================================================
def demo_phuong_thuc():
    cau = "   Chào mừng bạn đến với MindX Python   "
    print("\n--- PHƯƠNG THỨC XỬ LÝ XÂU ---")
    sach = cau.strip()
    print("strip() :", repr(sach))
    print("upper() :", sach.upper())
    print("lower() :", sach.lower())
    print("replace :", sach.replace("Python", "Cơ Bản"))
    tu = sach.split()
    print("split() :", tu, "| Số từ:", len(tu))
    ghep = "-".join(tu)
    print("join()  :", ghep)


# ==============================================================================
# PHẦN 3: BỘ MÃ HÓA & GIẢI MÃ MẬT MÃ CAESAR (ORD & CHR)
# ==============================================================================
def ma_hoa_caesar(van_ban, k):
    ket_qua = ""
    for ch in van_ban:
        if "A" <= ch <= "Z":
            ket_qua += chr((ord(ch) - ord("A") + k) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            ket_qua += chr((ord(ch) - ord("a") + k) % 26 + ord("a"))
        else:
            ket_qua += ch
    return ket_qua


def giai_ma_caesar(mat_thu, k):
    return ma_hoa_caesar(mat_thu, -k)


# ==============================================================================
# PHẦN 4: KIỂM TRA XÂU ĐỐI XỨNG (PALINDROME)
# ==============================================================================
def la_doi_xung(s):
    chuan = s.strip().lower()
    return chuan == chuan[::-1]


if __name__ == "__main__":
    print("=" * 60)
    print("BÀI 11: XÂU KÝ TỰ (STRING)")
    print("=" * 60)

    demo_slicing()
    demo_phuong_thuc()

    goc = "MindX Spy 2026!"
    ma = ma_hoa_caesar(goc, 3)
    print("\n--- MẬT MÃ CAESAR (k=3) ---")
    print("Bản gốc :", goc)
    print("Mã hóa  :", ma)
    print("Giải mã :", giai_ma_caesar(ma, 3))

    print("\n--- KIỂM TRA ĐỐI XỨNG ---")
    for test in ["radar", "Level", "Python"]:
        print(f"'{test}' đối xứng? -> {la_doi_xung(test)}")
