from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from authenticate.api.v1.serializers import LoginSerializer

User = get_user_model()


class LoginAPIView(APIView):

    def post(self, reqeust, *args, **kwargs):
        
        serializer = LoginSerializer(data=reqeust.data)

        if serializer.is_valid():
            user = authenticate(username=serializer.data["username"], password=serializer.data["password"])
            if not user:
                # Given credentials are invalid
                return Response({"message": "Invalid credentials"}, status=400)

            token, _ = Token.objects.get_or_create(user=user)

            return Response({"message": "Logged in", "token": token.key}, 200)
    
        return Response(serializer.errors, 400)
