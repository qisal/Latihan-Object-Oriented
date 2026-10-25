class Kendaraan:
    def __init__(self, merk, model, top_speed):
        self.merk = merk
        self.model = model
        self.top_speed = top_speed
        self.speed = 0
        self.is_running = False
        self.status = True #Artinya kendaraan dalam kondisi baik-baik saja
        

    def nyalakan_mesin(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.merk} {self.model} dinyalakan.")
        else:
            print(f"{self.merk} {self.model} sudah menyala.")

    def matikan_mesin(self):
        if self.is_running:
            self.is_running = False
            self.speed = 0
            print(f"{self.merk} {self.model} dimatikan.")
        else:
            print(f"{self.merk} {self.model} sudah mati.")

    def gas(self, amount):
        self.speed += amount
        if self.speed > self.top_speed:
            self.speed = self.top_speed
        print(f"{self.merk} {self.model} melaju dengan kecepatan {self.speed} km/jam.")

    def rem(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        print(f"{self.merk} {self.model} mengerem. Kecepatan sekarang {self.speed} km/jam.")

    def crash(self):
        self.speed = 0
        self.is_running = False
        self.status = False
        print(f"{self.merk} {self.model} mengalami kecelakaan! Kendaraan rusak, Segera perbaiki!")

    def repair(self):
        if self.status == False:
            self.status = True
            print(f"{self.merk} {self.model} telah diperbaiki!")
        else:
            print(f"{self.merk} {self.model} tidak perlu diperbaiki.")


#Pengujian Objek
mobil1 = Kendaraan("McLaren", "720s", 300)
mobil2 = Kendaraan("Lamborghini", "Huracan", 325)


mobil1.nyalakan_mesin()
mobil2.nyalakan_mesin()
print()

mobil1.gas(190)
mobil2.gas(250)
print()

mobil1.rem(50)
print()

mobil2.crash()
print()

mobil2.repair()
mobil1.repair()



   