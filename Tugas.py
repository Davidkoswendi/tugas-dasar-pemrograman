print("=== PERHITUNGAN BUDGET SEMINAR NASIONAL ===")

# Input data 
jumlahPeserta = int(input("Masukkan jumlah peserta seminar: "))
biayaSewaTempat = float(input("Masukkan biaya sewa tempat: "))
biayaDokumentasi = float(input("Masukkan biaya dokumentasi: "))

# a. Perhitungan Biaya Konsumsi
hargaSatuPaketKonsumsi = 35000
tambahanKonsumsi = 0.10
jumlahKonsumsi = round(jumlahPeserta + (jumlahPeserta * tambahanKonsumsi))
totalBiayaKonsumsi = jumlahKonsumsi * hargaSatuPaketKonsumsi

print("\n=== Perhitungan Biaya Konsumsi ===")
print(f"Jumlah Konsumsi Yang Disediakan : {jumlahKonsumsi}")
print(f"Total Biaya Konsumsi : Rp{totalBiayaKonsumsi:,}".replace(",", "."))

# b. Perhitungan Kebutuhan Cetak Sertifikat
satuRim = 500
hargaRim = 65000
sertifikatTambahan = 0.05

jumlahSertifikat = round(jumlahPeserta + (jumlahPeserta * sertifikatTambahan))
jumlahLembarKertas = jumlahSertifikat
perkiraanJumlahRim = (jumlahLembarKertas + satuRim - 1) // satuRim
totalBiayaKertas = perkiraanJumlahRim * hargaRim

print("\n=== Perhitungan Kebutuhan Cetak Sertifikat ===")
print(f"Jumlah Sertifikat Yang Perlu Dicetak : {jumlahSertifikat}")
print(f"Jumlah Lembar Kertas Yang Dibutuhkan : {jumlahLembarKertas}")
print(f"Perkiraan Jumlah Rim Kertas Yang Diperlukan : {perkiraanJumlahRim}")
print(f"Total Biaya Kertas : Rp{totalBiayaKertas:,}".replace(",", "."))

# c. Perhitungan Biaya Pendaftaran Peserta
danaCadanganPersen = 0.10

totalBiayaPenyelenggaraan = round(totalBiayaKonsumsi + totalBiayaKertas + biayaSewaTempat + biayaDokumentasi)
besarDanaCadangan = round(totalBiayaPenyelenggaraan * danaCadanganPersen)
totalDanaYangHarusDikumpulkan = totalBiayaPenyelenggaraan + besarDanaCadangan
biayaPendaftaranPerPeserta = (totalDanaYangHarusDikumpulkan + jumlahPeserta - 1) // jumlahPeserta

print("\n=== Perhitungan Biaya Pendaftaran Peserta ===")
print(f"Total Biaya Penyelenggaraan : Rp{totalBiayaPenyelenggaraan:,}".replace(",", "."))
print(f"Besar Dana Cadangan : Rp{besarDanaCadangan:,}".replace(",", "."))
print(f"Total Dana Yang Harus Dikumpulkan : Rp{totalDanaYangHarusDikumpulkan:,}".replace(",", "."))
print(f"Biaya Pendaftaran Yang Harus Dibayar Per Peserta : Rp{biayaPendaftaranPerPeserta:,}".replace(",", "."))