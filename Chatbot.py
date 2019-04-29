from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

ChatBot=ChatBot('Bot')
trainer=ListTrainer(ChatBot)

while True:
	message = input('You: ')
	if message.strip() != 'Bye':
		reply = ChatBot.get_response(message)
		print('ChatBot: ', reply)
	if message.strip() == 'Bye':
		print('ChatBot:Bye')
		break
