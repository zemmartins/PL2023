import re


def main() : 
    levantar = input()

    if (levantar=="LEVANTAR") : 
        print('maq: "Introduza moedas."(formato "MOEDA 10c, 30c, 50c, 2e.")')

        moedas = input()
        
        matches = re.findall(r"MOEDA[S]?\s([\dce,.\s]+)", moedas)
        coins = []
        saldo = 0

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
    while True : 
        numero = input()

        if numero == "POUSAR" : 
            print('maq: "troco=' + str(saldo) + '; Volte sempre!"')
            return saldo
        
        elif re.match(r"T=(601|641)\d{6}",numero) != None and len(numero) == 9:
            print('maq: "Esse número não é permitido neste telefone. Queira discar novo número!"')
        
        elif re.match(r"T=(00)\d+",numero) != None and len(numero) == 9: 
            if saldo >= 1.5 :
                saldo -= 1.5
                print('maq: saldo = ' + str(saldo))
            else : 
                print('maq: "O seu saldo não é suficiente!"')

        elif re.match(r"T=(2)\d{8}",numero) != None and len(numero) == 9: 
            if saldo >= 0.25 : 
                saldo -= 0.25
                print('maq: saldo = ' + str(saldo))
            else :
                print('maq: "O seu saldo não é suficiente!"')

        elif re.match(r"T=(800)\d{6}",numero) != None and len(numero) == 9:
            print('maq: saldo = ' + str(saldo))

        elif re.match(r"T=(808)\d{6}",numero) != None and len(numero) == 9:
            if saldo >= 0.10 : 
                saldo -= 0.1
                print('maq: saldo = ' + str(saldo))
            else : 
                print('maq: "O seu saldo não é suficiente!"')

        else : 
            print('maq: "Numero indicado não existe!"')

        
if __name__ == "__main__":
    main()