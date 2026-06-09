from rest_framework import viewsets
from items.models import Item
from items.serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.query.all() if hasattr(Item, 'query') else Item.objects.all().order_by('-created_at')
    serializer_class = ItemSerializer
