import sqlite3

TEN_FILE_CSDL = "chi_tieu.db"


def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)


def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS chi_tieu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            noi_dung TEXT NOT NULL,
            so_tien INTEGER NOT NULL,
            danh_muc TEXT NOT NULL,
            ngay TEXT NOT NULL
        )
    """)
    ket_noi.commit()
    ket_noi.close()


def them_chi_tieu(noi_dung, so_tien, danh_muc, ngay):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO chi_tieu (noi_dung, so_tien, danh_muc, ngay) VALUES (?, ?, ?, ?)",
        (noi_dung, so_tien, danh_muc, ngay)
    )
    ket_noi.commit()
    ket_noi.close()


def lay_toan_bo_chi_tieu():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "SELECT id, noi_dung, so_tien, danh_muc, ngay FROM chi_tieu ORDER BY ngay DESC, id DESC"
    )
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua


def tim_kiem_chi_tieu(tu_khoa):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "SELECT id, noi_dung, so_tien, danh_muc, ngay FROM chi_tieu "
        "WHERE noi_dung LIKE ? ORDER BY ngay DESC, id DESC",
        (f"%{tu_khoa}%",)
    )
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua


def sua_chi_tieu(id_chi_tieu, noi_dung, so_tien, danh_muc, ngay):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "UPDATE chi_tieu SET noi_dung = ?, so_tien = ?, danh_muc = ?, ngay = ? WHERE id = ?",
        (noi_dung, so_tien, danh_muc, ngay, id_chi_tieu)
    )
    ket_noi.commit()
    ket_noi.close()


def xoa_chi_tieu(id_chi_tieu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM chi_tieu WHERE id = ?", (id_chi_tieu,))
    ket_noi.commit()
    ket_noi.close()


def tong_chi_tieu():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT COALESCE(SUM(so_tien), 0) FROM chi_tieu")
    tong = con_tro.fetchone()[0]
    ket_noi.close()
    return tong


def thong_ke_theo_danh_muc():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "SELECT danh_muc, SUM(so_tien) FROM chi_tieu GROUP BY danh_muc ORDER BY SUM(so_tien) DESC"
    )
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua