from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.ProductViewset)
router.register('reviews', views.ReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
    
]