def generatesoal(tipe,soal):
    bil1=random.randint(1,20)
    bil2=random.randint(1,20)
    bil3=random.randint(1,20)
    bil4=random.randint(1,20)
    perbandingan = ['<','>','==']
    random_perbandingan=random.choice(perbandingan)
    a = soal
    soal=True
    if tipe=="penjumlahan":
        soal=bil1 + bil2, random_perbandingan, bil3 + bil4
        if random_perbandingan=='<':
            soal=bil1 + bil2 < bil3 + bil4
        elif random_perbandingan=='>':
            soal=bil1 + bil2 > bil3 + bil4
        else:
            soal=bil1 + bil2 == bil3 + bil4
        print('(benar/salah) jika ', bil1, '+', bil2, random_perbandingan, bil3, '+', bil4)
    elif tipe=="pengurangan":
        soal=bil1 + bil2, random_perbandingan, bil3 + bil4
        if random_perbandingan=='<':
            soal=bil1 - bil2 < bil3 - bil4
        elif random_perbandingan=='>':
            soal=bil1 - bil2 > bil3 - bil4
        else:
            soal=bil1 - bil2 == bil3 - bil4
        print('(benar/salah) jika ', bil1, '-', bil2, random_perbandingan, bil3, '-', bil4)
def cekHasil(jawaban):
    if jawaban ==True:
        tipe=input("Masukkan tipe yang ingin anda coba: ")
        a =tipe.lower()
        soal=0
        print("Jawaban Anda Masih Salah !")
        
cekHasil(jawaban=True)