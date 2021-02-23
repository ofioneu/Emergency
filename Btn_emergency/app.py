#! /usr/bin/python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as gpio
import time

import requests
import json
from threading import Thread
 
gpio.setmode(gpio.BCM)

# Com pull-up interno
gpio.setup(23, gpio.IN, pull_up_down = gpio.PUD_UP)
# definir uma porta / pino como saída   
gpio.setup (24, gpio.OUT)
gpio.setup (25, gpio.OUT)


def send_msg(bot_message):
    
    bot_token = '1504361799:AAHPqbU2CVabYwQ58OpOO2zoBA90DPPrJJQ'
    bot_chatID = '-517025841'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def check():
    bot_token = '1504361799:AAHPqbU2CVabYwQ58OpOO2zoBA90DPPrJJQ'
    send_check = 'https://api.telegram.org/bot'+bot_token+'/getUpdates'
    while True:
        print('Check function')
        try:
            response = requests.get(send_check)
            data=response.json() 
        except:
            gpio.output (25,  0)
        finally:       
            if data['ok'] == True:
                gpio.output (25,  1)
                time.sleep(1)
                gpio.output (25,  0)
                time.sleep(1)
    
def emergency():
    while True:
        print('Emergency function')
        if gpio.input(23) == gpio.LOW:
            while True:
                send_msg('Socorro!! Acionado botão em casa!')
                gpio.output (24,  1 )
                time.sleep(1)
                gpio.output(24,0)
                time.sleep(9)
                
        else:
            #check()
            pass
    
        time.sleep(3)

tcheck=Thread(target=check)
temergency=Thread(target=emergency)
temergency.start()
tcheck.start()
#gpio.cleanup()

