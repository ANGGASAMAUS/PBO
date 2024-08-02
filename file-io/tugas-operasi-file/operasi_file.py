def baca_file(pantun):
    with open(pantun, "r") as pantun_txt:
        isi_pantun = pantun_txt.read()
        print(isi_pantun)

def tulis_file(pantun):

    baca_file("pantun.txt")

    tulis_pantun = input("Tambahkan Pantun: ")
    text = "\n {}".format(tulis_pantun)

    with open(pantun, "a") as file_pantun:
        file_pantun.write(text)

tulis_file("pantun.txt")

