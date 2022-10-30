from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import InfoSerializer
from .models import Info

# Create your views here.


class InfoApiView(RetrieveAPIView):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()
