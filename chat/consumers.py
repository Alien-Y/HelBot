import json
from channels.generic.websocket import WebsocketConsumer
from .ai_model.chat import response


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        answer = response(message)

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': answer
        }))