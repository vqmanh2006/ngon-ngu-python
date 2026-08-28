cau = "Lap trinh Python rat thu vi"
print(cau[0]) # ky tu dau tien
print(cau[-1]) # ky tu cuoi cung
print(cau[4:10]) # cat tu vi tri 4 den truoc vi tri 10
print(cau[:8]) # tu dau den vi tri 8
print(cau[11:]) # tu vi tri 11 den het
print(cau[::-1]) # dao nguoc chuoi
print("Kiem tra palindrome: ", cau == cau[::-1]) # kiem tra palindrome

'''Yêu cầu: dùng cau[::-1] để in ra chuỗi đảo ngược, sau đó kiểm tra xem cau có phải là palindrome
không bằng biểu thức so sánh: cau == cau[::-1].'''