# Jadi kita membuat program dan tampilan yang mudah dibaca oleh programmer lain
# data kurs dari x-rates.com per 21 Oktober 2025)
# data crypto dari tradingview.com per 27 November 2025)

kurs = {
    "usd" : 1,        # USD
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
    "btc" : 90826,    # Bitcoin
    "eth" : 2991.3    # Etherium
}

def kurs_converter():
    asal = input("🔸 Masukkan kode mata uang asal (misal: usd/eur/gbp)\t: ").lower()
    tujuan = input("🔸 Masukkan kode mata uang tujuan (misal: jpy/cny/zar)\t: ").lower()

    # validasi masukannya apakah asal dan tujuannya tersedia di database, jika tidak maka hentikan fungsi dan munculkan error
    if asal not in kurs or tujuan not in kurs:
        print("\n")
        print("⚠️  Uups… mata uang itu belum ada di sistem kami")
        print("Coba pilih yang lain dulu ya 🙂")
        raise ValueError(f"Kami belum bisa mengubah nilai dari {asal} ke {tujuan}")

    jumlah = float(input("🔸 Masukkan jumlah yang ingin kamu konversi\t\t: "))

    # Konversi dari mata uang asal ke USD
    amount_in_usd = jumlah / kurs[asal]
    # konversi ke mata uang tujuan
    hasil = amount_in_usd * kurs[tujuan]
    print("\n✅ Konversi selesai!")

    print(f"👉 {jumlah:.2f} {asal} setara dengan {hasil:.2f} {tujuan}")

# Memberi salam, panduan, dan memanggil fungsi kurs konverter
print("✨ Selamat datang di ruang konversi mata uang kami")
print("🌍 Tempat di mana setiap angka berubah jadi nilai baru\n")

print("Silakan pilih mata uang yang ingin kamu jelajahi 💱")
for mata_uang in kurs:
    print(mata_uang.upper(), end=" ")

print("\n")

# Mencoba kurs converter dan tangani ketika error
try:
    kurs_converter()
except ValueError as message:
    print("Error:", message)