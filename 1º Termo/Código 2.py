from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# isso aqui só precisa para corrigir o bug
from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot("BusKredit", tagger_language=ENGSM)
