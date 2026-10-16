import tkinter as tk
from tkinter import messagebox
def them_ky_tu(ky_tu):
    man_hinh.insert(tk.END, ky_tu)

def xoa_man_hinh():
    man_hinh.delete(0, tk.END)

def xoa_ky_tu_cuoi():
    bieu_thuc = man_hinh.get()
    man_hinh.delete(0, tk.END)
    man_hinh.insert(0, bieu_thuc[:-1])

def tinh_ket_qua():
    bieu_thuc = man_hinh.get()
    if bieu_thuc == "":
        return
    try:
        ky_tu_hop_le = "0123456789+-*/(). "
        if any(ky_tu not in ky_tu_hop_le for ky_tu in bieu_thuc):
            raise ValueError
        ket_qua = eval(bieu_thuc, {"__builtins__": None}, {})
        man_hinh.delete(0, tk.END)
        man_hinh.insert(0, str(ket_qua))
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho 0.")
    except (ValueError, SyntaxError, TypeError):
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ.")

def xu_ly_phim(event):
    phim = event.keysym

    if phim == "Return":
        tinh_ket_qua()
        return "break"

    if phim == "Escape":
        xoa_man_hinh()
        return "break"

cua_so = tk.Tk()
cua_so.title("Máy tính bỏ túi")
cua_so.geometry("320x420")
cua_so.resizable(False, False)

man_hinh = tk.Entry(
    cua_so,
    font=("Arial", 24),
    justify="right",
    bd=8,
    relief=tk.GROOVE
)
man_hinh.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=15,
    ipady=10,
    sticky="nsew"
)

cac_nut = [
    ("C", 1, 0, xoa_man_hinh),
    ("⌫", 1, 1, xoa_ky_tu_cuoi),
    ("(", 1, 2, lambda: them_ky_tu("(")),
    (")", 1, 3, lambda: them_ky_tu(")")),
    ("7", 2, 0, lambda: them_ky_tu("7")),
    ("8", 2, 1, lambda: them_ky_tu("8")),
    ("9", 2, 2, lambda: them_ky_tu("9")),
    ("/", 2, 3, lambda: them_ky_tu("/")),
    ("4", 3, 0, lambda: them_ky_tu("4")),
    ("5", 3, 1, lambda: them_ky_tu("5")),
    ("6", 3, 2, lambda: them_ky_tu("6")),
    ("*", 3, 3, lambda: them_ky_tu("*")),
    ("1", 4, 0, lambda: them_ky_tu("1")),
    ("2", 4, 1, lambda: them_ky_tu("2")),
    ("3", 4, 2, lambda: them_ky_tu("3")),
    ("-", 4, 3, lambda: them_ky_tu("-")),
    ("0", 5, 0, lambda: them_ky_tu("0")),
    (".", 5, 1, lambda: them_ky_tu(".")),
    ("=", 5, 2, tinh_ket_qua),
    ("+", 5, 3, lambda: them_ky_tu("+")),
]

for noi_dung, hang, cot, lenh in cac_nut:
    tk.Button(
        cua_so,
        text=noi_dung,
        command=lenh,
        font=("Arial", 16),
        width=5,
        height=2
    ).grid(
        row=hang,
        column=cot,
        padx=5,
        pady=5,
        sticky="nsew"
    )
for cot in range(4):
    cua_so.grid_columnconfigure(cot, weight=1)
for hang in range(1, 6):
    cua_so.grid_rowconfigure(hang, weight=1)
cua_so.bind("<Key>", xu_ly_phim)
man_hinh.focus()
cua_so.mainloop()