import re


def add_saldo(saldo) : 

    moedas = input()

    matches = re.findall(r"MOEDA[S]?\s([\dce,.\s]+)", moedas)
    coins = []

    for match in matches:
        coins = match.split(' ')
    str_saldo = ""
    for coin in coins:
        if coin == "1c":
            saldo += 0.01
        elif coin == "2c":
            saldo += 0.02
        elif coin == "5c":
            saldo += 0.05
        elif coin == "10c":
            saldo += 0.1
        elif coin == "20c":
            saldo += 0.2
        elif coin == "50c":
            saldo += 0.5
        elif coin == "1e":
            saldo += 1
        elif coin == "2e":
            saldo += 2
        else:
            str_saldo += coin + " - moeda inválida;"
    if str_saldo != "":
        print("maq: " + str_saldo + " saldo = " + str(saldo) + "€\n")
    else:
        print("maq: saldo = " + str(saldo) +  "€\n")
    
    return saldo


def calculo_troco(saldo) :

    moedas = list()

    while (saldo >= 0) :
        if (saldo-2>=0) :
            moedas.append("2e")
            saldo-=2 
        elif (saldo-1>=0) :
            moedas.append("1e")
            saldo-=1
        elif (saldo-0.5>=0) :
            moedas.append("50c")
            saldo-=0.5
        elif (saldo-0.2>=0) :
            moedas.append("20c")
            saldo-=0.2
        elif (saldo-0.1>=0) :
            moedas.append("10c")
            saldo-=0.1
        elif (saldo-0.05>=0) :
            moedas.append("5c")
            saldo-=0.05
        elif (saldo-0.02>=0) :
            moedas.append("2c")
            saldo-=0.02 
        elif (saldo-0.01>=0) :
            moedas.append("1c")
            saldo-=0.01  
        else : 
            break 
    
    return ' '.join(moedas)


def main() : 
    levantar = input()
    if (levantar != "LEVANTAR") : 
        print('maq : "O telefone continua pousado"')
        main()

    else : 
        print('maq: "Introduza moedas."(formato "MOEDA 10c, 30c, 50c, 2e.")')

        saldo = add_saldo(0)
        
       
    while True : 
        numero = input ('maq :"Se desejar inserir mais modedas deve escrever "MOEDAS", se pretende pousar escreva "POUSAR", os numeros deverão ser escritos no formato "T=xxxxxxxxx""\n')

        if numero == "POUSAR" : 
            print('maq: "troco=' + calculo_troco(saldo) + '; Volte sempre!"')
            return saldo

        elif numero == "MOEDAS" :
            print('maq: "Introduza moedas."(formato "MOEDA 10c, 30c, 50c, 2e.")')

            add_saldo(saldo)

        
        elif re.match(r"T=(601|641)\d{6}",numero) != None and len(numero) == 11:
            print('maq: "Esse número não é permitido neste telefone. Queira discar novo número!"')
        
        elif re.match(r"T=(00)\d+",numero) != None and len(numero)==11: 
            if saldo >= 1.5 :
                saldo -= 1.5
                print('maq: saldo = ' + str(saldo))
            else : 
                print('maq: "O seu saldo não é suficiente!"')

        elif re.match(r"T=(2)\d{8}",numero) != None and len(numero) == 11: 
            if saldo >= 0.25 : 
                saldo -= 0.25
                print('maq: saldo = ' + str(saldo))
            else :
                print('maq: "O seu saldo não é suficiente!"')

        elif re.match(r"T=(800)\d{6}",numero) != None and len(numero) == 11:
            print('maq: saldo = ' + str(saldo))

        elif re.match(r"T=(808)\d{6}",numero) != None and len(numero) == 11:
            if saldo >= 0.10 : 
                saldo -= 0.1
                print('maq: saldo = ' + str(saldo))
            else : 
                print('maq: "O seu saldo não é suficiente!"')

        else : 
            print('maq: "Numero indicado não existe!"')

        
if __name__ == "__main__":
    main()