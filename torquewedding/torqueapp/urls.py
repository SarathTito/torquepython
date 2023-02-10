from django.urls import path
from . import views
app_name='torqueapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('func/<int:func_id>/',views.detail,name='detail'),
    path('info/',views.info,name='info'),
    path('test/',views.info,name='test')

]