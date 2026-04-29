from sistem_kasir import Produk, Keranjang  

p1 = Produk("Kopi Kenangan", -25000, -00)
p2 = Produk("Susu UHT", 18000, 10)
p3 = Produk("Keyboard Gaming", 250000, 5)

keranjang_saya = Keranjang(member=False)

keranjang_saya.tambah_produk(p1, 1)
keranjang_saya.tambah_produk(p2, 2)
keranjang_saya.tambah_produk(p3, 3)

keranjang_saya.bayar(900000)