import telebot
from cbrf import get_rates
from stocks import get_quotes
from nasa import get_ph_nasa


def main():
    token = "XXXXXXXXXXXXXXX"
    tb = telebot.TeleBot(token)
    tb.send_message(chat_id="832022014", text="Hello creator!")

##############################################################
    @tb.message_handler(commands=['start'])
    def do_start(message):
        tb.send_message(message.chat.id, "Отстаньте от меня, мои нейроны депрессии работают на полную катушку. Ладно, так и быть, что вам нужно?")

    @tb.message_handler(commands=['call'])
    def add(message):
        tb.send_message(message.chat.id, "Ну и зачем вы меня позвали? Я сегодня просто в отвратительном настроении")

    @tb.message_handler(commands=["rates"])
    def send_rates(message):
        tb.send_message(message.chat.id, get_rates("USD"))

    @tb.message_handler(commands=["quotes"])
    def send_quotes(message):
        for i in range(0, 7):
            quotes = get_quotes()[0][i] + " : " + str(get_quotes()[1][i])
            tb.send_message(message.chat.id, text=quotes)

    @tb.message_handler(commands=["nasa"])
    def send_ph_nasa(message):
        tb.send_photo(message.chat.id, get_ph_nasa()[0], caption=get_ph_nasa()[1])
        # (if everyone likes caption) tb.send_message(message.chat.id, get_ph_nasa()[2])
##########################################################################
    def echo(message):
        for m in message:
            if str(m.text[0]) != "/":
                tb.send_message(m.chat.id, text=m.text)


    tb.set_update_listener(echo)

    tb.polling(none_stop=True)

main()