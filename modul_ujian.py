import os
import modul_utama
import androidhelper
droid = androidhelper.Android()


def ujian():
    file_soal = droid.dialogGetInput("Mengambil File Soal", "Nama File").result
    direct = "/storage/emulated/0/qpython/UTS/"
    file = open(os.path.join(direct, file_soal+".txt"), "r")
    lis = []
    ok = 0
    for num, line in enumerate(file, 1):
        for i in range(100):
            if str(i+1)+'.' in line:
                ok += 1
                index = line.index(str(line))
                index = str(index)
                index = index.replace('0', str(ok+1))
                lis = [index]
    i = 1
    poin = 0
    no = int(lis[0])
    direct  = "/storage/emulated/0/qpython/UTS/"
    file = open(os.path.join(direct, file_soal+".txt"), "r")
    while i < no:
        i += 1
        text = file.readline()
        hashtag = text
        text = file.readline()
        soal = text
        text = file.readline()
        a = text
        text = file.readline()
        b = text
        text = file.readline()
        c = text
        text = file.readline()
        d = text
        text = file.readline()
        e = text
        text = file.readline()
        star = text
        text = file.readline()
        kunci_jwb = text.strip().split(" ")[1]
        text = file.readline()
        hashtag2 = text
        droid.dialogCreateAlert(soal)
        droid.dialogSetItems([a, b, c, d, e])
        droid.dialogShow()
        jawaban = droid.dialogGetResponse().result["item"]

        if jawaban == 0:
            cek("a", kunci_jwb)
        elif jawaban == 1:
            cek("b", kunci_jwb)
        elif jawaban == 2:
            cek("c", kunci_jwb)
        elif jawaban == 3:
            cek("d", kunci_jwb)
        elif jawaban == 4:
            cek("e", kunci_jwb)


def cek(jawaban, kunci_jwb):
    hasil = ""
    if jawaban == kunci_jwb:
        hasil = "Jawaban Anda Benar!"
    else:
        hasil = "Salah! Anda Menjawab (" + jawaban + ")\nyang benar (" + kunci_jwb + ")"
    droid.dialogCrateAlert("Periksa Jawaban")
    droid.dialogSetItems([hasil])
    droid.dialogSetPositiveButtonText("OK")
    droid.dialogShow()