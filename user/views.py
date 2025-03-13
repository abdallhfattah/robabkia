from rest_framework import generics, permissions
from .models import Account
from .serializers import AccountSerializer
from rest_framework import viewsets

class AccountProfileView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # only logined users will be able to view account
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  # Get the logged-in user


