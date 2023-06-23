from django.urls import path
from useraccount.views import(
    NewAccountAPI,
    LogInAPI,
    UpdateProfileAPI,
    DeleteUserAPI,
    GetBalanceAPI,
    MakeTransactionsAPI,
    AllUserTransactions

)

urlpatterns = [
    path('new-account/', NewAccountAPI.as_view(), name='new-account'),
    path('login/',LogInAPI.as_view(), name='new-account'),
    path('update-account/', UpdateProfileAPI.as_view(), name='update-account'),
    path('delete-user/<int:pk>/',DeleteUserAPI.as_view(), name='delete-user'),
    path('user-balance/', GetBalanceAPI.as_view(), name='user-balance'),
    path('make-transactions/', MakeTransactionsAPI.as_view(), name='transactions'),
    path('user-transactions/', AllUserTransactions.as_view(), name='user-transactions')

]