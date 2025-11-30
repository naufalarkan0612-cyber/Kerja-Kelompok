# 1. Database kurs (rate terkini per 1 USD, sumber: x-rates.com per 21 Oktober 2025)

rate = 0
kurs = {
    "dollar" : 1,     # USD
    "eur" : 0.859,    # Euro
    "gbp" : 0.746,    # British Pound
    "jpy" : 151,      # Japanese Yen
    "aud" : 1.53,     # Australian Dollar
    "cad" : 1.40,     # Canadian Dollar
    "chf" : 0.793,    # Swiss France
    "cny" : 7.11,     # Chinese Yuan
    "inr" : 87.9,     # Indian Rupee
    "brl" : 5.37,     # Brazilian Real
    "rub" : 80.8,     # Russian Ruble
    "zar" : 17.2,     # South African Rand
    "btc" : 0.000011, # Bitcoin
    "eth" : 0.00033   # Etherium
}

# 2. fungsi kurs konverter
def kurs_converter(amount, awal, tujuan):

    # 2.1. Validasi mata uang
    if awal not in kurs or tujuan not in kurs:
        raise ValueError("Maaf, sistem kami masih kentang, coba mata uang yang lain🙏.")
    
    # 2.2. Konversi dari mata uang asal ke USD
    amount_in_usd = amount / kurs[awal]
    
    # 2.3. Konversi dari USD ke mata uang tujuan
    converted_amount = amount_in_usd * kurs[tujuan]
    return converted_amount

# 3. Fungsi untuk memberikan feedback berdasarkan rating
def rate_feedback(rate):
    
    if rate >=5:
        print("Terima kasih atas ratingnya! Kami senang Anda puas dengan program ini \\\\ >_< ///.")
    elif rate == 4:
        print("Terima kasih atas ratingnya! Kami akan berusaha lebih baik lagi 😊.")
    elif rate == 3:
        print("Terima kasih atas masukannya! Kami akan berusaha memperbaiki program ini 🙂.")
    elif rate == 2:
        print("Terima kasih atas masukannya! Kami akan berusaha memperbaiki program ini 😕.")
    elif rate == 1:
        print("Terima kasih atas masukannya! Kami akan berusaha memperbaiki program ini 😞.")        
    else:
        print("Terima kasih atas masukannya! Kami akan berusaha memperbaiki program ini 😓🙏.")

# 4. Code utama

# 4.1. Pembukaan program
print("Selamat datang di program konversi mata uang Homemade milik kelompok kami!")
print("\nMata uang yang tersedia:\n")

# 4.2. Menampilkan daftar mata uang yang tersedia berdasarkan database kurs
for mata_uang in kurs.keys():
    print(f"- {mata_uang}", end=" ")
print("\n")
print("=-" * 44, "\n")

# 5.menangani error input
try:
    # 2.1..Input dari user
    jumlah = float(input("Masukkan jumlah uang yang akan dikonversi: "))
    awal = input("\nMasukkan kode mata uang asal (misal: dollar, eur, jpy): ").lower()
    tujuan = input("\nMasukkan kode mata uang tujuan (misal: dollar, eur, jpy): ").lower()

    # 2.2. memanggil fungsi kurs konverter
    hasil = kurs_converter(jumlah, awal, tujuan)
    print(f"{jumlah} {awal} setara dengan {hasil:.2} {tujuan}.")

    # 3.1.meminta feedback rating dari user
    rate = int(input("\nJika anda puas dengan program ini, berikan rating dari 1-5: "))
    rate_feedback(rate)
    
# 5.1.Menampilkan pesan error jika terjadi kesalahan    
except ValueError as x:
    print(f"Error: {x}")