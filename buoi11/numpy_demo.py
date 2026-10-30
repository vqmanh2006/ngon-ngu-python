import numpy as np
diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_array = np.array(diem_list)
print(type(diem_list), type(diem_array))
diem_cong_them = diem_array + 0.5
print(diem_cong_them)
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print(diem_cong_them_list)
print("Trung binh : ", np.mean(diem_array))
print("Lon nhat :", np.max(diem_array))
print("Nho nhat :", np.min(diem_array))
print("Do lech chuan :", round(np.std(diem_array), 2))
matran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma tran :\n",matran )
print("Kich thuoc (shape) :", matran.shape)
print("Ma tran nhan 2:\n", matran *2)