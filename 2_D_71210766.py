a = input("Masukkan sebuah kata/kalimat : ")
b = input("Masukkan karakter yang ingin disisipkan : ")

def huruf () :
    huruf = a.upper()
    print(b.join(list(huruf)))
def kalimat () : 
    huruf = a.title()
    print(b.join(huruf.split()))

huruf ()
kalimat ()