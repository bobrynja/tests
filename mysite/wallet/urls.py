from django.urls import path, include
from . import views
 
urlpatterns = [
    path('wallet/', views.WalletList.as_view(), name='wallet-list'),
    path('wallet/<int:pk>/', views.WalletDetail.as_view(), name='wallet-detail'),
    path('operation/', views.OperationList.as_view(), name='wallet-list'),
    path('user/', views.UserList.as_view(), name='wallet-list'),
    path('auth/', include("rest_framework.urls")),
]