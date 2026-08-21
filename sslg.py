""" Toán tử so sánh & logic:
Viết các biểu thức kiểm tra:
 -diem có đạt loại Khá (từ 6.5 đến dưới 8.0) hay không (kết hợp and).
 -tuoi có phải chưa đủ 18 hoặc trên 60 không (kết hợp or).
 -Phủ định lại điều kiện trên bằng not."""
 
diem = 6.5
tuoi = 20
if ( diem >= 6.5 and diem < 8.0):
    print("Điểm đạt loại Khá")
    
if ( tuoi < 18 or tuoi > 60):
    print("không")
    
if not ( diem >= 6.5 and diem < 8.0):
    print("Điểm không đạt loại Khá")