import sys
def main():
    uslov = True
    while(uslov == True):
        odg = input("Da li zelis da nastavis(d/n): ")
        if(odg == "d" or odg == "D"):
            fun = input("Unesi broj funkcije koju zelis da izvrsis\n1)budzet\n2)knjiga utisaka\n3)edit\n: ")
            if(fun == "1"):
                with open("budzet prodavca","r")as budzet:
                    sum = 0
                    for line in budzet:
                        sum = sum+int(line.split("\n")[0])
                print(sum)
            if(fun == "2"):
                with open("utisci","r") as utisak:
                    brojac = 1
                    zbir = 0
                    for line in utisak:
                        print(line)
                        zbir = zbir + float(line.split("-")[1])
                        brojac = brojac+1
                    print("Prosek: "+str(zbir/brojac))
            if(fun == "3"):
                odg1 = input("Unesi broj fajla koji zelis za izmenis:\n1)magacin\n2)akcije\n: ")
                if(odg1 == "1"):
                    vrsta = input("Da li zelis da zadrsis stari magacin i da ubacis novi proizvod ili da napravis novi magacin(1/2): ")
                    if(vrsta == "1"):
                        brIzmn = 0
                        cen = 0
                        with open("magacin","a")as mag:
                            brojacLen = 0
                            with open("magacin","r") as mag1:
                                for line in mag1:
                                    brojacLen = brojacLen+1
                            while(True):
                                try:
                                    brIzmn = int(input("Unesi koliko izmena zelis da uneses: "))
                                    if(brIzmn<=0):print("Moras uneti pozitivnu vrednost")
                                    else:break
                                except ValueError:print("Uneo si pogresnu vrednost")
                            for i in range(brIzmn):
                                while(True):
                                    IzmnProd = input("Unesi proizvod koji zelis da dodas: ")
                                    if(len(IzmnProd)==0):break
                                    else:
                                        while(True):
                                            try:
                                                cen = int(input("Unesi cenu ovog proizvoda"))
                                                if(cen <=0):print("Moras uneti pozitivan broj da bi nastavio!")
                                                elif(cen > 0 and brojacLen >0):
                                                    mag.write( "\n"+IzmnProd+"-"+str(cen))
                                                    break
                                                elif (cen > 0 and brojacLen == 0):
                                                    mag.write(IzmnProd + "-" + str(cen)+"\n")
                                                    break
                                            except ValueError:print("Uneo si neodgovarajucu vrednost")
                                        break
                    elif(vrsta=="2"):
                        while(True):
                            try:
                                broj = int(input("Unesi broj proizvoda kojih zelis da ubacis u magacin: "))
                                if(broj<=0):print("Moras da uneses pozitivan broj!")
                                else:break
                            except ValueError:print("Uneo si neodgovarajucu vrednost")
                        with open("magacin","w") as mag2:
                            for i in range(broj):
                                cenaPro = 0
                                proizvod = str(input("Unesi naziv proizvoda: "))
                                while(True):
                                    try:
                                        cenaPro = int(input("unesi cenu proizvoda: "))
                                        if(cenaPro<=0): print("cena mora da bude broj veci od 0!")
                                        else:break
                                    except ValueError:print("Unesena je neodgovarajuca vrednost!")
                                if (i == 0):mag2.write(proizvod+"-"+str(cenaPro))
                                else:mag2.write("\n"+proizvod+"-"+str(cenaPro))
                    else:print("Uneo si neodgovarajucu vrednost")
                if(odg1 == "2"):
                    with open("akcije","a") as akc:
                        brAkc = 0
                        while(True):
                            try:
                                brAkc = int(input("Unesi koliko linija zelis da napises u akcijama"))
                                if(brAkc <=0):print("Moras barem jednu liniju da napises!")
                                else:break
                            except ValueError:print("Uneo si neodgovarajucu vrednost!")
                        for i in range(brAkc):
                            akcija = input("Unesi akciju: ")
                            akc.write(akcija+"\n")
        elif(odg == "n" or odg == "N"):sys.exit()
        else:print("Uneo si neodgovarajucu vrednost")