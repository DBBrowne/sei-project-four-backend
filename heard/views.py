from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import HeardEvent
from .serializers import HeardEventSerializer

class EventListView(ListCreateAPIView):
    queryset = HeardEvent.objects.all()
    serializer_class = HeardEventSerializer

class EventDetailView(RetrieveUpdateDestroyAPIView):
    queryset = HeardEvent.objects.all()
    serializer_class = HeardEventSerializer