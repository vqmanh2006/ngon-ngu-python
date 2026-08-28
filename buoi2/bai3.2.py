a = -7
b = 2.6789
c, d = 17, 5

print("Tri tuyet doi : ", abs(a)) # gia tri tuyet doi
print("Lam tron : ", round(b)) # lam tron
print("Lam tron 2 chu so thap phan : ", round(b, 2)) # lam tron 2 chu so thap phan
print("C mu 2 : ", pow(c, 2)) # c mu 2
print("Thuong va du : ", divmod(c, d)) # tra ve (thuong, du) dang tuple

# Yêu cầu: so sánh pow(c, 2) với c ** 2 (toán tử đã học ở Buổi 1) - hai cách này có luôn cho kết quả giống nhau không? Tại sao?
''' Ca hai cach deu cho ket qua giong nhau, vi pow(c, 2) va c  2 deu thuc hien phep luy thua, trong do c duoc nang len mu 2.
pow() la mot ham tich hop cua Python, trong khi  la toan tu luy thua. Trong hau het cac truong hop, chung se cho cung mot ket qua,
nhung pow() co the cung cap them cac tuy chon nhu tinh modulo khi can thiet.'''