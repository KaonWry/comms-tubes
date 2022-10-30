#!/usr/bin/env python
# coding: utf-8

# In[28]:


print('Selamat datang di Anglur Selur')
print('Program ini akan membantumu dalam mobilisasi keseharianmu di ITB selama Semester 1 tahun ajaran 2022-2023 （╹◡╹）')
print('-----------------------------------------------------------------')

def Balik_Menu():
    print('Apakah mau kembali ke menu?')
    print('[1] Ya')
    print('[2] Keluar')
def Menu_Lanjutprak():
    print('Lanjut praktikum selanjutnya?')
    print('[1] Ya')
    print('[2] Tidak')
def Jalur_Masuk():
    print('dari mana?')
    print('[1] Gerbang Seni Rupa')
    print('[2] Gerbang Sipil')
    print('[3] Gerbang Utama Selatan')
    print('[4] Gedung Sebelumnya')
def Menu_Lanjut():
    print('Lanjut Mata kuliah selanjutnya?')
    print('[1] Ya ')
    print('[2] Tidak')
def Menu_Minggu():
    print('Hari ini minggu apa?')
    print('[1] Minggu A')
    print('[2] Minggu B')
def Menu_Hari(): #input hari untuk menentukan rute yang diambil dalam sehari kuliah
    print('Hari apa?')
    print('[1] Senin')
    print('[2] Selasa')
    print('[3] Rabu')
    print('[4] Kamis')
    print('[5] Jumat')
    print('[6] Sabtu')
    print('[7] Minggu')
    Hari=int(input())
    if (Hari == 1): #HARI SENIN
        Jalur_Masuk()
        JalurMasuk = int(input())#MATKUL PERTAMA KIMIA
        if (JalurMasuk == 1): 
            print(' Gerbang Seni Rupa ➝ Jalan J ➝ Jalan G ➝ Jalan 4')
            print(' Tujuanmu ada di sebelah utara/kanan jalan 4 yaitu oktagon ruangan 9017')
            print(' Selamat belajar Kimia Dasar 1 A :)')
        elif (JalurMasuk == 2):
            print(' Gerbang Sipil ➝ Jalan D ➝ Jalan 3 ➝ Jalan E ➝ Jalan 4 ')
            print(' Tujuanmu ada di sebelah utara/kiri jalan 4 yaitu oktagon ruangan 9017')
            print(' Selamat belajar Kimia Dasar 1 A :)')
        elif (JalurMasuk == 3):
            print(' Gerbang Utama ➝ Jalan A ➝ Jalan B ➝ Jalan 2 ➝ Jalan G ➝ Jalan 4')
            print(' Tujuanmu ada di sebelah utara/kanan jalan 4 yaitu oktagon ruangan 9017')
            print(' Selamat belajar Kimia Dasar 1 A :)')
        elif (JalurMasuk == 4):
            print(' Masih mata kuliah pertama, belum ada gedung sebelumnya :)') #Bantu looping biar input ulang jalur masuknya darimana aku gapaham
        else:#Bantu looping biar balik ke menu jalur masuk weh
            print('Invalid')
        Menu_Lanjut()
        Menulanjut = int(input())#MATKUL KEDUA FISIKA
        if (Menulanjut == 1):
            Jalur_Masuk()
            JalurMasuk = int(input())
            if (JalurMasuk == 1):
                print(' Gerbang seni rupa ➝ Jalan J➝ Jalan 2 ➝ Jalan C ke Utara')
                print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9121')
                print(' Selamat belajar Fisika Dasar 1 A :)')
            elif (JalurMasuk == 2):
                print(' Gerbang Sipil ➝ Jalan C ke Utara')
                print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9121')
                print(' Selamat belajar Fisika Dasar 1 A :)')
            elif (JalurMasuk == 3):
                print(' Gerbang utama selatan ➝ Jalan 1 ➝ Jalan C')
                print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9121')
                print(' Selamat belajar Fisika Dasar 1 A :)')
            elif (JalurMasuk == 4):
                print(' Oktagon ke selatan ➝ Jalan 4 ➝ Jalan E ➝ Jalan 3')
                print(' Tujuanmu ada di sebelah selatan/kiri jalan 3 yaitu Gedung GKUB ruangan 9121')
                print(' Selamat belajar Fisika Dasar 1 A :)')
            else: #bantui looping gimana oiy biar bisa balik ke menu jalur_masuk
                print('invalid')
        elif (Menulanjut == 2):
            Balik_Menu()
            BalikMenu = int(input())
            if (BalikMenu == 1):
                Menu_Tampilan()
            elif (BalikMenu == 2):
                print('Terimakasih telah menggunakan program')
        Menu_Lanjut()
        Menulanjut = int(input())
        if (Menulanjut == 1):
            Jalur_Masuk()
            JalurMasuk = int(input())
            if (JalurMasuk == 1): 
                print(' Gerbang Seni Rupa ➝ Jalan J ➝ Jalan G ➝ Jalan 4')
                print(' Tujuanmu ada di sebelah utara/kanan jalan 4 yaitu oktagon ruangan 9017')
                print(' Selamat belajar TTKI :)')
            elif (JalurMasuk == 2):
                print(' Gerbang Sipil ➝ Jalan D ➝ Jalan 3 ➝ Jalan E ➝ Jalan 4 ')
                print(' Tujuanmu ada di sebelah utara/kiri jalan 4 yaitu oktagon ruangan 9017')
                print(' Selamat belajar TTKI :)')
            elif (JalurMasuk == 3):
                print(' Gerbang Utama ➝ Jalan A ➝ Jalan B ➝ Jalan 2 ➝ Jalan G ➝ Jalan 4')
                print(' Tujuanmu ada di sebelah utara/kanan jalan 4 yaitu oktagon ruangan 9017')
                print(' Selamat belajar TTKI :)')
            elif (JalurMasuk == 4):
                print(' GKUB ➝ Jalan 3 ➝ Jalan E ➝ Jalan 4')
                print(' Tujuanmu ada di sebelah utara/kiri jalan 4 yaitu oktagon ruangan 9017')
                print(' Selamat belajar TTKI :)')
            else:
                print('Invalid')
        elif (Menulanjut == 2):
            Balik_Menu()
            BalikMenu = int(input())
            if (BalikMenu == 1):
                Menu_Tampilan()
            elif (BalikMenu == 2):
                print('Terimakasih telah menggunakan program')
        Menu_Lanjut()
        Menulanjut = int(input())
        if (Menulanjut == 1):
            Jalur_Masuk()
            JalurMasuk = int(input())
            if (JalurMasuk == 1): 
                print(' Gerbang Seni Rupa ➝ Jalan J ➝ Jalan G ➝ Jalan 4')
                print(' Tujuanmu ada di sebelah utara/kanan jalan 4 yaitu oktagon ruangan 9017')
                print(' Selamat belajar Pengenalan Komputasi :)')
            elif (JalurMasuk == 2):
                print(' Gerbang Sipil ➝ Jalan D ➝ Jalan 3 ➝ Jalan E ➝ Jalan 4 ')
                print(' Tujuanmu ada di sebelah utara/kiri jalan 4 yaitu oktagon ruangan 9017')
                print(' Selamat belajar Pengenalan Komputasi :)')
            elif (JalurMasuk == 3):
                print(' Gerbang Utama ➝ Jalan A ➝ Jalan B ➝ Jalan 2 ➝ Jalan G ➝ Jalan 4')
                print(' Tujuanmu ada di sebelah utara/kanan jalan 4 yaitu oktagon ruangan 9017')
                print(' Selamat belajar Pengenalan Komputasi :)')
            elif (JalurMasuk == 4):
                print(' Kamu sudah di Oktagon')
                print(' Tujuanmu ada di oktagon ruangan 9017')
                print(' Selamat belajar Pengenalan Komputasi :)')
            else: 
                print('Invalid')
        elif(Menulanjut == 2):
            Balik_Menu()
            BalikMenu = int(input())
            if (BalikMenu == 1):
                Menu_Tampilan()
            elif (BalikMenu == 2):
                print('Terimakasih telah menggunakan program')
    elif (Hari == 2):
        Menu_Minggu()
        Mingguke = int(input())
        if (Mingguke == 1):
            if(NIM > 16322215):
                Jalur_Masuk()
                JalurMasuk = int(input())
                if (JalurMasuk == 1):
                    print(' Gerbang seni rupa ➝ Jalan J ➝ Jalan G ➝ Jalan 4')
                    print(' Tujuanmu ada di sebelah utara/kanan jalan 4 yaitu gedung Lab Fisika Dasar')
                    print(' Selamat Praktikum Fisika Dasar. Jangan lupa jaslab :)')
                elif (JalurMasuk == 2):
                    print(' Gerbang sipil ➝ Jalan D ➝ Jalan 3 ➝ Jalan E ➝ Jalan 4')
                    print(' Tujuanmu ada di sebelah utara/kiri Jalan 4 yaitu gedung Lab Fisika Dasar')
                    print(' Selamat Praktikum Fisika Dasar. Jangan lupa jaslab')
                elif (JalurMasuk == 3):
                    print(' Gerbang utama selatan ➝ Jalan A ➝ Jalan B ➝ Jalan 2 ➝ Jalan G ➝ Jalan 4')
                    print(' Tujuanmu ada di sebelah utara/kanan jalan 4 yaitu gedung Lab Fisika Dasar')
                    print(' Selamat Praktikum Fisika Dasar. Jangan lupa jaslab :)')
                elif (JalurMasuk == 4):
                    print(' Masih mata praktikum pertama, belum ada gedung sebelumnya :)')
                Menu_Lanjutprak()
                Menulanjut = int(input())
                if (Menulanjut == 1):
                    Jalur_Masuk()
                    JalurMasuk = int(input())
                    if (JalurMasuk == 1):
                        print(' Gerbang seni rupa ➝ Jalan J ➝ Jalan 2 ➝ Jalan G')
                        print(' Tujuanmu ada di sebelah barat/kiri Jalan G yaitu gedung Labtek 1 di depan gedung Lab Kimia Dasar')
                        print(' Selamat praktikum pengenalan komputasi :)')
                    elif (JalurMasuk == 2):
                        print(' Gerbang sipil ➝ Jalan D ➝ Jalan 3 ➝ Jalan E ➝ Jalan 4 ➝ Jalan G')
                        print(' Tujuanmu ada di sebelah barat/kiri Jalan G yaitu gedung Labtek 1 di depan gedung Lab Kimia Dasar')
                        print(' Selamat praktikum pengenalan komputasi :)')
                    elif (JalurMasuk == 3):
                        print(' Gerbang utama selatan ➝ Jalan A ➝ Jalan B ➝ Jalan 2 ➝ Jalan G')
                        print(' Tujuanmu ada di sebelah barat/kiri Jalan G yaitu gedung Labtek 1 di depan gedung Lab Kimia Dasar')
                        print(' Selamat praktikum pengenalan komputasi :)')
                    elif (JalurMasuk == 4):
                        print(' Gedung lab fisika dasar ➝ Gedung Labtek 1')
                        print(' Tujuanmu ada tepat dibelakang gedung lab fisika dasar')
                        print(' Selamat praktikum pengenalan komputasi :)')
                elif(Menulanjut == 2):
                    Balik_Menu()
                    BalikMenu = int(input())
                    if (BalikMenu == 1):
                        Menu_Tampilan()
                    elif (BalikMenu == 2):
                        print('Terimakasih telah menggunakan program')

            else:
                Jalur_Masuk()
                JalurMasuk = int(input())
                if (JalurMasuk == 1):
                    print(' Gerbang seni rupa ➝ Jalan J ➝ Jalan G ➝ Jalan 4')
                    print(' Tujuanmu ada di sebelah utara/kanan jalan 4 yaitu gedung Lab Fisika Dasar')
                    print(' Selamat Praktikum Fisika Dasar. Jangan lupa jaslab :)')
                elif (JalurMasuk == 2):
                    print(' Gerbang sipil ➝ Jalan D ➝ Jalan 3 ➝ Jalan E ➝ Jalan 4')
                    print(' Tujuanmu ada di sebelah utara/kiri Jalan 4 yaitu gedung Lab Fisika Dasar')
                    print(' Selamat Praktikum Fisika Dasar. Jangan lupa jaslab')
                elif (JalurMasuk == 3):
                    print(' Gerbang utama selatan ➝ Jalan A ➝ Jalan B ➝ Jalan 2 ➝ Jalan G ➝ Jalan 4')
                    print(' Tujuanmu ada di sebelah utara/kanan jalan 4 yaitu gedung Lab Fisika Dasar')
                    print(' Selamat Praktikum Fisika Dasar. Jangan lupa jaslab :)')
                elif (JalurMasuk == 4):
                    print(' Masih praktikum pertama, belum ada gedung sebelumnya :)')
                Balik_Menu()
                BalikMenu = int(input())
                if (BalikMenu == 1):
                    Menu_Tampilan()
                elif (BalikMenu == 2):
                    print('Terimakasih telah menggunakan program')
        elif(Mingguke == 2):
            Jalur_Masuk()
            JalurMasuk = int(input())
            if (JalurMasuk == 1):
                print(' Gerbang seni rupa ➝ Jalan J ➝ Jalan 2➝ Jalan G')
                print(' Tujuanmu ada di sebelah timur/kanan Jalan G yaitu Gedung Lab Kimia Dasar')
                print(' Selamat Praktikum Kimia Dasar. Jangan lupa jaslab:)')
            elif (JalurMasuk ==2 ):
                print(' Gerbang Sipil ➝ Jalan 1 ➝ Jalan J ➝ Jalan 2 ➝ Jalan G ')
                print(' Tujuanmu ada di sebelah timur/kanan Jalan G yaitu Gedung Lab Kimia Dasar')
                print(' Selamat Praktikum Kimia Dasar. Jangan lupa jaslab:)')
            elif (JalurMasuk == 3):
                print(' Gerbang utama selatan ➝ Jalan B ➝ Jalan 2 ➝ Jalan G')
                print(' Tujuanmu ada di sebelah timur/kanan Jalan G yaitu Gedung Lab Kimia Dasar')
                print(' Selamat Praktikum Kimia Dasar. Jangan lupa jaslab:)')
            elif(JalurMasuk == 4):
                print(' Masih praktikum pertama, belum ada gedung sebelumnya :)')
            Balik_Menu()
            BalikMenu = int(input())
            if (BalikMenu == 1):
                Menu_Tampilan()
            elif (BalikMenu == 2):
                print('Terimakasih telah menggunakan program')
    elif (Hari == 3): #HARI RABU
        Jalur_Masuk()
        JalurMasuk = int(input())#MATKUL PERTAMA MATEMATIKA
        if (JalurMasuk == 1):
            print(' Gerbang seni rupa ➝ Jalan J➝ Jalan 2 ➝ Jalan C ke Utara')
            print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9104')
            print(' Selamat belajar Matematika 1 A :)')
        elif (JalurMasuk == 2):
            print(' Gerbang Sipil ➝ Jalan C ke Utara')
            print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9104')
            print(' Selamat belajar Matematika 1 A :)')
        elif (JalurMasuk == 3):
            print(' Gerbang utama selatan ➝ Jalan 1 ➝ Jalan C')
            print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9104')
            print(' Selamat belajar Matematika 1 A :)')
        elif (JalurMasuk == 4):
            print(' Masih mata kuliah pertama, belum ada gedung sebelumnya :)')
        else: 
            print('invalid')
        Menu_Lanjut()
        Menulanjut = int(input()) #MATKUL KE DUA FISIKA
        if (Menulanjut == 1):
            Jalur_Masuk()
            JalurMasuk = int(input())
            if (JalurMasuk == 1):
                print(' Gerbang seni rupa ➝ Jalan J➝ Jalan 2 ➝ Jalan C ke Utara')
                print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9104')
                print(' Selamat belajar Fisika Dasar 1 A :)')
            elif (JalurMasuk == 2):
                print(' Gerbang Sipil ➝ Jalan C ke Utara')
                print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9104')
                print(' Selamat belajar Fisika Dasar 1 A :)')
            elif (JalurMasuk == 3):
                print(' Gerbang utama selatan ➝ Jalan 1 ➝ Jalan C')
                print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9104')
                print(' Selamat belajar Fisika Dasar 1 A :)')
            elif (JalurMasuk == 4):
                print(' Kamu sudah di GKUB')
                print(' Tujuanmu ada di GKUB ruangan 9104')
                print(' Selamat belajar Fisika Dasar 1 A')
            else:
                print('invalid')
        elif(Menulanjut == 2):
            Balik_Menu()
            BalikMenu = int(input())
            if (BalikMenu == 1):
                Menu_Tampilan()
            elif (BalikMenu == 2):
                print('Terimakasih telah menggunakan program')
        
        Menu_Lanjut() 
        Menulanjut = int(input()) #MATKUL KE 3 PITB
        if (Menulanjut == 1):
            Jalur_Masuk()
            JalurMasuk = int(input())
            if (JalurMasuk == 1):
                print(' Gerbang seni rupa ➝ Jalan J ➝ Jalan G')
                print(' Tujuanmu ada di sebelah timur/kanan jalan G yaitu Gedung GKUT ruangan 9213')
                print(' Selamat belajar PITB :)')
            elif (JalurMasuk == 2):
                print(' Gerbang sipil ➝ Jalan C ➝ Jalan 2 ➝ Jalan G')
                print(' Tujuanmu ada di sebelah timur/kanan jalan G yaitu Gedung GKUT ruangan 9213')
                print(' Selamat belajar PITB :)')
            elif (JalurMasuk == 3):
                print(' Gerbang utama selatan ➝ Jalan 1 ke timur ➝ Jalan J ➝ Jaln G ')
                print(' Tujuanmu ada di sebelah timur/kanan jalan G yaitu Gedung GKUT ruangan 9213')
                print(' Selamat belajar PITB :)')
            elif (JalurMasuk == 4):
                print(' GKUB ➝ Jalan 3 ➝ Jalan E ➝ Jalan 4 ➝ Jalan G ke selatan')
                print(' Tujuanmu ada di sebelah timur/kiri jalan G yaitu Gedung GKUT ruangan 9213')
                print(' Selamat belajar PITB :)')
            else:
                print('invalid')
        elif (Menulanjut == 2):
            Balik_Menu()
            BalikMenu = int(input())
            if (BalikMenu == 1):
                Menu_Tampilan()
            elif (BalikMenu == 2):
                print('Terimakasih telah menggunakan program')
    elif(Hari == 4): #HARI KAMIS 
        Jalur_Masuk()
        JalurMasuk = int(input()) #MATKUL PERTAMA KIMIA 
        if (JalurMasuk == 1):
            print(' Gerbang seni rupa ➝ Jalan J➝ Jalan 2 ➝ Jalan C ke Utara')
            print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9307')
            print(' Selamat belajar Kimia Dasar 1 A :)')
        elif (JalurMasuk == 2):
            print(' Gerbang Sipil ➝ Jalan C ke Utara')
            print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9307')
            print(' Selamat belajar Kimia Dasar 1 A :)')
        elif (JalurMasuk == 3):
            print(' Gerbang utama selatan ➝ Jalan 1 ➝ Jalan C')
            print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9307')
            print(' Selamat belajar Kimia Dasar 1 A :)')
        elif (JalurMasuk == 4):
            print('Masih mata kuliah pertama, belum ada gedung sebelumnya :)') 
        else:
            print('invalid')
            
        Balik_Menu()
        BalikMenu = int(input())
        if (BalikMenu == 1):
            Menu_Tampilan()
        elif (BalikMenu == 2):
            print('Terimakasih telah menggunakan program')
            
    elif(Hari == 5):
        Jalur_Masuk()
        JalurMasuk = int(input())#MATKUL PERTAMA MATEMATIKA
        if (JalurMasuk == 1):
            print(' Gerbang seni rupa ➝ Jalan J➝ Jalan 2 ➝ Jalan C ke Utara')
            print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9104')
            print(' Selamat belajar Matematika Dasar 1 A :)')
        elif (JalurMasuk == 2):
            print(' Gerbang Sipil ➝ Jalan C ke Utara')
            print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9104')
            print(' Selamat belajar Matematika Dasar 1 A :)')
        elif (JalurMasuk == 3):
            print(' Gerbang utama selatan ➝ Jalan 1 ➝ Jalan C')
            print(' Tujuanmu ada di sebelah utara/depan jalan C yaitu Gedung GKUB ruangan 9104')
            print(' Selamat belajar Matematika Dasar 1 A :)')
        elif (JalurMasuk == 4):
            print('Masih mata kuliah pertama, belum ada gedung sebelumnya :)') 
        else:
            print('invalid')
        Menu_Lanjutprak()
        Menulanjut = int(input())
        if (Menulanjut == 1):
            Jalur_Masuk()
            JalurMasuk = int(input())
            if (JalurMasuk == 1):
                print(' Gerbang seni rupa ➝ Jalan J ➝ Jalan 2 ➝ Jalan G')
                print(' Tujuanmu ada di sebelah barat/kiri Jalan G yaitu gedung Labtek 1 di depan gedung Lab Kimia Dasar')
                print(' Selamat praktikum pengenalan komputasi :)')
            elif (JalurMasuk == 2):
                print(' Gerbang sipil ➝ Jalan D ➝ Jalan 3 ➝ Jalan E ➝ Jalan 4 ➝ Jalan G')
                print(' Tujuanmu ada di sebelah barat/kiri Jalan G yaitu gedung Labtek 1 di depan gedung Lab Kimia Dasar')
                print(' Selamat praktikum pengenalan komputasi :)')
            elif (JalurMasuk == 3):
                print(' Gerbang utama selatan ➝ Jalan A ➝ Jalan B ➝ Jalan 2 ➝ Jalan G')
                print(' Tujuanmu ada di sebelah barat/kiri Jalan G yaitu gedung Labtek 1 di depan gedung Lab Kimia Dasar')
                print(' Selamat praktikum pengenalan komputasi :)')
            elif (JalurMasuk == 4):
                print(' Gedung lab fisika dasar ➝ Gedung Labtek 1')
                print(' Tujuanmu ada tepat dibelakang gedung lab fisika dasar')
                print(' Selamat praktikum pengenalan komputasi :)')
        elif(Menulanjut == 2):
            Balik_Menu()
            BalikMenu = int(input())
            if (BalikMenu == 1):
                Menu_Tampilan()
            elif (BalikMenu == 2):
                print('Terimakasih telah menggunakan program')
    elif(Hari == 6):
        print('Hari libur nich')
        Balik_Menu()
        BalikMenu = int(input())
        if (BalikMenu == 1):
            Menu_Tampilan()
        elif (BalikMenu == 2):
            print('Terimakasih telah menggunakan program')
    elif(Hari == 7):
        print('Hari libur nich')
        Balik_Menu()
        BalikMenu = int(input())
        if (BalikMenu == 1):
            Menu_Tampilan()
        elif (BalikMenu == 2):
            print('Terimakasih telah menggunakan program')
        
