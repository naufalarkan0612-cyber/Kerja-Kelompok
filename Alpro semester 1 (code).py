# Database kurs (rate terkini per 1 USD, sumber: x-rates.com per 21 Oktober 2025)

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
}

def kurs_converter(amount, awal, tujuan):
    if awal not in kurs or tujuan not in kurs:
        raise ValueError("Maaf, sistem kami masih kentang, coba mata uang yang lain.")
    
    # Konversi dari mata uang asal ke USD
    amount_in_usd = amount / kurs[awal]
    
    # Konversi dari USD ke mata uang tujuan
    converted_amount = amount_in_usd * kurs[tujuan]
    return converted_amount

# memanggil fungsi kurs konverter
try:
    jumlah = float(input("Masukkan jumlah uang yang akan dikonversi: "))
    awal = input("Masukkan kode mata uang asal (misal: dollar, eur, jpy): ").lower()
    tujuan = input("Masukkan kode mata uang tujuan (misal: dollar, eur, jpy): ").lower()
    
    hasil = kurs_converter(jumlah, awal, tujuan)
    print(f"{jumlah} {awal} setara dengan {hasil:.2 {tujuan}.")
    
except ValueError as x:
    print(f"Error: {x}")