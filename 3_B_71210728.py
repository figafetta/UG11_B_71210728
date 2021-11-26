kal_awal = str(input("Masukkan kalimat awal: "))
kata_disisipkan = str(input("Masukkan kata untuk disisipkan: "))
index = int(input("Masukkan Index: "))

def hasil(kal_awal,kata_disisipan,index):
    penyisipan = kal_awal[:index] + kata_disisipan + kal_awal[index:]
    print(penyisipan)

hasil(kal_awal,kata_disisipkan,index)