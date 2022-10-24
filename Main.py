from telebot import TeleBot
from random import randint

app = TeleBot("Main")
app.config['api_key'] = '5449097213:AAEGC40fY9ccfEPoTF_IIG-wX_Eod1ESl80'

winner = ''
number = None

@app.route('/command ?(.*)')
def command_handler(dict_message, cmd):
    id_chat = dict_message['chat']['id']
    print(dict_message)
    print(cmd)

    app.send_message(id_chat, f'Вы отправили команду: {cmd}\n{dict_message}')

@app.route('/start ?(.*)') # маршрут реакции, /start ЛЮБОЙ ТЕКСТ
def start_handler(dict_message, cmd):   # dict_message - словарь характеризующий чат, cmd - то, что подошло под регулярное выражение
    id_chat = dict_message['chat']['id'] # получение id чата
    msg = "Такой команды не существует."

    if cmd == "random":
        id_chat = dict_message['chat']['id']
        msg = f"Вы выиграли {randint(1,100)} рублей."

    app.send_message(id_chat, msg)  # отправка сообщения в конкретный чат

# Запуск бота
app.poll(debug=True)
