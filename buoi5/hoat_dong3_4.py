print("Hoat dong 3")
for i in range(1, 6):
    print(i)
print()
diem_so = [8.5, 7.0, 9.2, 6.5]
for diem in diem_so:
    print("Diem:", diem)
print()
toa_do = (3, 5)
for gia_tri in toa_do:
    print(gia_tri)
print()
diem_mon = {"Toan": 8.0, "Ly": 7.5}
for mon, diem in diem_mon.items():
    print(mon, "-", diem)
print()
ten = "Python"
for ky_tu in ten:
    print(ky_tu)
print()
#bang cuu chuong

print("Bang cuu chuong 5")
n = 5
for i in range(1, 11):
  print(f"{n} x {i} = {n * i}")
print()

print("Hoat dong 4.1")
giai_thua = 1
i = 1
while i <= n:
    giai_thua = giai_thua * i
    i += 1
print(f"{n}! = {giai_thua}")
print()

#hd 4.2
print("Hoat dong 4.2")
so = 4527
so_tam = so
tong_chu_so = 0
while so_tam > 0:
    chu_so = so_tam % 10
    tong_chu_so += chu_so
    so_tam = so_tam // 10
print(f"Tong cac chu so cua {so} la: {tong_chu_so}")