from django.shortcuts import render
from rest_framework.generics import CreateAPIView, GenericAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class ProfileCreateView(CreateAPIView):
    serializer_class = ProfileCreateSerializer

    def post(self, request):
        s = self.serializer_class(data=request.data)

        if s.is_valid():
            s.save()

            return Response({'status': 'success'})
        else:
            return Response({'status': 'failed', 'data': s.errors}, status=status.HTTP_400_BAD_REQUEST)

class ProfileUpdateView(GenericAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAuthenticated, ]

    def patch(self, request, *args, **kwargs):
        instance = request.user.user_profile.first()

        s = self.serializer_class(data=request.data, instance=instance, partial=True)

        if s.is_valid():
            s.save()
            return Response({"status": "Success"})
        else:
            return Response({'status': 'failed', 'data': s.errors}, status=status.HTTP_400_BAD_REQUEST)

