from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView

from .models import Quote
from api.serializer import QuotesSerializers


class QuoteListView(ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuotesSerializers


class QuoteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuotesSerializers
