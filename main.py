import telebot
from cbrf import get_rates
from stocks import get_quotes


def main():
    token = "874315279:AAG68XqWMCmLJ5-or4-A0NckcTHRDi7A4uE"

    tb = telebot.TeleBot(token)

    # tb.send_message(chat_id="832022014", text="Hello creator!")

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
        tb.send_message(message.chat.id, get_quotes())


    tb.polling(none_stop=True)

main()