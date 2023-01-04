import telebot

CHAVE_API = "5373620947:AAEGYEbJQ1_8qGfJwrOWXuwWGeMwoUdKl7Y"

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
    

@bot.message_handler(commands=["MOriente"])
def MOriente(mensagem):
    bot.send_message(mensagem.chat.id, """
    Trajeto M  Oriente:

  Saida de M       Chegada em Oriente
              05:50         -       06:30
              06:50         -       07:30
              08:50         -       09:30
              11:20         -       12:00
              12:20         -       13:00
              14:50         -       15:30
              16:10         -       16:50
              16:50         -       17:30
              17:20         -       18:00
              18:20         -       19:00
              18:20         -       19:00""")


@bot.message_handler(commands=["MPompeia"])
def MPompeia(mensagem):
    bot.send_message(mensagem.chat.id, """
Trajeto Marília  X  Pompéia:
 
  Saída de Marília       Chegada em Pompéia
              05:50         -       06:50
              06:50         -       07:50
              08:50         -       09:50
              11:20         -       12:20
              12:20         -       13:20
              14:50         -       15:50
              16:10         -       17:10
              16:50         -       17:50
              17:20         -       18:20
              18:20         -       19:20
              18:20         -       19:20""")
    

@bot.message_handler(commands=["MPaulopolis"])
def MPaulopolis(mensagem):
    bot.send_message(mensagem.chat.id, """
Trajeto Marília  X  Paulópolis:
 
  Saída de Marília       Chegada em Paulópolis
              05:50         -       07:00
              06:50         -       08:00
              08:50         -       10:00
              12:20         -       13:30
              14:50         -       16:00
          	  16:50         -       18:00
              17:20         -       18:30
              18:20         -       19:30
              18:20         -       19:30""")


@bot.message_handler(commands=["MQuintana"])
def MQuintana(mensagem):
    bot.send_message(mensagem.chat.id,  """
Trajeto Marília  X  Quintana:
 
  Saída de Marília       Chegada em Quintana
              05:50         -       07:10
              06:50         -       08:10
              08:50         -       10:10
              12:20         -       13:40
              14:50         -       16:10
              16:50         -       18:10
              17:20         -       18:40
              18:20         -       19:40
              18:20         -       19:40""")
  

@bot.message_handler(commands=["MHerculandia"])
def MHerculandia(mensagem):
    bot.send_message(mensagem.chat.id,  """
Trajeto Marília  X  Padre Nóbrega:
 
         Saída de Marília       Chegada em Padre Nóbrega
              05:50         -       07:30
              06:50         -       08:30
              08:50         -       10:30
              12:20         -       14:00
              14:50         -       16:30
              16:50         -       18:30
              17:20         -       19:00
              18:20         -       20:00""")


@bot.message_handler(commands=["MT"])
def MT(mensagem):
    bot.send_message(mensagem.chat.id,  """
Trajeto Marília  X  Tupã:
 
  Saída de Marília       Chegada em Tupã
              05:50         -       07:50
              06:50         -       08:50
              08:50         -       10:50
              12:20         -       14:20
              14:50         -       16:50
              16:50         -       18:50
              17:20         -       19:20
              18:20         -       20:20""")
    
@bot.message_handler(commands=["THerculandia"])
def THerculandia(mensagem):
    bot.send_message(mensagem.chat.id,  """
Trajeto tupã  X  herculândia
 
        Saída de tupã             Chegada em herculândia: 
              04:50         -       05:10
              06:40         -       07:00
              08:00         -       08:20
              11:50         -       12:10
              14:00         -       14:20
              15:20         -       15:40
              17:30         -       17:50
              20:00         -       20:20""")
    
    
@bot.message_handler(commands=["TQuintana"])
def TQuintana(mensagem):
    bot.send_message(mensagem.chat.id,  """
Trajeto Tupã  X  Quintana:
 
  Saída de Tupã       Chegada em Quintana
              04:50         -       05:30
              —----         -       06:00
              06:40         -       07:20
              08:00         -       08:40
              11:50         -       12:30
              14:00         -       14:40
              15:20         -       16:00
              17:30         -       18:10
              20:00         -       20:40""")
    

@bot.message_handler(commands=["TPaulopolis"])
def TPaulopolis(mensagem):
    bot.send_message(mensagem.chat.id,  """
Trajeto Tupã  X  Paulópolis:
 
  Saída de Tupã       Chegada em Paulópolis
              04:50         -       05:40
              06:40         -       07:30
              08:00         -       08:50
              11:50         -       12:40
              14:00         -       14:50
              15:20         -       16:10
              17:30         -       18:20
              20:00         -       20:50 """)
    
    
@bot.message_handler(commands=["TPompeia"])
def TPompeia(mensagem):
    bot.send_message(mensagem.chat.id,  """
Trajeto Tupã  X  Pompéia:
 
  Saída de Tupã       Chegada em Pompéia
              04:50         -       05:50
              06:40         -       07:40
              08:00         -       09:00
              11:50         -       12:50
              14:00         -       15:00
              15:20         -       16:20
              17:30         -       18:30
              20:00         -       21:00""")
    

@bot.message_handler(commands=["TOriente"])
def TOriente(mensagem):
    bot.send_message(mensagem.chat.id,  """
Trajeto Tupã  X Oriente:
 
  Saída de Tupã      Chegada em Oriente
              04:50        -       06:10
              06:40        -       08:00
              08:00        -       09:20
              11:50        -       13:10
              14:00        -       15:20
		          15:20	       -	  	 16:40
              17:30        -       18:50
              20:00        -       21:20""")


@bot.message_handler(commands=["TPadreNobrega"])
def TPadreNobrega(mensagem):
    bot.send_message(mensagem.chat.id,  """
Trajeto Tupã  X Padre Nóbrega :
 
        Saída de Tupã              Padre Nóbrega
              04:50         -       06:20
              06:40         -       08:10
              08:00         -       09:30
              11:50         -       13:20
              14:00         -       15:30
              15:20         -       16:50
              17:30         -       19:00
              20:00         -       21:30""")
    

@bot.message_handler(commands=["TM"])
def TM(mensagem):
    bot.send_message(mensagem.chat.id,  """
 Trajeto Tupã  X Marília:
 
  Saída de Tupã      Chegada em Marília
              04:50        -       06:50
              06:40        -       08:40
              08:00        -       10:00
              11:50        -       13:20
              17:30        -       18:30
              20:00        -       22:00""")
    
@bot.message_handler(commands=["M"])
def M(mensagem):
    bot.send_message(mensagem.chat.id,  """
Terminal Rodoviário de Marília/SP, Av. Carlos Artêncio, 1001 - Fragata, Marília - SP, 17519-255

Tiradentes, 1081-1085 - Fragata, Marília - SP, 17519-100

Tiradentes, 277-355 - Jardim Tangara, Marília - SP

Ailton Barbearia, Av. Pres. Tancredo de Almeida Neves, 158 - Centro, Marília - SP, 17500-041

Praça São Miguel, Av. Castro Alves - Centro (Lácio), Marília - SP, 17539-022

Jardim Aquarius, Confiança Aquarius, Marília - SP

Jardim Aquarius, Hotel Trevellyn Marília - SP

Rod. Transbrasiliana, 4510 - Jóquei Clube, Marília - SP, 17521-460

R. Roberto Símonsen, 10-24 - Sítios de Recreio Letícia, Marília - SP

SP-294, Trevo da entrada de Marília - Padre Nóbrega, Marília - SP
""")


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
Selecione a cidade:

/M   - Márilia
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
