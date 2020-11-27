# Masukan NIM
nim = input("Masukkan NIM: ")
# jika nim terakhir angka 20
if nim[5:7] == '20' and len(nim) == 10:
    # bop angkatan 2020
    bop = 4000000
    # biaya angkatan 2020
    biaya = 200000
    tahun = 2020
    print('BOP mahasiswa angkatan ',tahun,'adalah',bop)
    # jumlah sks yang diambil angkatan 2020
    jumlah = int(input('Jumlah SKS yang diambil semester ini: '))
    
    if jumlah > 15:
        total = jumlah - 15
        tambahan = total * biaya
        print('Biaya tambahan untuk',total,'SKS:',tambahan)
        total_biaya = bop + tambahan
        print('Total biaya kuliah:',total_biaya)
        # subsidi pengajuan
        sbsd = input('Apakah Anda ingin mengajukan subsidi biaya kuliah? (Y/T): ')
        if sbsd == 'Y':
            # semester berapa sekarang
            sms = int(input('Semester berapa Anda sekarang? '))
            # rata-rata
            avg = 0
            # subsidi
            sub = 0
            print(sms)
            if 1 < sms < 9:
                for i in range(1, sms):
                    ip = eval(input("Masukkan IP semester " + str(i) + " :"))
                    if  0 < ip <= 4 :
                        avg += ip
                    else:
                        print("Salah memasukkan IP")
                        break
                # itung rata2 ip
                rata = avg/(sms-1)
                # itung total subsidi
                tsub = (round(rata, 2)/4.0 * 1000000)
                print("Anda mendapatkan subsidi sebesar",round(tsub))
                print("Total biaya kuliah:", total_biaya - round(tsub))
            else:
                ("Anda tidak bisa mengajukan subsidi biaya kuliah")
        elif sbsd == "T":
            print("Penghitungan biaya kuliah selesai.")
        else:
            print("Inputan yang anda masukkan salah.")
    elif jumlah == 15:
        print("Total biaya kuliah:",bop)
    else:
        print("Jumlah SKS anda kurang.")

elif nim[5:7] == '19' and len(nim) == 10:
    # bop angkatan 2019
    bop = 3500000
    # biaya angkatan 2019
    biaya = 175000
    tahun = 2019
    print('BOP mahasiswa angkatan ',tahun,'adalah',bop)
    # jumlah sks yang diambil angkatan 2019
    jumlah = int(input('Jumlah SKS yang diambil semester ini: '))
    # jika sks yg diambil lebih dari 15
    if jumlah > 15:
        total = jumlah - 15
        tambahan = total * biaya
        print('Biaya tambahan untuk',total,'SKS:',tambahan)
        total_biaya = bop + tambahan
        print('Total biaya kuliah:',total_biaya)
        # subsidi pengajuan
        sbsd = input('Apakah Anda ingin mengajukan subsidi biaya kuliah? (Y/T): ')
        if sbsd == 'Y':
            # semester berapa sekarang
            sms = int(input('Semester berapa Anda sekarang? '))
            # rata-rata
            avg = 0
            # subsidi
            sub = 0
            print(sms)
            # jika semester antara 1 dan 9 maka boleh ajukan subsidi
            if 1 < sms < 9:
                for i in range(1, sms):
                    ip = eval(input("Masukkan IP semester " + str(i) + " :"))
                    if  0 < ip <= 4 :
                        avg += ip
                    else:
                        print("Salah memasukkan IP")
                        break
                # itung rata2 ip
                rata = avg/(sms-1)
                # itung total subsidi
                tsub = (round(rata, 2)/4.0 * 1000000)
                print("Anda mendapatkan subsidi sebesar",round(tsub))
                print("Total biaya kuliah:", total_biaya - round(tsub))
            else:
                ("Anda tidak bisa mengajukan subsidi biaya kuliah")
        elif sbsd == "T":
            print("Penghitungan biaya kuliah selesai.")
        else:
            print("Inputan yang anda masukkan salah.")
    # jika sks = 15 maka biaya = bop
    elif jumlah == 15:
        print("Total biaya kuliah:",bop)
    else:
        print("Jumlah SKS anda kurang.")

