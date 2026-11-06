import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_chi_tieu as db

DANH_SACH_DANH_MUC = ["An uong", "Di chuyen", "Hoc tap", "Giai tri", "Mua sam", "Khac"]


class UngDungChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Chi tieu ca nhan")
        self.geometry("720x560")
        self.resizable(False, False)
        self.id_dang_chon = None
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Noi dung:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_noi_dung = tk.Entry(khung_nhap, width=30)
        self.o_noi_dung.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="So tien (VND):").grid(row=0, column=2, sticky="w", pady=5)
        self.o_so_tien = tk.Entry(khung_nhap, width=20)
        self.o_so_tien.grid(row=0, column=3, padx=10, pady=5)

        tk.Label(khung_nhap, text="Danh muc:").grid(row=1, column=0, sticky="w", pady=5)
        self.chon_danh_muc = ttk.Combobox(khung_nhap, values=DANH_SACH_DANH_MUC,
                                          width=27, state="readonly")
        self.chon_danh_muc.current(0)
        self.chon_danh_muc.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Ngay (YYYY-MM-DD):").grid(row=1, column=2, sticky="w", pady=5)
        self.o_ngay = tk.Entry(khung_nhap, width=20)
        self.o_ngay.grid(row=1, column=3, padx=10, pady=5)
        self.dat_ngay_hom_nay()

        khung_nut_nhap = tk.Frame(self)
        khung_nut_nhap.pack(pady=5)
        tk.Button(khung_nut_nhap, text="Them", width=12,
                  command=self.xu_ly_them).grid(row=0, column=0, padx=5)
        tk.Button(khung_nut_nhap, text="Cap nhat", width=12,
                  command=self.xu_ly_cap_nhat).grid(row=0, column=1, padx=5)
        tk.Button(khung_nut_nhap, text="Xoa", width=12,
                  command=self.xu_ly_xoa).grid(row=0, column=2, padx=5)
        tk.Button(khung_nut_nhap, text="Lam moi o nhap", width=14,
                  command=self.xoa_o_nhap).grid(row=0, column=3, padx=5)

        khung_tim = tk.Frame(self)
        khung_tim.pack(pady=5, padx=10, fill="x")
        tk.Label(khung_tim, text="Tim theo noi dung:").pack(side="left")
        self.o_tim_kiem = tk.Entry(khung_tim, width=30)
        self.o_tim_kiem.pack(side="left", padx=10)
        tk.Button(khung_tim, text="Tim", command=self.xu_ly_tim_kiem).pack(side="left", padx=5)
        tk.Button(khung_tim, text="Hien tat ca", command=self.tai_lai_danh_sach).pack(side="left")

        khung_bang = tk.Frame(self)
        khung_bang.pack(pady=5, padx=10, fill="both", expand=True)
        cac_cot = ("id", "noi_dung", "so_tien", "danh_muc", "ngay")
        self.bang = ttk.Treeview(khung_bang, columns=cac_cot, show="headings", height=12)
        for cot, tieu_de, rong in [("id", "ID", 40), ("noi_dung", "Noi dung", 240),
                                   ("so_tien", "So tien", 110), ("danh_muc", "Danh muc", 120),
                                   ("ngay", "Ngay", 110)]:
            self.bang.heading(cot, text=tieu_de)
            self.bang.column(cot, width=rong, anchor="center" if cot != "noi_dung" else "w")
        self.bang.pack(side="left", fill="both", expand=True)
        thanh_cuon = tk.Scrollbar(khung_bang, orient="vertical", command=self.bang.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.bang.config(yscrollcommand=thanh_cuon.set)
        self.bang.bind("<<TreeviewSelect>>", self.khi_chon_dong)

        khung_duoi = tk.Frame(self)
        khung_duoi.pack(pady=10, padx=10, fill="x")
        self.nhan_tong = tk.Label(khung_duoi, text="Tong chi tieu: 0 VND",
                                  font=("Arial", 11, "bold"))
        self.nhan_tong.pack(side="left")
        tk.Button(khung_duoi, text="Thong ke theo danh muc",
                  command=self.xu_ly_thong_ke).pack(side="right")

    # ---------- Ham tro giup ----------
    def dat_ngay_hom_nay(self):
        self.o_ngay.delete(0, tk.END)
        self.o_ngay.insert(0, datetime.now().strftime("%Y-%m-%d"))

    def xoa_o_nhap(self):
        self.o_noi_dung.delete(0, tk.END)
        self.o_so_tien.delete(0, tk.END)
        self.chon_danh_muc.current(0)
        self.dat_ngay_hom_nay()
        self.id_dang_chon = None
        self.bang.selection_remove(self.bang.selection())

    def doc_va_kiem_tra_du_lieu(self):
        """Tra ve (noi_dung, so_tien, danh_muc, ngay) neu hop le, nguoc lai None."""
        noi_dung = self.o_noi_dung.get().strip()
        so_tien_chuoi = self.o_so_tien.get().strip()
        danh_muc = self.chon_danh_muc.get()
        ngay = self.o_ngay.get().strip()

        if noi_dung == "" or so_tien_chuoi == "" or ngay == "":
            messagebox.showerror("Loi", "Vui long nhap day du noi dung, so tien va ngay.")
            return None
        try:
            so_tien = int(so_tien_chuoi)
        except ValueError:
            messagebox.showerror("Loi", "So tien phai la so nguyen (vi du: 50000).")
            return None
        if so_tien <= 0:
            messagebox.showerror("Loi", "So tien phai lon hon 0.")
            return None
        try:
            datetime.strptime(ngay, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Loi", "Ngay phai dung dinh dang YYYY-MM-DD.")
            return None
        return noi_dung, so_tien, danh_muc, ngay

    def hien_thi_danh_sach(self, danh_sach):
        for dong in self.bang.get_children():
            self.bang.delete(dong)
        for id_ct, noi_dung, so_tien, danh_muc, ngay in danh_sach:
            self.bang.insert("", tk.END, values=(id_ct, noi_dung, f"{so_tien:,}", danh_muc, ngay))
        self.nhan_tong.config(text=f"Tong chi tieu: {db.tong_chi_tieu():,} VND")

    def tai_lai_danh_sach(self):
        self.hien_thi_danh_sach(db.lay_toan_bo_chi_tieu())

    # ---------- Xu ly su kien ----------
    def khi_chon_dong(self, _su_kien=None):
        chon = self.bang.selection()
        if not chon:
            return
        id_ct, noi_dung, so_tien, danh_muc, ngay = self.bang.item(chon[0])["values"]
        self.id_dang_chon = int(id_ct)
        self.o_noi_dung.delete(0, tk.END)
        self.o_noi_dung.insert(0, noi_dung)
        self.o_so_tien.delete(0, tk.END)
        self.o_so_tien.insert(0, str(so_tien).replace(",", ""))
        self.chon_danh_muc.set(danh_muc)
        self.o_ngay.delete(0, tk.END)
        self.o_ngay.insert(0, ngay)

    def xu_ly_them(self):
        du_lieu = self.doc_va_kiem_tra_du_lieu()
        if du_lieu is None:
            return
        db.them_chi_tieu(*du_lieu)
        self.xoa_o_nhap()
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", "Da them khoan chi tieu.")

    def xu_ly_cap_nhat(self):
        if self.id_dang_chon is None:
            messagebox.showerror("Loi", "Vui long chon mot dong trong bang de cap nhat.")
            return
        du_lieu = self.doc_va_kiem_tra_du_lieu()
        if du_lieu is None:
            return
        db.sua_chi_tieu(self.id_dang_chon, *du_lieu)
        self.xoa_o_nhap()
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", "Da cap nhat khoan chi tieu.")

    def xu_ly_xoa(self):
        if self.id_dang_chon is None:
            messagebox.showerror("Loi", "Vui long chon mot dong trong bang de xoa.")
            return
        if not messagebox.askyesno("Xac nhan", "Ban co chac muon xoa khoan chi tieu nay?"):
            return
        db.xoa_chi_tieu(self.id_dang_chon)
        self.xoa_o_nhap()
        self.tai_lai_danh_sach()

    def xu_ly_tim_kiem(self):
        tu_khoa = self.o_tim_kiem.get().strip()
        if tu_khoa == "":
            self.tai_lai_danh_sach()
            return
        self.hien_thi_danh_sach(db.tim_kiem_chi_tieu(tu_khoa))

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_theo_danh_muc()
        if not du_lieu:
            messagebox.showinfo("Thong bao", "Chua co du lieu chi tieu de thong ke.")
            return
        cac_danh_muc = [dong[0] for dong in du_lieu]
        tong_tien = [dong[1] for dong in du_lieu]
        plt.figure(figsize=(7, 4))
        plt.bar(cac_danh_muc, tong_tien, color="seagreen")
        plt.title("Tong chi tieu theo danh muc")
        plt.xlabel("Danh muc")
        plt.ylabel("So tien (VND)")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    ung_dung = UngDungChiTieu()
    ung_dung.mainloop()