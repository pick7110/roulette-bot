import random
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply


@respond_to("こんにちは")
def greeting_1(message):
    message.reply('こんにちは！！')

@listen_to("コニチワ")
def greeting_2(message):
    message.reply('コニチワ！！')

@respond_to("ping")
def response_3(message):
    message.reply('pong!')

@respond_to("roulette")
def response_1(message):
    res_list = ['山田','川田','スズキ','モリヤマ']
    message.reply(random.choice(res_list))
    
    