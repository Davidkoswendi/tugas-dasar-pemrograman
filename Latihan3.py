print("=== PERHITUNGAN PERJALANAN ===")

jarakTempuh = 110        
konsumsiBbm = 122          
hargaPerLiter = 13000  

# 1. Menghitung jumlah liter bensin yang dibutuhkan
literDibutuhkan = round(jarakTempuh / konsumsiBbm)

# 2. Menghitung total biaya bensin
totalBiaya = literDibutuhkan * hargaPerLiter

print(f"Jarak tempuh : {jarakTempuh} km")
print(f"Konsumsi BBM : {konsumsiBbm} km/liter")
print(f"Harga bensin : Rp{hargaPerLiter:,}/liter".replace(",", "."))
print("==============================")
print(f"1. Bensin dibutuhkan : {literDibutuhkan} liter")
print(f"2. Total biaya       : Rp{totalBiaya:,}".replace(",", "."))

