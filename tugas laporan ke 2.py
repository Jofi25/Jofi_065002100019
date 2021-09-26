# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 12:16:48 2021

@author: jofin
"""

x = input('Halo, Dengan Siapa Disini?: ')
print('Selamat Datang ', x)
print('Program kami dapat membantu anda untuk menghitung sebuah luas dari ruangan')
which = input('Ketik "Mulai" untuk memulai program: ')

if which == 'Mulai':
    print('Baik tolong masukkan panjang ruangan terlebih dahulu')
    p = int(input('Panjang Ruangan: '))
    l = int(input('Masukkan Lebar Ruangan: '))
    
print('Baik panjang ruangan adalah', p, 'dan lebar ruangan adalah', l,)
print('Sekarang tentukan apakah panjang dan lebar ruangan tersebut sudah Meter atau masih Centimeter')
print('Jika sudah Meter, ketik "Y"')
print('Jika masih Centimeter, ketik "N"')
which = input('Sudah atau Belum?: ')

if which == 'Y' :
    
    L = p * l
    print('Luas Dari Ruangan Tersebut Adalah:', L, 'Meter')
    
else : 
    converted_p = (p/100)
    converted_l = (l/100)
    L = converted_p * converted_l
    print('Baik luas dari ruangan tersebut setelah di rubah ke meter adalah', L, 'Meter')


    
print('Terima Kasih')
    