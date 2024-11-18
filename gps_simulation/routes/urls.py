
from django.contrib import admin #
from django.urls import path #
from . import views
from django.conf import settings  #
from django.conf.urls.static import static  # 


urlpatterns = [
    path('', views.home, name='home'),
    path('load/', views.load_graph, name='load_graph'),
    path('shortest-route/', views.shortest_route, name='shortest_route'),
    path('city/<int:id>/', views.city_detail, name='city_detail'),
    path('tourist-places/', views.tourist_places, name='tourist_places'),
    path('contact/', views.contact, name='contact'),
]
