# from django.shortcuts import render
# from rest_framework import viewsets
# from .serializers  import QuoteSerializer
# from .models import Quote
# # Create your views here.


# class QuoteViewSet(viewsets.ModelViewSet):
#     queryset = Quote.objects.all()
#     serializer_class = QuoteSerializer

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import QuoteSerializer
from .models import Quote
import random

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    @action(detail=False, methods=['get'], url_path='random')
    def get_random_quote(self, request):
        count = self.queryset.count()
        if count == 0:
            return Response({'message': 'No quotes available'}, status=404)
        random_quote = self.queryset[random.randint(0, count - 1)]
        serializer = self.get_serializer(random_quote)
        return Response(serializer.data)
