import telebot

API_TOKEN = '5373620947:AAEGYEbJQ1_8qGfJwrOWXuwWGeMwoUdKl7Y'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    partida = """
    Selecione o Trajeto:

    /MPadreNobrega  -  Marília x Padre Nóbrega
    /MOriente	      -  Marília x Oriente
    /MPompeia       -  Marília x Pompeia
    /MPaulopolis    -  Marília x Paulopolis
    /MQuintana      -  Marília x Quintana
    /MHerculandia   -  Marília x Tupam
    /MT

    /THerculandia   -  Tupã   x  Herculandia
    /TQuintana      -  Tupã   x  Quintana
    /TPaulopolis    -  Tupã   x  Paulopolis
    /TPompeia       -  Tupã   x  Pompeia
    /TOriente       -  Tupã   x  Oriente
    /TPadreNobrega  -  Tupã   x  Padre nobrega
    /TM             -  Tupã   x  Marília"""
    bot.send_message(mensagem.chat.id, partida)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, """"
R$30,00  -  https://nubank.com.br/pagar/1bzgs1/gsi7JSdo9H
R$50,00  -  https://nubank.com.br/pagar/1bzgs1/ZH2v0lggeq
R$75,00  -  https://nubank.com.br/pagar/1bzgs1/oFAHqg4d47
R$100,00 -  https://nubank.com.br/pagar/1bzgs1/G56LtVCHC6
R$125,00 -  https://nubank.com.br/pagar/1bzgs1/wrrZ2uAK55
R$150,00 -  https://nubank.com.br/pagar/1bzgs1/Paa40r4etg
R$200,00 -  https://nubank.com.br/pagar/1bzgs1/tKuVhJ7lD8""")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, """
Selecione a cidade de partida:

/M   - Marilia
/N   - Padre Nóbrega
/O   - Oriente
/P   - Pompéia
/Pa  - Paulópolis
/Q   - Quintana
/T   - Tupâ""")

    @bot.message_handler(commands=["M"])
    def M(mensagem):
        bot.send_message(mensagem.chat.id, """
    Selecione a cidade de partida:

    /M   - Marilia
    /N   - Padre Nóbrega
    /O   - Oriente
    /P   - Pompéia
    /Pa  - Paulópolis
    /Q   - Quintana
    /T   - Tupâ""")



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    teto = """
Escolha uma opção para continuar:

/opcao1   Horário dos Ônibus
/opcao2   Recarga de Cartão
/opcao3   Pontos de Parada"""
    bot.reply_to(mensagem, teto)

bot.polling()
