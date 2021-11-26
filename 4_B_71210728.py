kalimat = input("Masukkan kalimat untuk dihitung : ")

def hitung(kalimat):
    hitung_kalimat = len(kalimat)
    hasil_akhir = hitung_kalimat * 2 / 3
    return hasil_akhir

print(int(hitung(kalimat)))