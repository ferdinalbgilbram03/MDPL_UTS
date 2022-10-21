import androidhelper
import modul_utama
droid = androidhelper.Android()


def tampilsoal():
    file_soal = droid.dialogGetInput("Menampilkan Soal", "Masukan file").result
    tampil_soal = droid.dialogGetResponse().result
    if tampil_soal == ["none"]:
        exit()
    else:
        file = file_soal
        file = "/storage/emulated/0/qpython/UTS/" + file + ".txt"
        objekfile = open(file, "r")
        droid.dialogCreateAlert("Menampilkan", objekfile.read())
        droid.dialogSetPositiveButtonText('Kembali')
        droid.dialogSetNegativeButtonText('Keluar')
        droid.dialogShow()
        opsi = droid.dialogGetResponse().result
        opsi = opsi['which']
        if opsi == "positive":
            modul_utama.utama()
        else:
            exit()