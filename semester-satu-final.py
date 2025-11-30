def kurs_converter(jumlah, asal, tujuan):    
    kurs = {
        "dollar" : 1,     # USD
        "eur" : 0.859,    # Euro
        "gbp" : 0.746,    # British Pound
        "jpy" : 151,      # Japanese Yen
        "aud" : 1.53,     # Australian Dollar
        "cad" : 1.40,     # Canadian Dollar
        "chf" : 0.793,    # Swiss Franc
        "cny" : 7.11,     # Chinese Yuan
        "inr" : 87.9,     # Indian Rupee
        "brl" : 5.37,     # Brazilian Real
        "rub" : 80.8,     # Russian Ruble
        "zar" : 17.2,     # South African Rand
        "btc" : 0.000011, # Bitcoin
        "eth" : 0.00033   # Etherium
    }
    # validasi apakah asal dan tujuan ada di kurs
    if asal not in kurs or tujuan not in kurs:
        # jika tidak raise error
        raise ValueError("Maaf, sistem kami masih kentang, coba mata uang yang lain.")
    
    # Konversi dari mata uang asal ke USD
    konversi_ke_dollar = jumlah / kurs[asal]
    # Konversi dari USD ke mata uang tujuan
    hasil_akhir = konversi_ke_dollar * kurs[tujuan]

    # selesai dan return
    return hasil_akhir

# START
try:
    # dapatkan masukan jumlah, asal dan tujuan
    jumlah = float(input("Masukkan jumlah uang yang akan dikonversi: "))
    asal = input("Masukkan kode mata uang asal (misal: dollar, eur, jpy): ").lower()
    tujuan = input("Masukkan kode mata uang tujuan (misal: dollar, eur, jpy): ").lower()
    
    # kalkulasikan hasilnya
    hasil = kurs_converter(jumlah, asal, tujuan)

    # Tampilkan kalimat akhir
    print(f"{jumlah} {asal} setara dengan {hasil:.2} {tujuan}.")
    
except ValueError as x:
    print(f"Error: {x}")
#END