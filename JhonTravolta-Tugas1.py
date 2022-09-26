from numpy import integer

 


x = 15000
y = 1.5
z = int(input("hours: "))
f = int(input("pemasukan: "))
total = 0
tabung = 0
if z <= 40:
    total = z * x
else:
    total = 600000 + (1.5 * 15000 * (z - 40))

 

print(f"gaji = {total}")
if total > f:
    print("bisa nabung")
    tabung = total - f
    print(f"tabungan : {tabung}")

 

elif total == f:
    print("tidak bisa menabung")

 

elif total < f:
    print("cari tambahan")