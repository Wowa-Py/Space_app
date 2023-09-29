from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.decorators import api_view
from django.utils import timezone

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = response.data['token']
        return Response({'token': token})
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'birthdate']
    ordering_fields = ['name', 'email', 'birthdate']

@api_view(['POST'])
def create_user(request):
    name = request.data.get('name')
    email = request.data.get('email')
    birthdate = request.data.get('birthdate', timezone.now())
    user = User.objects.create(name=name, email=email, birthdate=birthdate)
    return Response({'id': user.id, 'name': user.name, 'email': user.email, 'birthdate': user.birthdate})
