from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from django.contrib.auth.password_validation import validate_password

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