def Menu_Kalender():
    print('Selamat datang di menu kalender akademik')
    print('Masukkan tanggal yang dituju dengan format DD/MM/YYYY')
    Kalender = ['Hari kosong tanpa agenda' for i in range (1,730)]
    Kalender[55] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[56] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[57] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[58] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[59] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[60] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[61] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[62] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[63] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[64] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[65] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[66] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[67] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[68] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[69] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[70] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
    Kalender[217] ='Batas Akhir Pengajuan Perpanjangan Waktu Studi dari mahasiswa'
    Kalender[221] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
    Kalender[222] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
    Kalender[223] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
    Kalender[224] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
    Kalender[225] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
    Kalender[226] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
    Kalender[227] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
    Kalender[228] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
    Kalender[233] ='Batas Waktu Pembayaran Biaya Pendidikan Semester I-2022/2023 bagi Mahasiswa Lama'
    Kalender[234] ='Hari Pertama Masa Kuliah Semester I-2022/20223 & Batas Akhir Perubahan Nilai Mata Kuliah KP/TA/Tesis/Disertasi Semester I-2021/2022 '
    Kalender[249] ='Yudisium ITB Bulan September 2022'
    Kalender[252] ='Batas Akhir Perubahan Nilai Mata Kuliah Bukan KP/TA/Tesis/Disertasi Semester II-2021/2022 dan Semester Pendek 2021/2022'
    Kalender[256] ='Penggantian Rencana Studi Semester I-2022/2023'
    Kalender[257] ='Penggantian Rencana Studi Semester I-2022/2023'
    Kalender[258] ='Penggantian Rencana Studi Semester I-2022/2023'
    Kalender[259] ='Penggantian Rencana Studi Semester I-2022/2023'
    Kalender[262] ='Penyelesaian Kasus Mahasiswa yang Tidak Mendaftar Dua Semester'
    Kalender[271] ='Batas Waktu Pemenuhan Persyaratan Administrasi Kelulusan dan Pendaftaran Seremoni Wisuda Pertama Tahun Akademik 2022/2023'
    Kalender[277] ='Yudisium ITB Bulan Oktober 2022'
    Kalender[278] ='Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
    Kalender[279] ='Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
    Kalender[280] ='Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
    Kalender[281] ='Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
    Kalender[282] ='Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
    Kalender[283] ='Masa Ujian Tengah Semester I-2022/2022 & Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
    Kalender[284] ='Masa Ujian Tengah Semester I-2022/2022 & Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
    Kalender[285] ='Masa Ujian Tengah Semester I-2022/2022 & Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
    Kalender[286] ='Masa Ujian Tengah Semester I-2022/2022 & Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
    Kalender[287] =' Batas Waktu Pemasukan Nilai MBKM Semester II-2021/2022 & Masa Ujian Tengah Semester I-2022/2022 & Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
    Kalender[289] ='Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
    Kalender[290] ='Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
    Kalender[291] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
    Kalender[292] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
    Kalender[293] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
    Kalender[294] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
    Kalender[295] =' Hari Wisuda Pertama Tahun Akademik 2022/2023 & Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
    Kalender[296] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
    Kalender[297] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
    Kalender[298] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
    Kalender[299] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
    Kalender[300] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
    Kalender[301] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
    Kalender[305] ='Yudisium ITB Bulan November 2022'
    Kalender[321] ='Batas Koreksi DPK untuk Acuan DNA Semester I-2022/2023'
    Kalender[332] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[333] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[334] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[335] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[336] ='Hari Terakhir Masa Kuliah Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[337] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[338] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[339] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[340] ='Ujian Akhir Semester I-2022/2023 & Yudisium ITB Bulan Desember 2022 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[341] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[342] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[343] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[344] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[345] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[346] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
    Kalender[347] ='Ujian Akhir Semester I-2022/2023'
    Kalender[348] ='Ujian Akhir Semester I-2022/2023'
    Kalender[349] ='Ujian Akhir Semester I-2022/2023'
    Kalender[350] ='Ujian Akhir Semester I-2022/2023'
    Kalender[351] ='Ujian Akhir Semester I-2022/2023'
    Kalender[352] ='Ujian Akhir Semester I-2022/2023'
    Kalender[353] ='Ujian Akhir Semester I-2022/2023'
    Kalender[354] ='Ujian Akhir Semester I-2022/2023'
    Kalender[356] ='Batas Akhir Pengajuan Perpanjangan Waktu Studi dari mahasiswa '
    Kalender[368] ='Yudisium ITB Bulan Januari 2023'
    Kalender[369] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa & Penyelesaian Kasus Batas Waktu Studi untuk Mahasiswa Yang Mendaftar di Semester Genap'
    Kalender[370] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa'
    Kalender[371] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa'
    Kalender[372] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa'
    Kalender[373] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa'
    Kalender[374] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa'
    Kalender[375] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa'
    Kalender[377] ='Sidang Terbuka ITB Dalam Rangka Penerimaan Seluruh Mahasiswa Baru Semester Genap'
    Kalender[380] ='Batas Waktu Pembayaran Biaya Pendidikan Semester II-2022/2023'
    Kalender[381] ='Hari Pertama Masa Kuliah Semester II-2022/2023 & Batas Akhir Perubahan Nilai Mata Kuliah KP/TA/Tesis/Disertasi Semester II-2021/2022 dan Semester Pendek 2021/2022'
    Kalender[395] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[396] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[397] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[398] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[399] ='Batas Akhir Perubahan Nilai Mata Kuliah Bukan KP/TA/Tesis/Disertasi Semester I-2022/2023 & Verifikasi Portofolio Semester I-2022/2023'
    Kalender[400] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[401] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[402] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[403] ='Penggantian Rencana Studi Semester II-2022/2023 & Yudisium ITB Bulan Februari 2023 & Verifikasi Portofolio Semester I-2022/2023'
    Kalender[404] ='Penggantian Rencana Studi Semester II-2022/2023 & Verifikasi Portofolio Semester I-2022/2023'
    Kalender[405] ='Penggantian Rencana Studi Semester II-2022/2023 & Verifikasi Portofolio Semester I-2022/2023'
    Kalender[406] ='Penggantian Rencana Studi Semester II-2022/2023 & Verifikasi Portofolio Semester I-2022/2023'
    Kalender[407] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[408] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[409] ='Penyelesaian Kasus Mahasiswa yang Tidak Mendaftar Dua Semester & Verifikasi Portofolio Semester I-2022/2023'
    Kalender[410] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[411] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[412] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[413] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[414] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[415] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[416] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[417] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[418] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[419] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[420] ='Verifikasi Portofolio Semester I-2022/2023'
    Kalender[426] ='Sidang Terbuka Dalam Rangka Dies Natalis ke-64 ITB'
    Kalender[430] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi & Masa Ujian Tengah Semester II-2022/2023'
    Kalender[431] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi & Yudisium ITB Bulan Maret 2023 & Masa Ujian Tengah Semester II-2022/2023'
    Kalender[432] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi & Masa Ujian Tengah Semester II-2022/2023'
    Kalender[433] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi & Masa Ujian Tengah Semester II-2022/2023'
    Kalender[434] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi & Masa Ujian Tengah Semester II-2022/2023'
    Kalender[435] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[436] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[437] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[438] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[439] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[439] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[440] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[441] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[442] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[443] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[444] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[445] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[446] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[447] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[448] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[449] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[450] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[451] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[452] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[453] ='Batas Waktu Pemenuhan Persyaratan Administrasi Kelulusan dan Pendaftaran Seremoni Wisuda Kedua Tahun Akademik 2022/2023Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[454] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[455] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
    Kalender[456] ='Yudisium ITB Bulan April 2023'
    Kalender[474] ='Batas Koreksi DPK untuk Acuan DNA Semester II-2022/2023'
    Kalender[460] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[461] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[462] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[463] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[464] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[465] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[466] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[467] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[468] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[469] ='Batas Waktu Pemasukan Nilai MBKM Semester I-2022/2023 & Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[470] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[471] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[472] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[474] ='Libur Kuliah dalam rangka Idul Fitri'
    Kalender[475] ='Libur Kuliah dalam rangka Idul Fitri'
    Kalender[476] ='Libur Kuliah dalam rangka Idul Fitri'
    Kalender[477] ='Libur Kuliah dalam rangka Idul Fitri'
    Kalender[478] ='Libur Kuliah dalam rangka Idul Fitri'
    Kalender[479] ='Libur Kuliah dalam rangka Idul Fitri'
    Kalender[480] ='Libur Kuliah dalam rangka Idul Fitri'
    Kalender[483] ='Batas Akhir Pemilihan untuk Mahasiswa Berprestasi Tingkat Fakultas/Sekolah'
    Kalender[484] ='Hari Wisuda Kedua Tahun Akademik 2022/2023'
    Kalender[487] ='Yudisium ITB Bulan Mei 2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[488] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[489] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[490] ='Hari Terakhir Masa Kuliah Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[491] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[492] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[493] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[494] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[495] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[496] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[497] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[498] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[499] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[500] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[501] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[502] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[503] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[504] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[505] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[506] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[507] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
    Kalender[508] ='Ujian Akhir Semester II-2022/2023'
    Kalender[522] ='Yudisium ITB Bulan Juni 2023 & Batas Akhir Pemasukan Nilai Mata Kuliah Semester II-2022/2023'
    Kalender[523] ='Batas Akhir Pengisian Kuesioner Akhir Pilihan Program Studi Mahasiswa TPB 2023'
    Kalender[529] ='Penjurusan Mahasiswa TPB 2023'
    Kalender[612] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[613] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[614] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[615] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[616] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[617] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[618] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[619] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[620] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[621] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[622] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[623] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[624] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[625] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[626] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[627] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[628] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[629] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[630] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[631] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[632] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[633] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[634] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[635] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[636] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[637] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[638] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[639] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[640] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[641] ='Verifikasi Portofolio Semester II-2022/2023'
    Kalender[642] ='Verifikasi Portofolio Semester II-2022/2023'

    while True:   
        Tanggal = int(input('Tanggal : '))
        Bulan = int(input('Bulan : '))
        Tahun = int(input('Tahun : '))
        if (Tanggal <= 31 and Tanggal >= 1 and Bulan <= 12 and Bulan >= 1 and Tahun in [2022,2023]):
            break
        else:
            continue

    if (Bulan == 1 and Tahun == 2022):
        i = Tanggal
    elif (Bulan == 2 and Tahun == 2022):
        i = Tanggal + 31
    elif (Bulan == 3 and Tahun == 2022):
        i = Tanggal + 59
    elif (Bulan == 4 and Tahun == 2022):
        i = Tanggal + 90
    elif (Bulan == 5 and Tahun == 2022):
        i = Tanggal + 120
    elif (Bulan == 6 and Tahun == 2022):
        i = Tanggal + 151
    elif (Bulan == 7 and Tahun == 2022):
        i = Tanggal + 181
    elif (Bulan == 8 and Tahun == 2022):
        i = Tanggal + 212
    elif (Bulan == 9 and Tahun == 2022):
        i = Tanggal + 243
    elif (Bulan == 10 and Tahun == 2022):
        i = Tanggal + 273
    elif (Bulan == 11 and Tahun == 2022):
        i = Tanggal + 304
    elif (Bulan == 12 and Tahun == 2022):
        i = Tanggal + 334
    elif (Bulan == 1 and Tahun == 2023):
        i = Tanggal + 365
    elif (Bulan == 2 and Tahun == 2023):
        i = Tanggal + 396
    elif (Bulan == 3 and Tahun == 2023):
        i = Tanggal + 424
    elif (Bulan == 4 and Tahun == 2023):
        i = Tanggal + 455
    elif (Bulan == 5 and Tahun == 2023):
        i = Tanggal + 485
    elif (Bulan == 6 and Tahun == 2023):
        i = Tanggal + 516
    elif (Bulan == 7 and Tahun == 2023):
        i = Tanggal + 546
    elif (Bulan == 8 and Tahun == 2023):
        i = Tanggal + 577
    elif (Bulan == 9 and Tahun == 2023):
        i = Tanggal + 608
    elif (Bulan == 10 and Tahun == 2023):
        i = Tanggal + 638
    elif (Bulan == 11 and Tahun == 2023):
        i = Tanggal + 669
    elif (Bulan == 12 and Tahun == 2023):
        i = Tanggal + 699

    print('Pada tanggal berikut terdapat ' + str(Kalender[i]))
    
