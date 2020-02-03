from django.shortcuts import render
from rest_framework import generics
from .models import Currency
from .serializers import CurrencySerializer

class ListCurrencyView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer