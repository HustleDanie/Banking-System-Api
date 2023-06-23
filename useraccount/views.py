from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from useraccount.serializers import(
    NewAccountSerializer,
    LogInSerializer,
    UpdateProfileSerializer,
    AllUserTransactionsSerializer,
    GetBalanceSerializer,
    AllMadeTransactionSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView
from useraccount.models import(
    CustomUser,
    UserTransactions
)

class NewAccountAPI(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = NewAccountSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class LogInAPI(TokenObtainPairView):

    serializer_class = LogInSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class UpdateProfileAPI(generics.RetrieveUpdateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateProfileSerializer


    def get_object(self):
        return self.request.user
    
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
class MakeTransactionsAPI(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AllUserTransactionsSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

class AllUserTransactions(generics.ListAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AllMadeTransactionSerializer
    

    def get_queryset(self):
        return UserTransactions.objects.all().filter(sender=self.request.user)
    
       
class DeleteUserAPI(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
class GetBalanceAPI(generics.RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GetBalanceSerializer

    def get_object(self):
        return self.request.user