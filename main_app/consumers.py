import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            "type": "connection_established",
            "message": "You are now connected!"
        }))

    def receive(self, data):
        text_data_json = json.loads(data)
        message = text_data_json["message"]
        print("Message: ", message)