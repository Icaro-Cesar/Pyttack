"""

    Título:     SubDomainEnum3377.py
    Autor:      Ícaro César
    Objetivo:   Realizar ataque de força bruta para descobrir possíveis subdomínios de um alvo.


"""
import requests     # Importa a biblioteca que irá nos permitir a realizar cada requisição HTTP, em busca de um subdomínio que dê match.
import pyfiglet     # Importa a biblioteca que irá nos permitir construir nosso Banner.
import time         # Importa a biblioteca de manipulação de tempo, por puro floreamento :-)

subDomainENum3377_banner = pyfiglet.figlet_format("Pyttack \n Five/Nive \nSubDomain \nEnumeration")     # O Desenvolvimento do Banner utilizando a biblioteca 'pyfiglet'.
print(subDomainENum3377_banner)

time.sleep(4)

protocolo = input("\nO alvo utiliza HTTP ou HTTPS? Digite o protocolo para a realização adequada da requisição. Ex.: http ou https -> ")
time.sleep(1)
alvo = input("\nDigite o domínio alvo para a execução do Sub-domain Brute-Force. Ex.: alvo.com -> ")
time.sleep(1)
wordlist = input("\nDigite o nome sua Wordlist (se estiver em outro diretório, descreva o caminho absoluto da Wordlist) -> ")
time.sleep(1)



sub_list = open(wordlist).read()		                     # É criada a variável 'sub_list' que recebe a ação do Python de lê o conteúdo da wordlist especificada.
subdoms = sub_list.splitlines()				                 # Força a quebra de linhas da lista, para melhor entendimento do Python, e cria uma variável que força receberá a lista no novo formato.

for sub in subdoms:					                        # Inicia um loop for, no qual 'sub' recebe cada subdomínio contendo em 'subdoms'
    bforce_subdomains = f"{protocolo}://{sub}.{alvo}"		# Aqui a variável 'bforce_subdomains' recebe os resultados da execução do loop for, onde cada subdomínio da wordlist é testada, 
                                                            # para o domínio  informado pelo usuário.

    try:
        user_agent = {'User-Agent': uagent}
        req = requests.get(bforce_subdomains)                                  # Aqui tratamos iniciamos uma exceção, solicitando ao Python para realizar as requisições Web, para cada 
        print("\n",req,"\n",req.status_code,"\n")                              # subdomínio testado pelo loop for que são valores da variável bforce_subdomains.
                                                                               # através de um script em Python. O User-Agent, fica em cargo do usuário introduzir.


    except requests.ConnectionError:
        pass                                                                   # Caso aconteça algum erro, não interromper a execução do programa.

    else:
        print("\n\n[+] Subdomínio Encontrado: ",bforce_subdomains, "[+]\n")    # Imprime na tela todos os subdomínios válidos encontrados no Brute-Force.
