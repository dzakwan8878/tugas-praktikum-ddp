n = int(input("\nBanyaknya Data:    "))

print() #Membuat Baris Baru
data = []
jmlh = 0

for i in range(0, n):
    temp = int(input("Masukkan Data ke-%d:" % (i+1)))
    data.append(temp)
    jmlh += data[i]
    rata2 = jmlh / n

print("\n Rata-rata = %0.2f" % rata2)