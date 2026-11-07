print("=== PERHITUNGAN KEBUTUHAN BAHAN JUS ===")

buah = 600     
susu = 400    
gula = 4

gelas_dibutuhkan = 15
gelas_resep = 4

faktor = gelas_dibutuhkan / gelas_resep

buah_dibutuhkan = round(buah * faktor)
susu_dibutuhkan = round(susu * faktor)
gula_dibutuhkan = round(gula * faktor)

print(f"Kebutuhan Bahan untuk {gelas_dibutuhkan} Gelas Jus")
print(f"Buah : {buah_dibutuhkan} gram")
print(f"Susu : {susu_dibutuhkan} ml")
print(f"Gula : {gula_dibutuhkan} sendok makan")