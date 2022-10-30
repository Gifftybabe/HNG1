from django.urls import path
from .views import InfoApiView

urlpatterns = [

    path('info/<pk>', InfoApiView.as_view()),
]
