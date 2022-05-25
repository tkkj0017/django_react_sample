from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TaskViewSet, ManageUserView

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('myself/', ManageUserView.as_view(), name="myself"),
    path('', include(router.urls)),
]

