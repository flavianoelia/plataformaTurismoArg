
from django.contrib import admin #
from django.urls import path #
from . import views
from django.conf import settings  #
from django.conf.urls.static import static  # 
#from .views import home, shortest_route, load_graph, city_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('load/', views.load_graph, name='load_graph'),
    path('shortest-route/', views.shortest_route, name='shortest_route'),
    path('city/<int:id>/', views.city_detail, name='city_detail'),
]
# Agregue esta línea para servir archivos media en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)