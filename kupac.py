import sys
def main(novac):
    uslov1 = True
    korpa = []
    cenaKorpe = []
    while(uslov1 == True):
        odg = input("Da li zelis da nastavis(d/n):")
        if(odg == "d" or odg == "D"):
            fun = input("Unesi broj funkcije koju zelis da izvrsis\n0)provera akcija\n1)Magacin\n2)Korpa\n3)Izbaci\n4)Kupovina\n5)Balans\n6)Knjiga utisaka\n7)Izlaz\n: ")
            #akcije
            if(fun =="0"):
                with open("akcije","r") as akc:
                    brojac1 = 0
                    for line in akc:
                        print(line)
                        brojac1 = brojac1+1
                    if(brojac1==0):print("Trenutno nema akcija")
            #magacin
            if(fun == "1"):
                with open("magacin", "r") as mag:
                    for line in mag:
                        print(line)
            #korpa
            if (fun == "2"):
                brojack = 0
                proizvodi = {}
                with open("magacin", "r")as mag1:
                    for line in mag1:
                        proizvod = line.split("-")[0]
                        cena = (line.split("-")[1]).split("\n")[0]
                        proizvodi[proizvod] = int(cena)
                while(True):
                    try:
                        brojack = int(input("Unesi koliko proizvoda zelis da ubacis u korpu: "))
                        if(brojack<=0):print("Moras uneti pozitivan broj!")
                        else:
                            while(brojack != 0):
                                art = input("Unesi proizvod koji zelis da stavis u kopru: ")
                                if (art not in proizvodi):
                                    print("Taj proizvod se ne nalazi u nasem magacinu!")
                                else:
                                    korpa.append(art)
                                    cenaKorpe.append(proizvodi[art])
                                    brojack = brojack - 1
                            print("korpa:", korpa)
                            print("ukupna cena", sum(cenaKorpe))
                        break
                    except ValueError:print("Unesena je neodgovarajuca vrednost!")
            #izbacivanje
            if(fun == "3"):
                uljez = input("Unesi proizvod koji zelis da izvadis iz korpe: ")
                if(len(korpa)==0):print("U korpi nemate nista.")
                elif(uljez not in korpa):print("Ovaj proizvod nije u korpi")
                else:
                    cenaKorpe.remove(cenaKorpe[korpa.index(uljez)])
                    korpa.remove(uljez)
            #kupovina
            if(fun == "4"):
                if(sum(cenaKorpe)>novac):print("Nemate dovoljno novca da kupite sve iz korpe, molimo vas da izbacite nesto.")
                elif(len(korpa)==0):print("U korpi nemate nista.")
                else:
                    print("Svi proizvodi su kupljeni!")
                    korpa = []
                    novac = novac - sum(cenaKorpe)
                    with open("budzet prodavca","a")as budzet:
                        budzet.write(str(sum(cenaKorpe))+"\n")
                    cenaKorpe = []
                    print(korpa)
                    print(novac)
            #provera racuna
            if(fun == "5"):print(novac)
            #knjiga utisaka
            if(fun=="6"):
                with open("utisci.txt","a") as ut:
                    utisak = input("Unesi svoj utisak o nasoj prodavnici: ")
                    while(True):
                        try:
                            ocena = float(input("Unesi svoju ocenu(1-10): "))
                            if(ocena <=0 or ocena >10):print("Moras da uneses ocenu izmedju 1 i 10")
                            else:break
                        except ValueError:print("Uneta je pogresna vrednost")
                    ut.write(utisak+", ocena: "+str(ocena))
            #izlaz
            if(fun == "7"):sys.exit()
        elif(odg == "n" or odg == "N"):uslov1 = False
        else:print("Uneta je neodgovarajuca vrednost")