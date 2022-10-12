from math import*
def kurehacim(yarıcap):
    hacim=4/3*pi*yarıcap**3
    return hacim
def kureaalan(yarıcap):
    alan=4*pi*yarıcap**2
    return alan
def silindiryuzeyalan(yarıcap,yukseklik):
    yuzeyalan=2*pi*yarıcap*(yarıcap+yukseklik)
    return yuzeyalan
def silindirhacim(yarıcap,yukseklik):
    hacim=pi*(yarıcap**2)*yukseklik
    return hacim
def kuphacmi(a):
    hacim=a**3
    return hacim
print("-------------------------------------------")
print("* Kürenin hacmini Hesaplamak için     [1] -")
print("* Kürenin alanını Hesaplamak için     [2] -")
print("* Silindir Yüzeyalanı Hesaplamak için [3] -")
print("* Silindir  hacmini Hesaplamak için   [4] -")
print("* Küp alma işlemi için                [5] -")
print("-------------------------------------------")
while True:
    try:
        secenek=int(input("Yapmak istediğiniz hesaplama türünü giriniz: "))
        if secenek==1:
            yarıcap=int(input("Yarıçap Giriniz: "))
            print(kuphacmi(yarıcap))
        elif secenek==2:
            yarıcap=int(input("Yarıçap Giriniz: "))
            print(kureaalan(yarıcap))
        elif secenek==3:
            yarıcap=int(input("Yarıçap Giriniz     : "))
            yukseklik=int(input("Yükseklik Giriniz   : "))
            print(silindiryuzeyalan(yarıcap,yukseklik))
        elif secenek==4:
            yarıcap=int(input("Yarıçap Giriniz     : "))
            yukseklik=int(input("Yükseklik Giriniz   : "))
            print(silindirhacim(yarıcap,yukseklik))
        elif secenek==5:
            a=int(input("Küpünü almak istediğiniz değeri giriniz: "))
            print(kuphacmi(a))
        elif secenek==6:
            break
        else:
            print("SADECE TABLODAKİ 5 SEÇENEKTEN BİRİNİ GİRİNİZ")
    except ValueError:
        print("LÜTFEN SADECE SAYISAL DEĞER GİRİNİZ!!")