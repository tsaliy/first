class Perpus():
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

    def display_info(self):
        print(f"Judul: {self.judul}")
        print(f"Pengarang: {self.pengarang}")
        print(f"Tahun Terbit: {self.tahun_terbit}")

    def update_info(self, judul=None, pengarang=None, tahun_terbit=None):   
        if judul is not None:
            self.judul = judul
        if pengarang is not None:
            self.pengarang = pengarang
        if tahun_terbit is not None:
            self.tahun_terbit = tahun_terbit            

