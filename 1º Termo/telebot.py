import telebot

CHAVE_API = "AAGtYfPJfyil5EM8ED18PEH-2DXoNQjUg3Q"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["MPadreNobrega"])
def MPadreNobrega(mensagem):
    bot.send_message(mensagem.chat.id, """
Trajeto Marília  X  Padre Nóbrega:
 
  Saída de Marília       Chegada em Padre Nóbrega
              05:50         -       06:20
              06:50         -       07:20
              08:50         -       09:20
              11:20         -       11:50
              12:20         -       12:50
              14:50         -       15:20
              16:10         -       16:40
              16:50         -       17:20
              17:20         -       17:50
              18:20         -       18:50
              18:20         -       18:50""")
    


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    partida = """
    Selecione o Trajeto:
                        marilia
                        nobrega
                        oriente
                        pomepia"""
    bot.send_message(mensagem.chat.id, partida)
    while True:
        def opcao1(mensagem):
            chegada= """
                        Selecione o Trajeto:
                                            marilia
                                            nobrega
                                            oriente
                                            pomepia"""

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Ainda não tem essa função")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu!  mandou um abraço de volta")



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