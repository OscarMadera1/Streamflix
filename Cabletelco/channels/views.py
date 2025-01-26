# Create your views here.
from rest_framework import viewsets
from .models import Channel
from .serializers import ChannelSerializer


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
