from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from .models import Registration


class RegistrationListAPIView(APIView):
    """Handle registration API - List all or Create new"""
    parser_classes = [ JSONParser,FormParser,MultiPartParser]

    def get(self, request):
        registrations = Registration.objects.all()
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response("Success")
            return Response({
                'message': 'Registration successful!',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


