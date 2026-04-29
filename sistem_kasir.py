class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.__harga = harga
        self.__stok = stok
        
    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, value):
        if value < 0:
            raise ValueError("harga tidak boleh negatif")
        self.__harga = value

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, value):
        if value < 0:
            raise ValueError("stok tidak boleh negatif")
        self.__stok = value
 
    def kurangi_stok(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            return True
        return False
 
    def cek_stok(self):
        return self.stok
 
 
class Keranjang:
    def __init__(self, member=False):
        self.daftar_barang = []
        self.member = member
 
    def tambah_produk(self, produk_baru, jumlah):
        if produk_baru.kurangi_stok(jumlah):
            self.daftar_barang.append({
                "produk": produk_baru,
                "jumlah": jumlah
            })
            print(f"Berhasil menambah: {produk_baru.nama} ({jumlah})")
        else:
            print(f"Stok {produk_baru.nama} tidak cukup!")
 
    def hapus_produk(self, nama_produk):
        for barang in self.daftar_barang:
            if barang["produk"].nama == nama_produk:
                barang["produk"].stok += barang["jumlah"]
                self.daftar_barang.remove(barang)
                print(f"{nama_produk} dihapus dari keranjang")
                return
        print("Produk tidak ditemukan")
 
    def hitung_total(self):
        total = 0
        for barang in self.daftar_barang:
            total += barang["produk"].harga * barang["jumlah"]
        return total
 
    def cetak_struk(self):
        print("\n=== Struk Belanja ===")
        for barang in self.daftar_barang:
            p = barang["produk"]
            j = barang["jumlah"]
            print(f"- {p.nama} x{j} : Rp{p.harga * j:,.0f}")
 
        total = self.hitung_total()
        print(f"Subtotal : Rp{total:,.0f}")
 
        if self.member:
            diskon_member = total * 0.05
            print(f"Diskon Member (5%) : -Rp{diskon_member:,.0f}")
            total -= diskon_member
 
        ppn = total * 0.11
        print(f"PPN (11%) : Rp{ppn:,.0f}")
        total += ppn
 
        total = round(total, 2)
        print(f"Total Akhir : Rp{total:,.0f}")
        return total
 
    def bayar(self, uang_diterima):
        total = self.cetak_struk()
 
        print(f"\nUang Diterima : Rp{uang_diterima:,.0f}")
 
        if uang_diterima >= total:
            kembalian = uang_diterima - total
            print(f"Kembalian : Rp{kembalian:,.0f}")
        else:
            print("Uang tidak cukup!")
 