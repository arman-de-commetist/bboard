from django.urls import path

from bboard.views import index, by_rubric, BbCreateView

urlpatterns = [
    path('add/',BbCreateView.as_view(), name="add"),
    path('<int:rubric_id>/', by_rubric, name="by_rubric"),
    path('', index, name='index'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.login_page, name='login'),
]
