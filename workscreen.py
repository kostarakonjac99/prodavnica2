#moji fajlovi
import login
import registracija
import kupac
import prodavac
#promenljive
prodavaci = {"prodavac":"admin123"}
kupci = {}
prod = False
print("IT SHOP")
#Loop za registrovanje i logovanje na sistem
while(True):
    odg1= input("1)Login\n2)Registracija\n3)pomoc: ")
    if(odg1 =="1"):
        odg2 = input("Da li zelis da se ulogujes kao kupac ili prodavac(1/2)?: ")
        if(odg2=="1"):
            with open("kupci","r") as kupc:
                for line in kupc:
                    Username = line.split("-")[0]
                    Password =(line.split("-")[1]).split("\n")[0]
                    kupci[Username]=Password
            login.log(kupci)
            break
        elif(odg2=="2"):
            login.log(prodavaci)
            prod = True
            break
        else:print("Uneo si neodgovarajucu vrednost")
    elif(odg1=="2"):registracija.reg(kupci)
    elif(odg1 == "3"):
        with open("Upustvo","r") as tut:
            for line in tut:print(line)
    else:print("Uneli ste neodgovarajucu vrednost, pokusajte ponovo.")
#proveravanje da li je korisnik prodavac ili kupac
if(prod==True):prodavac.main()
else:#loop za kupca
    while(True):
        try:
            balans = int(input("Unesi koliko novca imas: "))
            if(balans<=0):print("Balans mora biti pozitivan broj!")
            else:break
        except ValueError:print("Uneta je neodgovarajuca vrednost")
    kupac.main(balans)