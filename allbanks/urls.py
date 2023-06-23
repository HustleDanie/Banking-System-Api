from django.urls import path
from allbanks.views import(
    NewBankAPIView
)

urlpatterns =[
    path('create-bank/', NewBankAPIView.as_view(), name='create-bank')
]