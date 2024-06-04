from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from django.contrib.auth.password_validation import validate_password

# 사용자 인증
from rest_framework.authentication import TokenAuthentication
# 권한 부여
from rest_framework.permissions import IsAuthenticated

from addresses.serializers import AddressSerializer
from .serializers import MyInfoUserSerializer
from .models import User
from addresses.models import Address

class Users(APIView):
    def get(sefl, request):
        users = User.objects.all()
        return Response(MyInfoUserSerializer(users, many=True).data)

    def post(self, request):
        # password => 검증 && 해쉬화 해서 저장 필요
        password = request.data.get('password')
        serializer = MyInfoUserSerializer(data=request.data)

        try: 
            validate_password(password=password)
        except:
            raise ParseError('Invalid password')
        
        if serializer.is_valid():
            user = serializer.save() # 새로운 유저 생성
            user.set_password(password) # 비밀번호 해쉬화
            user.save()

            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        
        else:
            raise ParseError(serializer.errors)
        

class UserAddress(APIView):
    def get(self, request, user_id):
        addr = Address.objects.filter(user_id=user_id)

        if not addr.exists():
            raise Http404("No addresses found for this user.")

        serializer = AddressSerializer(addr, many=True)
        return Response(serializer.data)
    
    def post(self, request, user_id):
        serializer = AddressSerializer(data=request.data)

        if serializer.is_valid():
            addr = serializer.save(user=request.user)
            serializer = AddressSerializer(addr)
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)
        
class MyInfo(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)

        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)

            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)
        
from django.contrib.auth import authenticate, login, logout
from rest_framework import status

class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            raise ParseError()
        
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

class Logout(APIView):
    permisson_classes = [IsAuthenticated]
    def post(self, request):
        print("header: ", request.headers)
        logout(request)

        return Response(status=status.HTTP_200_OK)
    
import jwt
from django.conf import settings
class JWTLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            raise ParseError()
        
        user = authenticate(request, username=username, password=password)

        if user:
            payload = {"id": user.id, "username": user.username}
            token = jwt.encode(
                payload,
                settings.SECRET_KEY,
                algorithm="HS256"
            )

            return Response({"token": token})
        
from config.authentication import JWTAuthentication
class UserDetailView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({"id": user.id, "username": user.username})