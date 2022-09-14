from django.urls import path
from .views import UserList, UserDetail, UserCreate

urlpatterns = [
    path("", UserList.as_view(), name="UserList"),
    path("<int:pk>/", UserDetail.as_view(), name="UserDetail"),
    path('register/', UserCreate.as_view())
]