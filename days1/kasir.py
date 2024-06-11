data_product = {
   1:"gb kopi arabika muria",
   2:"gb kopi robusta muria fine",
   3:"gb kopi robusta muria grade 1",
   4:"gb kopi robusta muria asalan",
   5:"gb kopi robusata luwak",
   6:"gb kopi arabika luwak"
}
daftar_harga ={
    1: 110000,
    2: 75000,
    3: 58000,
    4: 48500,
    5: 500000,
    6: 600000
}

dict_trx = {}
daftar_metode_pembayaran = {
    1:"transfer",
    2:"virtual account",
    3:"cash on delivery"
}
print("===============List product===============")
for i in data_product:
    print("Id product : ", i, "\t nama product : ", 
          data_product[i], "\t \t harga product : ", daftar_harga[i])
pilih_id = int(input("pilihan id product : "))
if pilih_id in data_product :
    pilih_beli = input("ingin beli ? (Y/N) : ")
    if pilih_beli =="y" or pilih_beli=="Y":
        nama_penerima    = input("nama penerima : ")
        alamat_penerima  = input("alamt penerima : ")
        telepon          = input("No Hp : ")
        kurir_pengiriman  = input("kurir pengiriman : ")
        dict_trx = {
            "nama penerima":nama_penerima,
            "alamat penerima":alamat_penerima,
            "no hp":telepon,
            "kurir pengiriman":kurir_pengiriman,
            "product id":data_product
        }
    else:
        pass
    if len (dict_trx) > 0 :
        print("=============== Metode pembayaran ===============")
    for i in daftar_metode_pembayaran:
        print("id : ",i, "\t metode pembayaran : ",daftar_metode_pembayaran[i])
    pilih_metode = int(input("pilih id metode pembayaran : "))
    if pilih_metode in daftar_metode_pembayaran :
        print("nama penerima : ", dict_trx["nama penerima"])
        print("alamat penerima : ", dict_trx["alamat penerima"])
        print("no hp : ", dict_trx["no hp"]) 
        print("kurir pengiriman : ", dict_trx["kurir pengiriman"])
        print("product : ", data_product[pilih_id])
        print("harga : ", daftar_harga[pilih_id])
        print("metode pembayaran : ", daftar_metode_pembayaran[pilih_metode])
        konfirmasi = input("apakah anda yakin ingin melakukan pembayaran? (Y/N) : ")
        if konfirmasi == "y" or konfirmasi == "Y":
            print("anda sudah berhasil melakukan pembayaran")
        else:
            pass
    else:
        print("id metode pembayaran tidak tersedia")
else:
    print("id product tidak tersedia")