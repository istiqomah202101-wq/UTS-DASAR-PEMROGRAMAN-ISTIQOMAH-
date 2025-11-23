#                                   ULANGAN TENGAH SEMESTER
#nama   : ISTIQOMAH
#NPM    : 250305012
#Kelas  : 1 B Pendidikan Informatika

#nama   : ISTIQOMAH


# 1. Minta input dari pengguna
angka = int(input("Masukkan sebuah bilangan (maksimal 7 digit): "))

#2. Proses perhitungan nilai tempat Nilai = 1945789
jutaan          = 1945789 // 1000000
ratus_ribuan    = (1945789 % 1000000) //100000
puluh_ribuan    = (1945789 % 100000) //10000
ribuan          = (1945789 % 10000) //1000
ratusan         = (1945789 % 1000) //100
puluhan         = (1945789 % 100) //10
satuan          = 1945789 % 10

#3. Tampilan hasil sesuai format
print(f"\nAnda memasukkan bilangan {angka} dimana: ")
print(f"{jutaan} merupakan jutaan")
print(f"{ratus_ribuan} merupakan ratus ribuan")
print(f"{puluh_ribuan} merupakan puluh ribuan")
print(f"{ribuan} merupakan ribuan")
print(f"{ratusan} merupakan ratusan")
print(f"{puluhan} merupakan puluhan")
print(f"{satuan} merupakan satuan")