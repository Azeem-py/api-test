from rest_framework.response import Response
from rest_framework import viewsets, views, status
from .serializers import *
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

class CreateUser(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    #This is just for testing if the new user was actually created or better still for getting the list of all users
    def list(self, request):
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(views.APIView):
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        _,token = AuthToken.objects.create(user)
        content = {
            "user": str(user), "token": token
        }
        return Response(content)