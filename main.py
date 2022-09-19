import telebot
from config import Bot_token as BT
from config import spisok_del, help_notification, slovar_del
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
	item3 = types.KeyboardButton('Удалить задачу')
	markup.add(item1, item2, item3)

	# Ответы

	bot.reply_to(message, f"Добро пожаловать {user_name}. Этот бот составляет общий список дел. Теперь все записано",
				 reply_markup=markup)

	bot.send_message(message, "Для вызова справки напишите слово 'Cправка'")




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

	if message.text == 'Cправка':
		bot.send_message(message.chat.id, help_notification)

	if message.text == 'Удалить задачу':

		del_choise = bot.send_message(message.chat.id, 'Напишите номер задачи которую хотите удалить)')
		bot.register_next_step_handler(del_choise, chose_to_del)

def chose_to_del(message):
	try:
		del_number = message.text
		del_number = int(del_number)
		del_number = del_number - 1
		element = slovar_del[del_number]
		spisok_del.remove(element)
	except ValueError:
		bot.send_message(message.chat.id, 'Вы ввели не число')
	else:
		bot.send_message(message.chat.id, f'Задача {slovar_del[del_number]} удалена')


def new_msg_handler_add(message):

	new_message_add = message.text
	spisok_del.append(new_message_add)

	last_task = chek_len()

	last_task = last_task[-1]
	bot.send_message(message.chat.id, f'Вы добавили задачу {last_task}:  {new_message_add}')

	for i in range(len(spisok_del)):
		slovar_del[i] = spisok_del[i]

def chek_len():
	all_tasks = len(spisok_del)
	np_spis_add = []
	for i in range(all_tasks):
		np_spis_add.append(i+1)
	return np_spis_add

def read_spisok(message, spisok_del):

	for i in range(len(spisok_del)):
		stroka = f'{i+1}: {slovar_del[i]}'
		bot.send_message(message.chat.id, stroka)


bot.polling(none_stop=True)