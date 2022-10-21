import androidhelper
import modul_utama
droid = androidhelper.Android()

def tambahfile():
    file_soal = droid.dialogGetInput("Buat File Baru", "Nama File").result
    file = file_soal
    file = "/storage/emulated/0/qpython/UTS/" + file + ".txt"
    file_objek = open(file, "w+")
    modul_utama.utama()