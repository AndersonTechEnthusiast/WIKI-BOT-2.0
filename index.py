import wikipediaapi
import time
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import pyfiglet
from datetime import datetime
from colorama import init
from colorama import Fore
from unidecode import unidecode
import os
_CONTEUDO = []

hora = datetime.now().hour
# init(autoreset=True)
titulo = pyfiglet.figlet_format("WIKI-BOT 2.0")
print(titulo)

formalidade = None
if hora <= 12:
    formalidade = "☀️  Bom Dia \n"
elif hora > 12 and hora <= 18:
    formalidade = "🌤️  Boa Tarde \n"
elif hora > 18:
    formalidade = "🌙  Boa Noite \n"

welcome_system = f"👋 Olá \n"
pergunta_system = f"🚀  Para iniciarmos , 🏗️  gostaria de {Fore.GREEN}Custumizar{Fore.WHITE} seu uso \n 🤔  o que você prefere ❓ \n 💾 {Fore.CYAN}Memória Volátil 💾 \n\t ✅ {Fore.GREEN}Vantagens \n\t\t ✔️ {Fore.GREEN}  Economia de Memória Fixa \n\t\t ✔️ {Fore.GREEN}  Não cria documentos Terceiros \n\t ❌ {Fore.RED}Desvantagens \n\t\t ❗ {Fore.RED}Perca de Dados Após o Desligamento do Sistema \n\t\t ❗ {Fore.RED}Perca de Dados Caso o Sistema Pare de Funcionar {Fore.YELLOW}(usuário saiu do Terminal) \n 📀 {Fore.CYAN}Memória Fixa 📀 \n\t ✅  {Fore.GREEN} Vantagens \n\t\t ✔️   Desnecessariedade de requisições subsequentes após a primeira \n\t\t ✔️   Não faz requisições após o Desligamento do Sistema (só necessario um única requisição) \n\t ❌ {Fore.RED} Desvantagens \n\t\t ❗ {Fore.RED}Consumo de Memória do seu SSD {Fore.YELLOW} (Cria um Arquivo para Armazenar todas as requisções feitas da Internet) \n\t\t ❗ {Fore.RED}Arquivo Dependente Necessario {Fore.YELLOW} (Se o Arquivo for Deletado ou Corrompido , a Requisição será refeita) \n 🎯  {Fore.BLUE}Qual é a sua Escolha ?  🎯  \n\t 💾 {Fore.CYAN} Memória Volátil | {Fore.WHITE}Pressione {Fore.GREEN}[V] \n\t 📀 {Fore.CYAN}Memória Fixa | {Fore.WHITE}Pressione {Fore.GREEN}[F] \n"
for i in formalidade:
    time.sleep(.01)
    print(f"{i}",end="",flush=True)
    time.sleep(.01)
for i in welcome_system:
    time.sleep(.01)
    print(f"{i}",end="",flush=True)
    time.sleep(.01)
for i in pergunta_system:
    time.sleep(.01)
    print(f"{i}",end="",flush=True)
    time.sleep(.01)
Error = f"❌ {Fore.RED} Error ❌ \n"
Alerta = f"⚠️ {Fore.YELLOW} Alerta: Valor Inválido ⚠️\n "

pergunta_input = input(f"{Fore.WHITE}Tecla:")
while pergunta_input.lower() not in ['v','f']:
    if not pergunta_input:
        for i in Error:
            time.sleep(.01)
            print(f"{i}",end="",flush=True)
            time.sleep(.01)
        for i in Alerta:
            time.sleep(.01)
            print(f"{i}",end="",flush=True)
            time.sleep(.01)
        pergunta_input = input(f"{Fore.WHITE}Tecla:")
    else:
        for i in Error:
            time.sleep(.01)
            print(f"{i}",end="",flush=True)
            time.sleep(.01)
        for i in Alerta:
            time.sleep(.01)
            print(f"{i}",end="",flush=True)
            time.sleep(.01)
        pergunta_input = input(f"{Fore.WHITE}Tecla:")

