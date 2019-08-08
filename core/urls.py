from django.urls import path
from .views import *
urlpatterns = [
     path('create/profile/', ProfileCreateView.as_view()),
     path('update/profile/', ProfileUpdateView.as_view()),
     path('retrive/profile/', ProfileRetriveView.as_view()),
     path('create/product/', ProductCreateView.as_view()),
     path('create/gate/', GateCreateView.as_view()),
     path('list/gates/', GateListView.as_view()),
     path('list/products/', ProductListView.as_view()),
     path('detail/products/<uuid:uuid>/', ProductRetrieveView.as_view()),
]
