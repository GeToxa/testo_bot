import telebot
from config import Bot_token as BT
from telebot import types

bot = telebot.TeleBot(BT, parse_mode='None')

user = bot.get_me()

@bot.message_handler(commands=['start'])
def send_welcome(message):



	#Клавиатура для управления

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('Добавить задачу')
	item2 = types.KeyboardButton('Посмотреть задачи')
	markup.add(item1, item2)
	bot.reply_to(message, "Добро пожаловать в общий список дел по домашней бытовухе", reply_markup=markup)


A = ['1', '2']

def read_spisok(message):
	for i in A:
		data_messege = str(i)
		bot.send_message(message.chat.id, data_messege)

@bot.message_handler(content_types=['text'])
def main_act(message):
	if message.chat.type == 'private':
		bot.send_message(message.chat.id, 'Хорошо сейчас')
		if message.text == 'Добавить задачу':
			bot.send_message(message.chat.id, 'Добавляю задачу')
		elif message.text == 'Посмотреть задачи':
			read_spisok(message)


bot.polling(none_stop=True)