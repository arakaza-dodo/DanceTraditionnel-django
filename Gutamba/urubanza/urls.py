from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()
router.register('agenda', AgendaViewset)
router.register('club', ClubViewset)
router.register('video', VideoViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/',TokenPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('api-auth/',include('rest_framework.urls')),
  
]

