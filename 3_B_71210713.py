Kalimat_awal= str(input("Masukkan kalimat awal: "))
sisipkan_kata= str(input("Masukkan kata untuk disisipkan: "))
index= int(input("Masukkan index: "))


def hasil(kalimat_awal,sisipkan_kata,index):
    penyisipan= kalimat_awal[:index] + sisipkan_kata + kalimat_awal[index:]
    print(penyisipan)

hasil(Kalimat_awal,sisipkan_kata,index)