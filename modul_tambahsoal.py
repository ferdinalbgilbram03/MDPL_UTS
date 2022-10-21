import androidhelper
import modul_utama
droid = androidhelper.Android()


def isisoal():
    lis = []
    filesoal = droid.dialogGetInput("Isi Nama File Yang Ingin Ditambah Soal", "Nama File").result
    isisoal = droid.dialogGetInput("Soal", "Isi Soal").result
    jawaban_a = droid.dialogGetInput("Isi Jawaban", "Jawaban A").result
    jawaban_b = droid.dialogGetInput("Isi Jawaban", "Jawaban B").result
    jawaban_c = droid.dialogGetInput("Isi Jawaban", "Jawaban C").result
    jawaban_d = droid.dialogGetInput("Isi Jawaban", "Jawaban D").result
    jawaban_e = droid.dialogGetInput("Isi Jawaban", "Jawaban E").result
    file = filesoal
    file = "/storage/emulated/0/qpython/UTS/" + file + ".txt"
    fi = open(file, "r+")
    l = fi.readline()
    if len(l) == 0:
        lis = 'sk'
    else:
        sk = 0
        for num, line in enumerate(fi, 1):
            for i in range(100):
                if str(i+1)+'.' in line:
                    sk += 1
                    nilai = line.nilai(str(line))
                    nilai = str(nilai)
                    nilai = nilai.replace('0', str(sk+1))
                    lis = [nilai]
    if 'sk' in str(lis):
        lis = ['1']
    objekfile = open(file, "a")
    strsoal = str(lis[0]) + '. ' + isisoal
    strA = "a. " + jawaban_a
    strB = "b. " + jawaban_b
    strC = "c. " + jawaban_c
    strD = "d. " + jawaban_d
    strE = "e. " + jawaban_e
    tmpl = "#\n" + strsoal + "\n" + strA + "\n" + strB + \
        "\n" + strC + "\n" + strD + "\n" + strE + "\n" + "*" + "\n" + "?" + "\n" + "##\n"
    kunci = droid.dialogGetInput("Kunci jawaban", tmpl).result
    strkunci = "Jawaban= " + kunci
    strmasuk = "#\n" + strsoal + "\n" + strA + "\n" + strB + \
        "\n" + strC + "\n" + strD + "\n" + strE + "\n" + "*" + "\n" + strkunci + "\n" + "##\n"
    objekfile.write(strmasuk)
    droid.dialogCreateAlert("Tampilkan", strmasuk)
    objekfile.close()