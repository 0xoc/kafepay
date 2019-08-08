from django.shortcuts import render
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
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

class ProfileUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProfileRetriveUpdateSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user.user_profile.first()

    def put(self, request, *args, **kwargs):
        s = self.serializer_class(data=request.data, instance=self.get_object)

        if s.is_valid():
            s.save()
            return Response({"status": "Success"})
        else:
            return Response({'status': 'failed', 'data': s.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProfileRetriveView(RetrieveAPIView):
    serializer_class = ProfileRetriveUpdateSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user.user_profile.first()

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
        return self.request.user.user_profile.first().products.all().order_by('-id')

class ProductRetrieveView(RetrieveAPIView):

    permission_classes = [AllowAny, ]
    serializer_class = ProductListSerializer
    lookup_field = 'uuid'
    queryset = Product.objects.all()

class GateListView(ListAPIView):

    permission_classes = [IsAuthenticated, ]
    serializer_class = GateListSerializer
    
    def get_queryset(self):
        return self.request.user.user_profile.first().gates.all()