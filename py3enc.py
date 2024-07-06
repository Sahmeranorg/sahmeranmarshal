#!/usr/bin/env python
#Coded By SAHMERAN (SAHMERAN)
#Telegram Channel
#https://t.me/endlessarchivist


import os,marshal,time,random
try :
    from colorama import *
except:
    os.system('pip install colorama')
    from colorama import *

def cık():
    print("\n\033[95mGörüşürüz! Yine bekleriz 😉\033[00m")
    time.sleep(0.5)
    exit()

def enc():
    file_path = input('\033[94mŞifrelenecek python3 dosyasını yaz (örnek : file.py ) :\n\033[00m')
 
    if '.py' not in file_path:
        print(notfound)
        exit()
    else:
        try:
            file=open(file_path,'r').read()
            name = file_path.replace('.py','')
        except FileNotFoundError:
            print(notfound)
            exit()

    compiled_file = compile(file,'','exec')
    encoded_code = marshal.dumps(compiled_file)
    efile = open(f'{name}_encoded.py','w')
    efile.write('#encoded by SAHMERAN\nimport marshal\nexec(marshal.loads(' + repr(encoded_code) + '))')
    efile.close()
    print(f'\n\033[92mBaşarılı! Kod {name}_encoded.py dosyasına kaydedildi ✅\033[00m')
    time.sleep(3)

def dec():
    file = input('\033[94mÇözülecek python3 dosyasını yaz (örnek : file_encoded.py ) :\n\033[00m')
 
    if '.py' not in file_path:
        print(notfound)
        exit()
    else:
        try:
            file=open(file_path,'r').read()
            name = file_path.replace('.py','')
        except FileNotFoundError:
            print(notfound)
            exit()

    decompiled
    dfile = open(f"{name}.py", "w")
    dfile.write("#decoded by SAHMERAN\n\n")
    dfile.write(repr(decoded_code))


notfound="\033[91mHATA: Lütfen dosya adını\ndoğru yazdığınızdan emin olunuz!\033[00m"
alrdy = "\033[91mHATA: Girdiğiniz dosya zaten şifrelenmiş!\033[00m"

init()
os.system("clear")
banner="""\033[91m
                              SAHMERAN FİLELOCK TOOL

                         ███████████████████████████
                         ███████▀▀▀░░░░░░░▀▀▀███████
                         ████▀░░░░░░░░░░░░░░░░░▀████
                         ███│░░░░░░░░░░░░░░░░░░░│███
                         ██▌│░░░░░░░░░░░░░░░░░░░│▐██
                         ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
                         ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
                         ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
                         ██▌░│██████▌░░░▐██████│░▐██
                         ███░│▐███▀▀░░▄░░▀▀███▌│░███
                         ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
                         ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
                         ████▄─┘██▌░░░░░░░▐██└─▄████
                         █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
                         ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
                         █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
                         ███████▄░░░░░░░░░░░▄███████
                         ██████████▄▄▄▄▄▄▄██████████
                         ███████████████████████████

                  | TG : @OBİRSANALTANRİSİ - @ENDLESSARCHİVİST |
\033[00m
\033[93m🔒Marshal Şifreleme aracına hoşgeldiniz!🔒\n\033[90m✅Python3 script'inizi daha korunaklı hale getirin✅\n\033[92m😉 İyi eğlenceler 😉\nTG: https://t.me/endlessarchivist\033[00m
"""
print(banner)

try:
    enc()
        
except KeyboardInterrupt:
    cık()

