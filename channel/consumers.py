import json

from channels.generic.websocket import AsyncWebsocketConsumer
from .models import *

from asgiref.sync import sync_to_async

@sync_to_async
def save_message(text_data_json):
    newMessage = Message(id_to_channel=text_data_json['channel_id'],
                             content=text_data_json['message'],
                             user=text_data_json['user'])
    newMessage.save()

    return newMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        print(self.room_name)
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_receive)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        self.msg = await save_message(text_data_json)

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    async def chat_message(self, event):
        context = {
            'user': self.msg.user,
            'message': self.msg.content,
            'date': f"{self.msg.date.day}/{self.msg.date.month}/{self.msg.date.year}",
        }
        message = event["message"]
        await self.send(text_data=json.dumps(context))