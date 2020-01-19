from django.urls import path
from . import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.setting),
    path('index', views.index),
    path('button1', views.button1),
    path('button2', views.button2),
    path('button3', views.button3),
    path('button4', views.button4),
    path('win',views.win),
]

