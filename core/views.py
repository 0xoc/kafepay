from django.shortcuts import render
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
# Create your views here.


class ProfileCreateView(CreateAPIView):
    serializer_class = ProfileCreateSerializer

    def post(self, request):
        s = self.serializer_class(data=request.data)

        if s.is_valid():
            profile = s.save()

            token, created = Token.objects.get_or_create(user=profile.user)

            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
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


class ProductCreateView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        s = self.serializer_class(data=request.data, context={'profile': request.user.user_profile.first()})

        if s.is_valid():
            s.save()
            return Response({'status':"Success"})
        else :
            return Response({'status': 'failed', 'data': s.errors}, status=status.HTTP_400_BAD_REQUEST)


class GateCreateView(CreateAPIView):
    serializer_class = GateCreateSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        s = self.serializer_class(data=request.data, context={'profile': request.user.user_profile.first()})

        if s.is_valid():
            s.save()
            return Response({'status':"Success"})
        else :
            return Response({'status': 'failed', 'data': s.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProductListView(ListAPIView):

    permission_classes = [IsAuthenticated, ]
    serializer_class = ProductListSerializer

    def get_queryset(self):
        return self.request.user.user_profile.first().products.all()

class GateListView(ListAPIView):

    permission_classes = [IsAuthenticated, ]
    serializer_class = GateListSerializer
    
    def get_queryset(self):
        return self.request.user.user_profile.first().gates.all()