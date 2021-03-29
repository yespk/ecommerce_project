from django.urls import path

from store import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('addbrand', views.set_brands, name='addbrand'),
    path('success', views.success, name='success')
]


