danh_sach_phong = [
    {
        "ma_phong": "P101",
        "loai_phong": "Don",
        "gia": 300000,
        "trang_thai": "Trong",
        "ten_khach": ""
    },
    {
        "ma_phong": "P102",
        "loai_phong": "Doi",
        "gia": 500000,
        "trang_thai": "Trong",
        "ten_khach": ""
    },
    {
        "ma_phong": "P103",
        "loai_phong": "VIP",
        "gia": 900000,
        "trang_thai": "Trong",
        "ten_khach": ""
    },
    {
        "ma_phong": "P104",
        "loai_phong": "Don",
        "gia": 300000,
        "trang_thai": "Trong",
        "ten_khach": ""
    }
]

lich_su_doanh_thu = []


def nhap_so_nguyen(loi_nhac, gia_tri_nho_nhat=None):
    """Nhập số nguyên an toàn bằng try-except."""
    while True:
        try:
            gia_tri = int(input(loi_nhac))

            if gia_tri_nho_nhat is not None and gia_tri < gia_tri_nho_nhat:
                print(
                    f"-> Gia tri phai lon hon hoac bang "
                    f"{gia_tri_nho_nhat}, vui long nhap lai."
                )
                continue

            return gia_tri

        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap mot so nguyen.")


def hien_thi_danh_sach_phong():
    """Hiển thị toàn bộ danh sách phòng."""
    print("\n" + "=" * 75)
    print(
        f"{'Ma phong':<12}"
        f"{'Loai phong':<15}"
        f"{'Gia/dem':>15}"
        f"{'Trang thai':<15}"
        f"{'Khach':<20}"
    )
    print("-" * 75)

    if len(danh_sach_phong) == 0:
        print("-> Chua co phong nao trong danh sach.")
    else:
        for phong in danh_sach_phong:
            print(
                f"{phong['ma_phong']:<12}"
                f"{phong['loai_phong']:<15}"
                f"{phong['gia']:>12,} VND"
                f"{phong['trang_thai']:<15}"
                f"{phong['ten_khach']:<20}"
            )

    print("=" * 75)


def tim_phong_theo_ma(ma_phong):
    """Tìm phòng theo mã phòng."""
    for phong in danh_sach_phong:
        if phong["ma_phong"] == ma_phong:
            return phong

    return None


def xem_phong_trong():
    """Hiển thị các phòng đang trống."""
    phong_trong = [
        phong
        for phong in danh_sach_phong
        if phong["trang_thai"] == "Trong"
    ]

    if len(phong_trong) == 0:
        print("-> Hien khong con phong trong nao.")
        return

    print("\nCAC PHONG DANG TRONG:")
    for phong in phong_trong:
        print(
            f"- {phong['ma_phong']} | "
            f"{phong['loai_phong']} | "
            f"{phong['gia']:,} VND/dem"
        )


def them_phong(ma_phong, loai_phong, gia):
    """Thêm phòng mới."""
    if tim_phong_theo_ma(ma_phong) is not None:
        print(f"-> Ma phong {ma_phong} da ton tai, khong the them.")
        return

    if gia <= 0:
        print("-> Gia phong phai lon hon 0.")
        return

    danh_sach_phong.append(
        {
            "ma_phong": ma_phong,
            "loai_phong": loai_phong,
            "gia": gia,
            "trang_thai": "Trong",
            "ten_khach": ""
        }
    )

    print(f"-> Da them phong {ma_phong} thanh cong.")


def dat_phong(ma_phong, ten_khach):
    """Đặt phòng cho khách."""
    phong = tim_phong_theo_ma(ma_phong)

    if phong is None:
        print(f"-> Khong tim thay phong {ma_phong}.")
        return

    if phong["trang_thai"] == "Da dat":
        print(f"-> Phong {ma_phong} da co khach, khong the dat.")
        return

    if ten_khach == "":
        print("-> Ten khach khong duoc de trong.")
        return

    phong["trang_thai"] = "Da dat"
    phong["ten_khach"] = ten_khach

    print(
        f"-> Dat phong {ma_phong} cho khach "
        f"{ten_khach} thanh cong."
    )


def tra_phong(ma_phong, so_dem):
    """Trả phòng và tính tiền."""
    phong = tim_phong_theo_ma(ma_phong)

    if phong is None:
        print(f"-> Khong tim thay phong {ma_phong}.")
        return

    if phong["trang_thai"] == "Trong":
        print(
            f"-> Phong {ma_phong} dang trong, "
            "khong co khach de tra phong."
        )
        return

    if so_dem <= 0:
        print("-> So dem phai lon hon 0.")
        return

    thanh_tien = phong["gia"] * so_dem

    lich_su_doanh_thu.append(
        {
            "ma_phong": ma_phong,
            "ten_khach": phong["ten_khach"],
            "so_dem": so_dem,
            "thanh_tien": thanh_tien
        }
    )

    print(
        f"-> Khach {phong['ten_khach']} tra phong "
        f"{ma_phong} sau {so_dem} dem."
    )
    print(
        f"-> Tong tien phai thanh toan: "
        f"{thanh_tien:,} VND"
    )

    phong["trang_thai"] = "Trong"
    phong["ten_khach"] = ""


def thong_ke_doanh_thu():
    """Hiển thị lịch sử giao dịch và tổng doanh thu."""
    if len(lich_su_doanh_thu) == 0:
        print("-> Chua co giao dich tra phong nao.")
        return

    tong_doanh_thu = 0

    print("\nLICH SU GIAO DICH:")
    print("-" * 60)

    for giao_dich in lich_su_doanh_thu:
        print(
            f"- Phong: {giao_dich['ma_phong']} | "
            f"Khach: {giao_dich['ten_khach']} | "
            f"So dem: {giao_dich['so_dem']} | "
            f"Thanh tien: {giao_dich['thanh_tien']:,} VND"
        )

        tong_doanh_thu += giao_dich["thanh_tien"]

    print("-" * 60)
    print(f">>> TONG DOANH THU: {tong_doanh_thu:,} VND")


def hien_thi_menu():
    """Hiển thị menu chính."""
    print("\n===== QUAN LY DAT PHONG KHACH SAN MINI =====")
    print("1. Hien thi danh sach tat ca phong")
    print("2. Xem cac phong dang trong")
    print("3. Them phong moi")
    print("4. Dat phong cho khach")
    print("5. Tra phong / Thanh toan")
    print("6. Thong ke doanh thu")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    """Điều khiển chương trình chính."""
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach_phong()

        elif lua_chon == "2":
            xem_phong_trong()

        elif lua_chon == "3":
            ma_phong = input("Nhap ma phong moi: ").strip().upper()
            loai_phong = input(
                "Nhap loai phong (Don/Doi/VIP): "
            ).strip().title()

            gia = nhap_so_nguyen(
                "Nhap gia phong/dem: ",
                gia_tri_nho_nhat=1
            )

            them_phong(ma_phong, loai_phong, gia)

        elif lua_chon == "4":
            ma_phong = input(
                "Nhap ma phong can dat: "
            ).strip().upper()

            ten_khach = input(
                "Nhap ten khach: "
            ).strip().title()

            dat_phong(ma_phong, ten_khach)

        elif lua_chon == "5":
            ma_phong = input(
                "Nhap ma phong can tra: "
            ).strip().upper()

            so_dem = nhap_so_nguyen(
                "Nhap so dem da o: ",
                gia_tri_nho_nhat=1
            )

            tra_phong(ma_phong, so_dem)

        elif lua_chon == "6":
            thong_ke_doanh_thu()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()