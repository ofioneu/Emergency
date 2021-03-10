import RPi.GPIO as gpio
import time
import requests


red = 24
buzz = 8
btn_input = 23

gpio.setmode(gpio.BCM)

gpio.setup(btn_input, gpio.IN, pull_up_down = gpio.PUD_DOWN)
#gpio.setup(btn_input, gpio.IN)
gpio.setup (red, gpio.OUT)
gpio.setup (buzz, gpio.OUT)

def send_msg(bot_message):
    
    bot_token = '1504361799:AAHPqbU2CVabYwQ58OpOO2zoBA90DPPrJJQ'
    bot_chatID = '-517025841'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def sos():
    while True:
        while gpio.input(btn_input) == 0:
            send_msg('Socorro!! Acionado botão em casa!')
            gpio.output (red,  1 )
            gpio.output (buzz,  1)
            time.sleep(1)
            gpio.output(red,0)
            gpio.output (buzz,  0)
            time.sleep(1)
            time.sleep(5)
        else:
            gpio.cleanup()
    
        time.sleep(1)
        

sos()
