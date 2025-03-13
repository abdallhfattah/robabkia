# chat/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountProfileView

app_name = 'account'  # Add this line
router = DefaultRouter()

router.register(r'', AccountProfileView)

urlpatterns = [
    path('/' , include(router.urls)),
]
