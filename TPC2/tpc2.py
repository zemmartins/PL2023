import sys

class soma :

    def __init__ (self) :
        self.estado = "off"
        self.total = 0 


    # Exercicio 1

    def sum_text (self,string : str) : 
        i = 0 
        while i<len(string) : 
            if string[i].isdigit() : 
                lista = list()
                lista.append(string[i]) # poe na primeira pos o numero inicial
                i+=1
                while(i<len(string) and string[i].isdigit()) : 
                    lista.append(string[i])
                    i+=1
                tamanho = len(lista)
                total = 0 
                for x in lista : 
                    total += int(x) * 10**(tamanho-1)
                    tamanho -= 1
                if self.estado == "on" :
                    self.total += total
            elif string[i].lower() == 'o' : 
                i+=1
                if (string[i].lower() == 'f') : 
                    i+=1
                    if (string[i].lower() == 'f') : 
                        i+=1
                        self.estado = "off"
                elif (string[i].lower() == 'n') : 
                    i+=1
                    self.estado = "on"
            elif string[i] == '=' : 
                i+=1
                print(self.total)
            else : 
                i+=1
        return self.total

    # Exercicio 2

    def read_stdin(self) : 
        return (self.sum_text(input()))

    # Exercicio 3
    # feitos no sum_text




def main () : 
    sum = soma()
    sum.read_stdin()

if __name__ == "__main__":
    main()