def Menu_Tampilan(): #Input Menu yang mau dipakai user
    print('MENU')
    print('[1] Temukan rute perjalanan pada hari tertentu')
    print('[2] Cari tahu kegiatan pada tanggal tertentu ')
    print('[3] Keluar program')
    MenuTampilan = int(input())
    if (MenuTampilan == 1):  
            Menu_Hari()
    elif (MenuTampilan == 2):
        Menu_Kalender()
        Balik_Menu()
        BalikMenu = int(input())
        if (BalikMenu==1):
            Menu_Tampilan()
        elif (BalikMenu==2):
            print('Terimakasih telah menggunakan program ini')
    elif (MenuTampilan == 3):
        print('Terimakasih telah menggunakan program ini')

NIM = int(input(' Masukkan NIM-mu : '))
importData = open("dataKelas02.txt", "r")
importData = importData.read()
importData = (importData.split("\n"))
dataNIM = [0] * len(importData)
dataNama = [0] * len(importData)
j = 0
for i in importData:
    i = i.split("-")
    dataNama[j] = i[1]
    dataNIM[j] = i[0]
    j += 1
dataNIM = list(map(int, dataNIM))
if (NIM in dataNIM):
    print(f"Halo, {dataNama[dataNIM.index(NIM)]}")
    Menu_Tampilan()
else:
    print("Anda bukan golongan kami.")
