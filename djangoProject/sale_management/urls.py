from django.urls import path

from sale_management.views import detail, listing

urlpatterns = [
    path('employee/<int:employee_id>/', detail, name='detail'),
    path('employee/', listing, name='listing'),
]
