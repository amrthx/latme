# Buka File
file_baca = open("test.txt","r")

# Baca file
baca = file_baca.readlines()
# baca dengan perulangan
for teks in baca:
    print (teks)

# Tutup file
file_baca.close()
