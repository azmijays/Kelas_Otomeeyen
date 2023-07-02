def is_prime (number):
    if number < 2: #Bilangan kurang dari 2 merupakan bukan bilangan prima
      return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0 : # Bilangan memiliki faktor selain 1 dan dirinya sendiri
           return False
    return True 

#Input
num = int(input("Masukkan Bilangan  : "))
if is_prime(num):
    print(num,"<- Adalah bilangan prima!")
else:
    print(num,"<- Bukan bilangan prima (Komposit) !")
