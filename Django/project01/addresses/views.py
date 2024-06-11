from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Address
from .serializers import AddressSerializer


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Addresses(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # 모든 주소 정보 조회
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = AddressSerializer(data=request.data)

        if serializer.is_valid():
            address = serializer.save(user=request.user)
            serializer = AddressSerializer(address)        
            
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        
class AddressDetail(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, address_id):
        try:
            return Address.objects.get(id=address_id)
        except Address.DoesNotExist:
            raise NotFound

    # 주소 수정
    def put(self, request, address_id):
        address = self.get_object(address_id)
        serializer = AddressSerializer(address, data=request.data, partial=True)

        if serializer.is_valid():
            addr = serializer.save()
            serializer = AddressSerializer(addr)
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)

    # 주소 삭제
    def delete(self, request, address_id):
        address = self.get_object(address_id)
        if address is None:
            return Response({'error' : 'not found'})
        address.delete()

        return Response({ "success delete" }, status.HTTP_204_NO_CONTENT)