if pergunta_input.lower() == "v":
    with open('ChatBox/Parametros.txt',"r",encoding="utf-8") as file:
        array = file.read().split() # transforma todos os parametros em arrays
        for i in tqdm(array,"Extraindo Informações"): # adiciona o carregamento no percorrimento da array
            paginas_wikipedia = requests.get(str(i)) # a cada laço pesquisa o link do Parametro que é representado pela variavel (i)
            soup = BeautifulSoup(paginas_wikipedia.text , 'html.parser') # configura o BeautifulSoup 
            titulo_span = soup.find("span",class_="mw-page-title-main") # busca pela tag html span com essa classe
            if titulo_span != None: 
                _CONTEUDO.append(titulo_span.get_text()) # Pega o Texto da tag capturada
    arquivo = "Historico.txt"
    def question():
        pergunta = input("Faça a sua Pergunta: ")
        for i in _CONTEUDO:
            if unidecode(i).lower() in unidecode(pergunta).lower():
                wiki = wikipediaapi.Wikipedia('BotAskQuestion','pt')
                conteudo = wiki.page(str(i))
                texto = conteudo.summary
                with open(arquivo , "a" , encoding="utf-8") as file:
                    file.write(f"\n\n{str(pergunta)}\n\n")
                    file.write(texto)
                for t in texto: 
                    time.sleep(.01)
                    print(f"{t}",end="",flush=True)
                    time.sleep(.01)
                break
    question()
    repeat = input("Quer Fazer outra pergunta ? (s/n)")
    while repeat.lower() not in ['s','n']:
        for i in Error:
            time.sleep(.01)
            print(f"{i}",end="",flush=True)
            time.sleep(.01)
        for i in Alerta:
            time.sleep(.01)
            print(f"{i}",end="",flush=True)
            time.sleep(.01)
        repeat = input("Quer Fazer outra pergunta ? (s/n)")
    while repeat == 's':
        question()
        repeat = input("Quer Fazer outra pergunta ? (s/n)")
