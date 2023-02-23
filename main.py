import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Aqui está o link que deseja!{os.linesep}https://github.com/alexandrevisintainer{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} Teste{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} Aqui está o link que deseja!{os.linesep}https://proj-agencypage.vercel.app/#{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} Teste{os.linesep}')
    else:
        print(f'{os.linesep}{nome} Teste{os.linesep}')

def start():
    #Apresentar o chatbot
    print('Olá! Sou Alexandre Visintainer e bem vindo ao meu currículo')
    #Pedir o nome
    nome = input('Digite seu nome: ')

    while True:
        # Oferecer o menu de Opções
        resposta = input(
            f'O que gostaria de ver hoje?{os.linesep}[1] - GitHub{os.linesep}[2] - Projeto 1{os.linesep}[3] - Site da minha Agencia Web{os.linesep}[4] - Projeto 2{os.linesep}[5] - Projeto 3{os.linesep}')
        # Processr resposta enviada
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()   