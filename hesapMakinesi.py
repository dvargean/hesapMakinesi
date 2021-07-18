giris = """
(1) Toplama
(2) Çıkarma
(3) Çarpma
(4) Bölme
"""
print(giris)


while True :
  soru = input("Yapmak istediğiniz işlemi yazınız(çıkmak için q): ")
  
  if soru == "q":
    print("Çıkılıyor...\nGüle güle :)")
    break

  elif soru == "1":
    sayı1=int(input("ilk sayı: "))
    sayı2=int(input("ikinci sayı: "))
    print(sayı1,"+",sayı2,"=",sayı1+sayı2)
   
  elif soru == "2":
    sayı3=int(input("ilk sayı: "))
    sayı4=int(input("ikinci sayı: "))
    print(sayı3,"-",sayı4,"=",sayı3-sayı4)
  
  elif soru == "3":
    sayı5=int(input("ilk sayı: "))
    sayı6=int(input("ikinci sayı: "))
    print(sayı5,"x",sayı6,"=",sayı5*sayı6)
  
  elif soru == "4":
    sayı7=int(input("ilk sayı: "))
    sayı8=int(input("ikinci sayı: "))
    print(sayı7,"÷",sayı8,"=",sayı7/sayı8)
  else:
    print("Hatalı işlem yaptınız.")
    print("Aşağıdaki seçeneklerden birini giriniz.",giris)
  