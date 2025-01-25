import json
from django.core.management.base import BaseCommand
from channels.models import Channel


class Command(BaseCommand):
    help = 'Load channels from JSON file'

    def handle(self, *args, **kwargs):
        with open('channels_colombia.json', 'r', encoding="utf-8") as file:
            channels_data = json.load(file)
            for channel_data in channels_data['channels']:
                Channel.objects.create(
                    name=channel_data['name'],
                    logo=channel_data['logo'],
                    stream_url=channel_data['streamUrl']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded channels'))
