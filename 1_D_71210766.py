A = input("Masukkan string : ")

def cek_string (A) :
    if A.isdigit() :
        angka = int(A)
        if angka %2 == 0:
            angka = int(angka/2)
            print(angka)
        else :
            angka =int((angka+5)/2)
            print(angka)
    else : 
        A = A[::-1]
        print(A)

cek_string (A)