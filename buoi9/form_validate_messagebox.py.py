import tkinter as tk
from tkinter import messagebox


def xu_ly_submit():
    ho_ten = entry_ho_ten.get().strip()
    tuoi_nhap = entry_tuoi.get().strip()
    email = entry_email.get().strip()

    if ho_ten == "":
        messagebox.showerror("Lỗi", "Họ tên không được để trống.")
        return

    try:
        tuoi = int(tuoi_nhap)
    except ValueError:
        messagebox.showerror("Lỗi", "Tuổi phải là một số nguyên.")
        return

    if tuoi <= 0:
        messagebox.showerror("Lỗi", "Tuổi phải lớn hơn 0.")
        return

    if "@" not in email:
        messagebox.showerror(
            "Lỗi",
            "Email không hợp lệ, email phải chứa ký tự @."
        )
        return

    messagebox.showinfo(
        "Thành công",
        f"Đã nhận thông tin: {ho_ten} - {tuoi} tuổi - {email}"
    )


cua_so = tk.Tk()
cua_so.title("Form có validate")
cua_so.geometry("380x220")

tk.Label(cua_so, text="Họ tên:").grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)

entry_ho_ten = tk.Entry(cua_so, width=25)
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10)

tk.Label(cua_so, text="Tuổi:").grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
)

entry_tuoi = tk.Entry(cua_so, width=25)
entry_tuoi.grid(row=1, column=1, padx=10, pady=10)

tk.Label(cua_so, text="Email:").grid(
    row=2, column=0, padx=10, pady=10, sticky="w"
)

entry_email = tk.Entry(cua_so, width=25)
entry_email.grid(row=2, column=1, padx=10, pady=10)

tk.Button(
    cua_so,
    text="Submit",
    command=xu_ly_submit
).grid(row=3, column=0, columnspan=2, pady=15)

cua_so.mainloop()