elif nim[5:7] == '18' and len(nim) == 10:
    # bop angkatan 2018
    bop = 3200000
    # biaya angkatan 2018
    biaya = 150000
    tahun = 2018
    print('BOP mahasiswa angkatan ',tahun,'adalah',bop)
    # jumlah sks yang diambil angkatan 2018
    jumlah = int(input('Jumlah SKS yang diambil semester ini: '))
    # jika sks yg diambil lebih dari 15
    if jumlah > 15:
        total = jumlah - 15
        tambahan = total * biaya
        print('Biaya tambahan untuk',total,'SKS:',tambahan)
        total_biaya = bop + tambahan
        print('Total biaya kuliah:',total_biaya)
        # subsidi pengajuan
        sbsd = input('Apakah Anda ingin mengajukan subsidi biaya kuliah? (Y/T): ')
        if sbsd == 'Y':
            # semester berapa sekarang
            sms = int(input('Semester berapa Anda sekarang? '))
            # rata-rata
            avg = 0
            # subsidi
            sub = 0
            print(sms)
            # jika semester antara 1 dan 9 maka boleh ajukan subsidi
            if 1 < sms < 9:
                for i in range(1, sms):
                    ip = eval(input("Masukkan IP semester " + str(i) + " :"))
                    if  0 < ip <= 4 :
                        avg += ip
                    else:
                        print("Salah memasukkan IP")
                        break
                # itung rata2 ip
                rata = avg/(sms-1)
                # itung total subsidi
                tsub = (round(rata, 2)/4.0 * 1000000)
                print("Anda mendapatkan subsidi sebesar",round(tsub))
                print("Total biaya kuliah:", total_biaya - round(tsub))
            else:
                ("Anda tidak bisa mengajukan subsidi biaya kuliah")
        elif sbsd == "T":
            print("Penghitungan biaya kuliah selesai.")
        else:
            print("Inputan yang anda masukkan salah.")
    # jika sks = 15 maka biaya = bop
    elif jumlah == 15:
        print("Total biaya kuliah:",bop)
    else:
        print("Jumlah SKS anda kurang.")


elif nim[5:7] == '17' and len(nim) == 10:
    # bop angkatan 2017
    bop = 2800000
    # biaya angkatan 2017
    biaya = 130000
    tahun = 2017
    print('BOP mahasiswa angkatan ',tahun,'adalah',bop)
    # jumlah sks yang diambil angkatan 2017
    jumlah = int(input('Jumlah SKS yang diambil semester ini: '))
    # jika sks yg diambil lebih dari 15
    if jumlah > 15:
        total = jumlah - 15
        tambahan = total * biaya
        print('Biaya tambahan untuk',total,'SKS:',tambahan)
        total_biaya = bop + tambahan
        print('Total biaya kuliah:',total_biaya)
        # subsidi pengajuan
        sbsd = input('Apakah Anda ingin mengajukan subsidi biaya kuliah? (Y/T): ')
        if sbsd == 'Y':
            # semester berapa sekarang
            sms = int(input('Semester berapa Anda sekarang? '))
            # rata-rata
            avg = 0
            # subsidi
            sub = 0
            print(sms)
            # jika semester antara 1 dan 9 maka boleh ajukan subsidi
            if 1 < sms < 9:
                for i in range(1, sms):
                    ip = eval(input("Masukkan IP semester " + str(i) + " :"))
                    if  0 < ip <= 4 :
                        avg += ip
                    else:
                        print("Salah memasukkan IP")
                        break
                # itung rata2 ip
                rata = avg/(sms-1)
                # itung total subsidi
                tsub = (round(rata, 2)/4.0 * 1000000)
                print("Anda mendapatkan subsidi sebesar",round(tsub))
                print("Total biaya kuliah:", total_biaya - round(tsub))
            else:
                ("Anda tidak bisa mengajukan subsidi biaya kuliah")
        elif sbsd == "T":
            print("Penghitungan biaya kuliah selesai.")
        else:
            print("Inputan yang anda masukkan salah.")
    # jika sks = 15 maka biaya = bop
    elif jumlah == 15:
        print("Total biaya kuliah:",bop)
    else:
        print("Jumlah SKS anda kurang.")

else:
    print("NIM yang ada masukkan salah")

                