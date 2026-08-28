""" Độ ưu tiên toán tử:
Dự đoán kết quả trước khi chạy, sau đó kiểm tra lại bằng Python: """

print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)
#Ket qua du doan :  print(2 + 3 * 4 ** 2) : Độ ưu tiên sẽ là **, *, +, => 2 + 3 * 16 = 2 + 48 = 50
#Ket qua du doan :  print((2 + 3) * 4 ** 2) : Độ ưu tiên sẽ là (), **, *,  => (5) * 16 = 80
#Ket qua du doan :  print(10 > 5 and 3 < 1 or not False) : Độ ưu tiên sẽ là and, or, not => (True and False) or True = False or True = True