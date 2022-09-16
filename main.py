import telebot
from config import Bot_token as BT
from config import spisok_del
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



def read_spisok(message, spisok_del):
	for i in spisok_del:
		data_messege = str(i)
		bot.send_message(message.chat.id, data_messege)

@bot.message_handler(content_types=['text'])
def main_act(message):
#	if message.chat.type == 'private':
#		bot.send_message(message.chat.id, 'Хорошо сейчас')

	if message.text == 'Добавить задачу':
		bot.send_message(message.chat.id, 'Какую задачу Вы хотите добавить ?))')

	elif message.text == 'Посмотреть задачи':
		read_spisok(message, spisok_del)


@bot.message_handler(commands=['Добавить задачу'])
def main_act(message):
	new_message = message.text
	bot.send_message(message.chat.id, f'Вы добавили {new_message}')


bot.polling(none_stop=True)