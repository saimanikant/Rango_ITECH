from django.urls import path
from rango import views

app_name='rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
    views.show_category, name='show_category'),
]
