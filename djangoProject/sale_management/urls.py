from django.urls import path

from sale_management.views import index

urlpatterns = [
    path('', index, name='index'),
]
