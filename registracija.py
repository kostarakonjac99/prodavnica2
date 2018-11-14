import sys
def reg(lista):
    brojac = 0
    while(True):
        with open("kupci","r") as kupc:
            for line in kupc:brojac = brojac+2
        Username = str(input("Unesi svoj username(q za izlaz): "))
        if(Username in lista):print("Ovaj username vec postoji pokusajte ponovo!")
        elif(Username == "q"):sys.exit()
        else:
            Password = str(input("Unesi svoj password: "))
            if(len(Password)==0):print("Niste uneli sifru")
            else:
                with open("kupci","a") as kupac:
                    usrpsw = Username+"-"+Password
                    if(brojac == 0):kupac.write(usrpsw)
                    else:kupac.write("\n"+usrpsw)
                print("Uspesno ste se registrovali, ponovo pokreni program kako bi se ulogovao.")
                asd = input("")
                sys.exit()


