from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path("", UserList.as_view(), name="UserList"),
    path("<int:pk>/", UserDetail.as_view(), name="UserDetail"),
]