from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from userbase.serializers import UserBaseSerializer


class UserBaseSerializerView(APIView):
    permission_classes=[AllowAny,]
    def post(self, request, format='json'):
        serializer = UserBaseSerializer(data=request.data)
        if serializer.is_valid():
            json = serializer.data
            return Response(json,status = status.HTTP_200_OK)
        else:
            print("sell_order_serializer")
            return Response(serializer.errors ,status = status.HTTP_404_NOT_FOUND)