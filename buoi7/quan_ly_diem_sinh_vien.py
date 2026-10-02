danh_sach_sv = [
    {
        "ma_sv": "SV001",
        "ho_ten": "Vuong Quoc Manh",
        "nam_sinh": 2006,
        "diem_toan": 8.5,
        "diem_ly": 7.5,
        "diem_hoa": 9.0,
        "diem_tb": 8.33,
        "xep_loai": "Gioi"
    },
    {
        "ma_sv": "SV002",
        "ho_ten": "Nguyen Van A",
        "nam_sinh": 2006,
        "diem_toan": 6.5,
        "diem_ly": 7.0,
        "diem_hoa": 6.0,
        "diem_tb": 6.5,
        "xep_loai": "Kha"
    },
    {
        "ma_sv": "SV003",
        "ho_ten": "Le Van B",
        "nam_sinh": 2005,
        "diem_toan": 5.5,
        "diem_ly": 5.0,
        "diem_hoa": 5.0,
        "diem_tb": 5.17,
        "xep_loai": "Trung binh"
    },
    {
        "ma_sv": "SV004",
        "ho_ten": "Tran Thi C",
        "nam_sinh": 2006,
        "diem_toan": 4.5,
        "diem_ly": 5.0,
        "diem_hoa": 4.0,
        "diem_tb": 4.5,
        "xep_loai": "Yeu"
    }
]

def tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa):
    return round((diem_toan + diem_ly + diem_hoa) / 3, 2)


def xep_loai_sinh_vien(diem_tb):
    if diem_tb >= 8.0:
        return "Gioi"
    elif diem_tb >= 6.5:
        return "Kha"
    elif diem_tb >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"
    
def cap_nhat_ket_qua(sinh_vien):
    sinh_vien["diem_tb"] = tinh_diem_trung_binh(
        sinh_vien["diem_toan"],
        sinh_vien["diem_ly"],
        sinh_vien["diem_hoa"]
    )

    sinh_vien["xep_loai"] = xep_loai_sinh_vien(
        sinh_vien["diem_tb"]
    )


def nhap_so_nguyen(loi_nhac, gia_tri_nho_nhat=None):
    while True:
        try:
            gia_tri = int(input(loi_nhac))

            if (
                gia_tri_nho_nhat is not None
                and gia_tri < gia_tri_nho_nhat
            ):
                print(
                    f"-> Gia tri phai lon hon hoac bang "
                    f"{gia_tri_nho_nhat}, vui long nhap lai."
                )
                continue

            return gia_tri

        except ValueError:
            print(
                "-> Du lieu khong hop le, "
                "vui long nhap mot so nguyen."
            )


def nhap_diem(loi_nhac):
    while True:
        try:
            diem = float(input(loi_nhac))

            if 0 <= diem <= 10:
                return diem

            print("-> Diem phai nam trong khoang tu 0 den 10.")

        except ValueError:
            print(
                "-> Du lieu khong hop le, "
                "vui long nhap mot so."
            )


def tim_sinh_vien_theo_ma(ma_sv):
    for sinh_vien in danh_sach_sv:
        if sinh_vien["ma_sv"] == ma_sv:
            return sinh_vien

    return None


def hien_thi_danh_sach():
    print("\n" + "=" * 115)
    print(
        f"{'Ma SV':<10}"
        f"{'Ho ten':<25}"
        f"{'Nam sinh':<12}"
        f"{'Toan':>8}"
        f"{'Ly':>8}"
        f"{'Hoa':>8}"
        f"{'Diem TB':>10}"
        f"{'Xep loai':<15}"
    )
    print("-" * 115)

    if len(danh_sach_sv) == 0:
        print("-> Danh sach sinh vien dang rong.")
        print("=" * 115)
        return

    for sinh_vien in danh_sach_sv:
        cap_nhat_ket_qua(sinh_vien)

        print(
            f"{sinh_vien['ma_sv']:<10}"
            f"{sinh_vien['ho_ten']:<25}"
            f"{sinh_vien['nam_sinh']:<12}"
            f"{sinh_vien['diem_toan']:>8.2f}"
            f"{sinh_vien['diem_ly']:>8.2f}"
            f"{sinh_vien['diem_hoa']:>8.2f}"
            f"{sinh_vien['diem_tb']:>10.2f}"
            f"{sinh_vien['xep_loai']:<15}"
        )

    print("=" * 115)
    

def them_sinh_vien():
    ma_sv = input("Nhap ma sinh vien moi: ").strip().upper()

    if ma_sv == "":
        print("-> Ma sinh vien khong duoc de trong.")
        return

    if tim_sinh_vien_theo_ma(ma_sv) is not None:
        print(f"-> Ma sinh vien {ma_sv} da ton tai.")
        return

    ho_ten = input("Nhap ho ten sinh vien: ").strip().title()

    if ho_ten == "":
        print("-> Ho ten khong duoc de trong.")
        return

    nam_sinh = nhap_so_nguyen(
        "Nhap nam sinh: ",
        gia_tri_nho_nhat=1900
    )

    diem_toan = nhap_diem("Nhap diem Toan: ")
    diem_ly = nhap_diem("Nhap diem Ly: ")
    diem_hoa = nhap_diem("Nhap diem Hoa: ")

    sinh_vien = {
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "nam_sinh": nam_sinh,
        "diem_toan": diem_toan,
        "diem_ly": diem_ly,
        "diem_hoa": diem_hoa,
        "diem_tb": 0,
        "xep_loai": ""
    }

    cap_nhat_ket_qua(sinh_vien)
    danh_sach_sv.append(sinh_vien)

    print(f"-> Da them sinh vien {ma_sv} thanh cong.")


