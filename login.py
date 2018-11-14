def log(lista):
    while(True):
        Username = input("Unesi svoj username: ")
        if(len(Username)==0):print("Nisi uneo Username.")
        elif(Username not in lista):print("ovaj username nije u bazi podataka!")
        elif(Username in lista):
            Password = input("Unesi svoj password: ")
            if(len(Password) == 0):print("Nisi uneo Password.")
            elif(lista[Username] == Password):
                print("Uspesno ste se ulogovali")
                break
            elif(lista[Username]!=Password):print("Ova sifra neodgovara datom username-u!")