import requests
import time
import json
import os

while True:
    token = '5227924277:AAFBO_SyXoNU-NGH7GmAZoFm82SWnox99Cs'
    # Ler mensagens
    url_base = f'https://api.telegram.org/bot{token}/getUpdates'
    resultado = requests.get(url_base)
    # Imprimir Resultados
    print(resultado.json())
    time.sleep(10)

class TelegramBot:
    def __init__(self):
        token = '1374813849:AAHauYQ2ikM4E-fTYOsZDNFZ-uOf39TecEM'
        url_base = f'https://api.telegram.org/bot{token}/getUpdates?timeout=100'
class TelegramBot:
    def __init__(self):
        token = '1374813849:AAHauYQ2ikM4E-fTYOsZDNFZ-uOf39TecEM'
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

bot = TelegramBot()
bot.Iniciar()