def sua_sinh_vien():
    ma_sv = input("Nhap ma sinh vien can sua: ").strip().upper()
    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    print(f"-> Dang sua sinh vien: {sinh_vien['ho_ten']}")

    ho_ten_moi = input("Nhap ho ten moi: ").strip().title()

    if ho_ten_moi != "":
        sinh_vien["ho_ten"] = ho_ten_moi

    sinh_vien["nam_sinh"] = nhap_so_nguyen(
        "Nhap nam sinh moi: ",
        gia_tri_nho_nhat=1900
    )

    sinh_vien["diem_toan"] = nhap_diem(
        "Nhap diem Toan moi: "
    )
    sinh_vien["diem_ly"] = nhap_diem(
        "Nhap diem Ly moi: "
    )
    sinh_vien["diem_hoa"] = nhap_diem(
        "Nhap diem Hoa moi: "
    )

    cap_nhat_ket_qua(sinh_vien)

    print(f"-> Da cap nhat sinh vien {ma_sv} thanh cong.")


def xoa_sinh_vien():
    ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()
    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    danh_sach_sv.remove(sinh_vien)

    print(f"-> Da xoa sinh vien {ma_sv} thanh cong.")


def tim_kiem_sinh_vien():
    tu_khoa = input(
        "Nhap ma sinh vien hoac ten can tim: "
    ).strip().lower()

    ket_qua = [
        sinh_vien
        for sinh_vien in danh_sach_sv
        if tu_khoa in sinh_vien["ma_sv"].lower()
        or tu_khoa in sinh_vien["ho_ten"].lower()
    ]

    if len(ket_qua) == 0:
        print("-> Khong tim thay sinh vien phu hop.")
        return

    print("\nKET QUA TIM KIEM:")
    for sinh_vien in ket_qua:
        print(
            f"- {sinh_vien['ma_sv']} | "
            f"{sinh_vien['ho_ten']} | "
            f"DTB: {sinh_vien['diem_tb']:.2f} | "
            f"Xep loai: {sinh_vien['xep_loai']}"
        )


def sap_xep_theo_diem():
    if len(danh_sach_sv) == 0:
        print("-> Danh sach sinh vien dang rong.")
        return

    for sinh_vien in danh_sach_sv:
        cap_nhat_ket_qua(sinh_vien)

    danh_sach_sv.sort(
        key=lambda sinh_vien: sinh_vien["diem_tb"],
        reverse=True
    )

    print(
        "-> Da sap xep sinh vien "
        "theo diem trung binh giam dan."
    )

    print("\nDANH SACH SINH VIEN SAU KHI SAP XEP:")
    hien_thi_danh_sach()


def thong_ke():
    if len(danh_sach_sv) == 0:
        print("-> Chua co sinh vien de thong ke.")
        return

    so_luong_gioi = 0
    so_luong_kha = 0
    so_luong_trung_binh = 0
    so_luong_yeu = 0
    tong_diem = 0

    for sinh_vien in danh_sach_sv:
        cap_nhat_ket_qua(sinh_vien)

        tong_diem += sinh_vien["diem_tb"]

        if sinh_vien["xep_loai"] == "Gioi":
            so_luong_gioi += 1

        elif sinh_vien["xep_loai"] == "Kha":
            so_luong_kha += 1

        elif sinh_vien["xep_loai"] == "Trung binh":
            so_luong_trung_binh += 1

        elif sinh_vien["xep_loai"] == "Yeu":
            so_luong_yeu += 1

    diem_cao_nhat = max(
        sinh_vien["diem_tb"]
        for sinh_vien in danh_sach_sv
    )

    diem_thap_nhat = min(
        sinh_vien["diem_tb"]
        for sinh_vien in danh_sach_sv
    )

    diem_tb_lop = round(
        tong_diem / len(danh_sach_sv),
        2
    )

    print("\nTHONG KE KET QUA HOC TAP")
    print("-" * 40)
    print(f"Tong so sinh vien: {len(danh_sach_sv)}")
    print(f"So sinh vien Gioi: {so_luong_gioi}")
    print(f"So sinh vien Kha: {so_luong_kha}")
    print(f"So sinh vien Trung binh: {so_luong_trung_binh}")
    print(f"So sinh vien Yeu: {so_luong_yeu}")
    print(f"Diem trung binh cua lop: {diem_tb_lop}")
    print(f"Diem cao nhat: {diem_cao_nhat}")
    print(f"Diem thap nhat: {diem_thap_nhat}")

def hien_thi_menu():
    print("\n===== QUAN LY DIEM SINH VIEN =====")
    print("1. Hien thi danh sach sinh vien")
    print("2. Them sinh vien moi")
    print("3. Sua thong tin sinh vien")
    print("4. Xoa sinh vien")
    print("5. Tim kiem sinh vien")
    print("6. Sap xep theo diem trung binh")
    print("7. Thong ke ket qua hoc tap")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach()

        elif lua_chon == "2":
            them_sinh_vien()

        elif lua_chon == "3":
            sua_sinh_vien()

        elif lua_chon == "4":
            xoa_sinh_vien()

        elif lua_chon == "5":
            tim_kiem_sinh_vien()

        elif lua_chon == "6":
            sap_xep_theo_diem()

        elif lua_chon == "7":
            thong_ke()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()