elif pergunta_input.lower() == 'f':
    arquivo = "ChatBox.txt"
    Pasta = "ChatBox"
    if os.path.exists(f"{Pasta}/{arquivo}"):
        with open(f"{Pasta}/{arquivo}" , "r" , encoding="utf-8") as file:
            array = file.read().split(',')
            def question():
                pergunta = input("Faça a sua Pergunta: ")
                for i in array:
                    if unidecode(i).lower() in unidecode(pergunta).lower():
                        wiki = wikipediaapi.Wikipedia('BotAskQuestion','pt')
                        # # conteudo = wiki.page('Jesus Cristo')
                        conteudo = wiki.page(str(i))
                        texto = conteudo.summary
                        with open('Historico.txt' , 'a' , encoding="utf-8") as txt:
                            txt.write(f"\n\n {str(pergunta)}\n\n")
                            txt.write(f"{texto}")
                        for t in texto: 
                            time.sleep(.01)
                            print(f"{t}",end="",flush=True)
                            time.sleep(.01)
                        break
            question()
            repeat = input("Quer Fazer outra pergunta ? (s/n)")
            while repeat.lower() not in ['s','n']:
                for i in Error:
                    time.sleep(.01)
                    print(f"{i}",end="",flush=True)
                    time.sleep(.01)
                for i in Alerta:
                    time.sleep(.01)
                    print(f"{i}",end="",flush=True)
                    time.sleep(.01)
                repeat = input("Quer Fazer outra pergunta ? (s/n)")
            while repeat == 's':
                question()
                repeat = input("Quer Fazer outra pergunta ? (s/n)")
    elif not os.path.exists(f"{Pasta}/{arquivo}"):
        with open(f"{Pasta}/Parametros.txt" , "r", encoding="utf-8") as file:
            array = file.read().split()
            for i in tqdm(array,desc="Extraindo Informações"):
                wiki_paginas = requests.get(str(i))
                soup = BeautifulSoup(wiki_paginas.text , 'html.parser')
                titulos_span = soup.find('span',class_="mw-page-title-main")
                if titulos_span != None:
                    _CONTEUDO.append(titulos_span.get_text())
        if len(_CONTEUDO) > 0:
            with open(f"{Pasta}/{arquivo}" , "a" , encoding="utf-8") as file:
                for i in _CONTEUDO:
                    file.write(f"{str(i)},")
            with open(f"{Pasta}/{arquivo}" , "r" , encoding="utf-8") as file:
                keys_words = file.read().split(',')
                def question():
                    pergunta = input("Faça a sua Pergunta: ")
                    for i in keys_words:
                        if unidecode(i).lower() in unidecode(pergunta).lower():
                            wiki = wikipediaapi.Wikipedia('BotAskQuestion','pt')
                            # conteudo = wiki.page('Jesus Cristo')
                            conteudo = wiki.page(str(i))
                            texto = conteudo.summary
                            with open('Historico.txt' , "a" , encoding="utf-8") as file:
                                file.write(f"\n\n{str(pergunta)}\n\n")
                                file.write(texto)
                            for t in texto: 
                                time.sleep(.01)
                                print(f"{t}",end="",flush=True)
                                time.sleep(.01)
                            break
                question()
                repeat = input("Quer Fazer outra pergunta ? (s/n)")
                while repeat.lower() not in ['s','n']:
                    for i in Error:
                        time.sleep(.01)
                        print(f"{i}",end="",flush=True)
                        time.sleep(.01)
                    for i in Alerta:
                        time.sleep(.01)
                        print(f"{i}",end="",flush=True)
                        time.sleep(.01)
                    repeat = input("Quer Fazer outra pergunta ? (s/n)")
                while repeat == 's':
                    question()
                    repeat = input("Quer Fazer outra pergunta ? (s/n)")
        else:
            with open(f"{Pasta}/Parametros.txt" , "r", encoding="utf-8") as file:
                array = file.read().split()
                for i in array:
                    wiki_paginas = requests.get(str(i))
                    soup = BeautifulSoup(wiki_paginas.text , 'html.parser')
                    titulos_span = soup.find('span',class_="mw-page-title-main")
                    if titulos_span != None:
                        _CONTEUDO.append(titulos_span.get_text())
                    with open(f"{Pasta}/{arquivo}" , "a" , encoding="utf-8") as file:
                        for i in _CONTEUDO:
                            file.write(f"{str(i)},")
                    with open(f"{Pasta}/{arquivo}" , "r" , encoding="utf-8") as file:
                        keys_words = file.read().split()
                        def question():
                            pergunta = input("Faça a sua Pergunta: ")
                            for i in keys_words:
                                if i in pergunta:
                                    wiki = wikipediaapi.Wikipedia('BotAskQuestion','pt')
                                    # conteudo = wiki.page('Jesus Cristo')
                                    conteudo = wiki.page(str(i))
                                    texto = conteudo.summary
                                    with open(arquivo , "a" , encoding="utf-8") as file:
                                        file.write(f"\n\n{str(pergunta)}\n\n")
                                        file.write(texto)
                                    for t in texto: 
                                        time.sleep(.01)
                                        print(f"{t}",end="",flush=True)
                                        time.sleep(.01)
                                    break
                                # if i not in pergunta:
                                    # print("nenhum Resultando encontrado")
                        question()
                        repeat = input("Quer Fazer outra pergunta ? (s/n)")
                        while repeat.lower() not in ['s','n']:
                            for i in Error:
                                time.sleep(.01)
                                print(f"{i}",end="",flush=True)
                                time.sleep(.01)
                            for i in Alerta:
                                time.sleep(.01)
                                print(f"{i}",end="",flush=True)
                                time.sleep(.01)
                            repeat = input("Quer Fazer outra pergunta ? (s/n)")
                        while repeat == 's':
                                    question()
                                    repeat = input("Quer Fazer outra pergunta ? (s/n)")