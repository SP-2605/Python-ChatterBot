from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


def setup():
	chatbot = ChatBot('Bot',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	trainer='chatterbot.trainers.ListTrainer')

	for files in os.listdir('C:/Users/Suriya Prasath.S/Desktop\chatterbot-corpus-master\chatterbot-corpus\data\english/'):
		ConvData=open('C:/Users/Suriya Prasath.S/Desktop\chatterbot-corpus-master\chatterbot-corpus\data\english/' + files,encoding='latin-1' ).readlines()
		trainer=ListTrainer(chatbot)
		trainer.train(ConvData)
		#print('Training Completed')
setup()