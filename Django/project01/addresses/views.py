from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Address
from .serializers import AddressSerializer

class Addresses(APIView):
    # 모든 주소 정보 조회
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)

        return Response(serializer.data)
    
class AddressDetail(APIView):
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


        return Response({ "success delete"})