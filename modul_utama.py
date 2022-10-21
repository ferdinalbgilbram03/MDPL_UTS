import androidhelper
import modul_tambahsoal
import modul_tambahfile
import modul_lihatsoal
import modul_ujian
droid = androidhelper.Android()


def utama():
    droid.dialogCreateAlert("Pilih Opsi")
    droid.dialogSetItems(
        ["Ujian", "Lihat Soal", "Tambah File", "Tambah Soal Baru", "Keluar"])
    droid.dialogShow()
    ops = droid.dialogGetResponse().result
    if ops['item'] == 0:
        modul_ujian.ujian()
    elif ops['item'] == 1:
        modul_lihatsoal.tampilsoal()
    elif ops['item'] == 2:
        modul_tambahfile.tambahfile()
    elif ops['item'] == 3:
        modul_tambahsoal.isisoal()
    else:
        droid.dialogCreateAlert("Anda Keluar")
        droid.dialogShow()