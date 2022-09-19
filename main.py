import telebot
from config import Bot_token as BT
from config import spisok_del
from telebot import types

bot = telebot.TeleBot(BT, parse_mode='None')

user = bot.get_me()

@bot.message_handler(commands=['start'])
def send_welcome(message):


	user_name = message.from_user.first_name

	#Клавиатура для управления

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('Добавить задачу')
	item2 = types.KeyboardButton('Посмотреть задачи')
	markup.add(item1, item2)

	# Ответы

	bot.reply_to(message, f"Добро пожаловать {user_name}. Этот бот составляет общий список дел. Теперь не увернуться от дел!",
				 reply_markup=markup)

	bot.send_message(message, "Для вызова справки напишите слово 'справка'")


def read_spisok(message, spisok_del):
	for i in spisok_del:
		data_messege = str(i)
		bot.send_message(message.chat.id, data_messege)

@bot.message_handler(content_types=['text'])
def main_act(message):

#	if message.chat.type == 'private':
#		message_non = message.text
#		bot.send_message(message.chat.id, f'Такой задачи нет {message_non}')

	if message.text == 'Добавить задачу':
		add_choise = bot.send_message(message.chat.id, 'Какую задачу Вы хотите добавить ?))')

		bot.register_next_step_handler(add_choise, new_msg_handler_add)

	if message.text == 'Посмотреть задачи':
		read_spisok(message, spisok_del)

def new_msg_handler_add(message):

	new_message_add = message.text
	spisok_del.append(new_message_add)
	bot.send_message(message.chat.id, f'Вы добавили: {new_message_add}')


bot.polling(none_stop=True)




