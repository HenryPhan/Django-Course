from django.urls import path

from sale_management.views import employee, order

urlpatterns = [
    # path('employee/<int:employee_id>/', employee.detail, name='employee_detail'),
    path('employee/<int:pk>/', employee.DetailView.as_view(), name='employee_detail'),
    path('employee/', employee.ListingView.as_view(), name='employee_listing'),

    path('order/<int:pk>/', order.DetailView.as_view(), name='order_detail'),
    # path('order/', order.listing, name='order_listing'),
    path('order/', order.ListingView.as_view(), name='order_listing'),
]
