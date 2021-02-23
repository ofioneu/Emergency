from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import requests
import json

app = Flask(__name__)
api = Api(app)

def send_msg(bot_message):
    
    bot_token = '1504361799:AAHPqbU2CVabYwQ58OpOO2zoBA90DPPrJJQ'
    bot_chatID = '-596270661'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

class Help(Resource):
    def post(self):
        if request.method == 'POST':
            parser = reqparse.RequestParser()
            parser.add_argument('socorro')
            dados = parser.parse_args()
            if dados['socorro'] == '1':
                print('SOCORRO!!!!')
                return send_msg("Socorro!"), 200
            else:
                print("Suave")
                return send_msg("Pedido de socorro CANCELADO!!"), 200


class Url(Resource):
    def post(self):
        if request.method == 'POST':
            parser = reqparse.RequestParser()
            parser.add_argument('url')
            parser.add_argument('help')
            dados = parser.parse_args()
            with open('urls.json', 'w') as f:
                data ={
                   'servUrl': dados['url'],
                    'servHelp':dados['help']
                }
                json.dump(data, f, indent=4)
            return 200
    
    def get(self):
        if request.method == 'GET':
            with open('urls.json', 'r') as f:
                data = json.load(f)
                print(data)
                return data, 200
        else:
            print('Error')
            return 504

api.add_resource(Help, '/help')
api.add_resource(Url, '/url')



if __name__ == '__main__':
    app.run(port=19002, host='0.0.0.0', debug = True)