from django.shortcuts import render
from rest_framework import generics, permissions
from allbanks.serializers import(
    NewBankSerializer
)

class NewBankAPIView(generics.CreateAPIView):
    serializer_class = NewBankSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)