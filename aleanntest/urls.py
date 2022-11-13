from django.contrib import admin
from django.urls import path

from aleannlab.views import UsersAPIView, RankAPIView, UserAPIDetailView, RankAPIDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', UsersAPIView.as_view()),
    path('api/v1/ranks/', RankAPIView.as_view()),
    path('api/v1/users/<int:pk>', UserAPIDetailView.as_view()),
    path('api/v1/ranks/<int:pk>', RankAPIDetailView.as_view()),

]
