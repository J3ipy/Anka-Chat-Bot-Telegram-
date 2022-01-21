import requests
import time
import json
import os


class TelegramBot:
    def __init__(self):
        token = '5281960165:AAHFhdDjKhTHAIt_rh1xKdVVaN7RIalR6c4'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('menu', 'Menu'):
            return f'''Olá bem vindo ao meu primeiro Bot com python. {os.linesep}Digite o número para eu realizar um comando:{os.linesep}1 - Qual é o seu nome?{os.linesep}2 - Música favorita{os.linesep}3 - Filmes {os.linesep}4 - Animes {os.linesep}5- Séries {os.linesep}6 - Meus Desenhos '''
        if mensagem == '1':
            return f'''Oi, meu nome é Anka, prazer em te conhecer :) {os.linesep} {os.linesep} Continuar mexendo no Bot?(s/n)
            '''
        elif mensagem == '2':
            return f'''Vou deixar o link da minha música fav, só porque estou humilde hoje - https://youtu.be/nmjdaBaZe8Y {os.linesep} {os.linesep} Continuar mexendo no Bot?(s/n)
            '''
        elif mensagem == '3':
            return f'''Lista de alguns Filmes que eu recomendo: {os.linesep} {os.linesep} - Django Livre{os.linesep} - Her {os.linesep} - Star Wars {os.linesep} - Rede Social: o Filme {os.linesep} - Eu, Robô ( Esse é o meu favorito :) ) {os.linesep} {os.linesep} Os sites que eu encontrei são cheios de propagandas, desculpa não tenho como recomendar um ótimo site para você, perdão :( {os.linesep} {os.linesep} Continuar mexendo no Bot?(s/n)'''

        elif mensagem == '4':
            return f'''Lista de alguns Animes que eu recomendo: {os.linesep} {os.linesep} - Evangelion Neo Genesis{os.linesep} - HxH {os.linesep} - Attack on Titan {os.linesep} - Akira {os.linesep} - Naruto {os.linesep}{os.linesep} Assistam esses animes que eu recomendei aqui nesse site: https://betteranime.net/animes {os.linesep} {os.linesep} Continuar mexendo no Bot?(s/n)'''

        elif mensagem == '5':
            return f'''Lista de algumas Séries que eu recomendo: {os.linesep} {os.linesep} - Mr. Robot{os.linesep} - The end of the fucking world {os.linesep} - Black mirror {os.linesep} - Demolidor {os.linesep} - Vikings {os.linesep} {os.linesep}*Vocês podem assistir no meu amigo bot de séries: @TuaSerieBot {os.linesep} {os.linesep} Continuar mexendo no Bot?(s/n)'''

        if mensagem == '6':
            return f'''Hmm, só vou deixar vc dar uma olhadinha :) {os.linesep} https://drive.google.com/file/d/1M8w_AU8hasHUgPQjx-SPsxpUqbRoJHmO/view?usp=sharing {os.linesep} {os.linesep} Continuar mexendo no Bot?(s/n)
            '''
        

        elif mensagem.lower() in ('s', 'sim'):
            return ''' Fico feliz com sua companhia! '''
        elif mensagem.lower() in ('n', 'não'):
            return ''' Poxa, nós vemos em uma próxima oportunidade ;( '''
        else:
            return 'Gostaria de acessar o meu menu? Digite "menu"'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()