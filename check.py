import requests
import json
import time
import RPi.GPIO as gpio

green = 25
gpio.setmode(gpio.BCM)
gpio.setup (green, gpio.OUT)



while True:
    try:
        bot_token = '1504361799:AAHPqbU2CVabYwQ58OpOO2zoBA90DPPrJJQ'
        send_check = 'https://api.telegram.org/bot'+bot_token+'/getUpdates'
        response = requests.get(send_check)
        data=response.json()
        if data['ok'] == True:
            gpio.output (green,  1)
            time.sleep(0.5)
            gpio.output (green,  0)
            time.sleep(0.5)
        else:
            gpio.output (green,  0)
    except Exception as e:
        gpio.output (green,  0)
    finally:   
        gpio.output (green,  0)
    time.sleep(3)