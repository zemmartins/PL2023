# TPC3: Processador de Pessoas listadas nos Róis de Confessados

# (publicado em 2023.02.28)

# Construa agora um ou vários programas Python para processar o texto 'processos.txt' (procurar o ficheiro no Bb) com o intuito de calcular frequências de alguns elementos (a ideia é utilizar arrays associativos, dicionários em Python, para o efeito) conforme solicitado a seguir:

#     a) Calcula a frequência de processos por ano (primeiro elemento da data); DONE

#     b) Calcula a frequência de nomes próprios (o primeiro em cada nome) e apelidos (o ultimo em cada nome) por séculos e apresenta os 5 mais usados;

#     c) Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.;

#     d) Converta os 20 primeiros registos num novo ficheiro de output mas em formato Json.


from collections import defaultdict
import re
import json

# A - Calcula a frequência de processos por ano (primeiro elemento da data);

def frequencia_ano(ficheiro) :
    anos_dict = dict() #ano->nr de processos  

    with open(ficheiro, 'r') as f:
        for linha in f :
            if len(linha.strip()) > 0:                
                string = linha.split('::')
                ano = string[1].split('-')[0]
                if ano not in anos_dict : 
                    anos_dict[ano] = 1
                else :
                    anos_dict[ano] += 1
    return anos_dict

def escrever_dicionario_em_ficheiro(dicionario, nome_ficheiro):
    with open(nome_ficheiro, 'w') as f:
        for chave, valor in dicionario.items():
            linha = f'{chave}: {valor}\n'
            f.write(linha)


#B - Calcula a frequência de nomes próprios (o primeiro em cada nome) e apelidos (o ultimo em cada nome) por séculos e apresenta os 5 mais usados;


def calcula_seculo(ano) : 
    if (int(ano[2])>0 or int(ano[3])>0) : 
        return int(ano[0])*10+int(ano[1])+1
    else : 
        return int(ano[0])*10+int(ano[1])


def frequencia_nomes_apelidos_por_seculo(ficheiro):
    nomes_por_seculo = defaultdict(lambda: defaultdict(int))  # dicionário aninhado: século -> nome -> frequência
    with open(ficheiro) as f:
        for linha in f:
            if len(linha.strip()) > 0:                
                partes = linha.strip().split("::")
                nome_completo = partes[2]
                ano_nascimento = partes[1].split("-")[0]
                primeiro_nome = nome_completo.split()[0]
                ultimo_nome = nome_completo.split()[-1]
                seculo = calcula_seculo(ano_nascimento)
                nomes_por_seculo[seculo][primeiro_nome] += 1
                nomes_por_seculo[seculo][ultimo_nome] += 1

    for seculo, nomes in nomes_por_seculo.items():
        print(f"---- Século {seculo} ----")
        nomes_ordenados = sorted(nomes.items(), key=lambda x: x[1], reverse=True)
        for nome, frequencia in nomes_ordenados[:5]:
            print(f"{nome}: {frequencia}")
        print("\n")

# C - Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.;

def freq_relacao (ficheiro) : 
    relacoes = dict.fromkeys(['primo', 'irmao', 'sobrinho', 'tio'], 0)
    with open(ficheiro) as f : 
        for linha in f : 
            if len(linha.strip()) > 0:
                if re.search(r"(?i:irmao)",linha) != None : 
                    relacoes["irmao"]+=1
                if re.search(r"(?i:primo)",linha) != None : 
                    relacoes["primo"]+=1
                if re.search(r"(?i:sobrinho)",linha) != None : 
                    relacoes["sobrinho"]+=1
                if re.search(r"(?i:tio)",linha) != None : 
                    relacoes["tio"]+=1
    return relacoes



# D - Converta os 20 primeiros registos num novo ficheiro de output mas em formato Json.

def convert_Json (ficheiro) :
    with open(ficheiro, 'r') as f:
        registos = []
        for i in range(20):
            linha = f.readline().strip()
            if linha:
                campos = linha.split('::')
                registo = {
                    'id': int(campos[0]),
                    'data': campos[1],
                    'nome': campos[2],
                    'pai': campos[3],
                    'mae': campos[4],
                    'outros': campos[5]
                }
                registos.append(registo)

    # escreve a lista de dicionários em um arquivo de saída no formato JSON
    with open('arquivo_de_saida.json', 'w') as f:
        f.write(json.dumps(registos, indent=4))
        
                        
def main () : 
    escolha = input("Por favor insira qual ação que pretende fazer:\nA -> Calcula a frequência de processos por ano (primeiro elemento da data);\nB -> Calcula a frequência de nomes próprios (o primeiro em cada nome) e apelidos (o ultimo em cada nome) por séculos e apresenta os 5 mais usados;\nC -> Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.;\nD - Converta os 20 primeiros registos num novo ficheiro de output mas em formato Json.\n")

    if (escolha=='A' or escolha == '1') : 
        dicionario_ordenado = dict(sorted(frequencia_ano("processos.txt").items()))
        print(dicionario_ordenado)
        escrever_dicionario_em_ficheiro(dicionario_ordenado,"resA.txt")
        print(dicionario_ordenado)

    elif (escolha=='B' or escolha=='2') : 
        frequencia_nomes_apelidos_por_seculo("processos.txt")

    elif (escolha=='C' or escolha=='3') : 
        print(freq_relacao("processos.txt"))
    
    elif (escolha=='D' or escolha=='d') : 
        convert_Json(("processos.txt"))

if __name__ == "__main__":
    main()