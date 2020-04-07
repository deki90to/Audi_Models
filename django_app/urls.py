from django.urls import path
from . import views


urlpatterns = [
	path('', views.a1, name='a1'),
	path('2', views.a2, name='a2'),
	path('3', views.a3, name='a3'),
	path('4', views.a4, name='a4'),
	path('5', views.a5, name='a5'),
	path('6', views.a6, name='a6'),
	path('7', views.a7, name='a7'),
	path('8', views.a8, name='a8'),
]