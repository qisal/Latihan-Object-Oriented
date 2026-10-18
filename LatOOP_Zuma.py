class KatakZuma:
    def __init__(self, warna_awal, skor, is_active):
        self.warna_peluru = warna_awal  
        self.skor = 0
        self.is_active = True

    def tembak(self):
        self.skor += 50
        print("Your kodok menembak!")

    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru
        print("Your kodok mengganti warna bola nya!")

    def kondisi(self, status):
        if self.is_active == True:
            status = "Aktif"
        else:
            status = "Tidak Aktif"

        print(f"Your Kodok : {status}, Warna Peluru : {self.warna_peluru}, Skor : {self.skor}")

# TES PROGRAM

katak = KatakZuma("Hijau", 0, True)

print("Kondisi awal: ")
katak.warna_awal = "Putih"
katak.kondisi(None)
print()

katak.tembak()
katak.ganti_warna("Biru")
print()

print("Kondisi sekarang: ")
katak.kondisi(None)