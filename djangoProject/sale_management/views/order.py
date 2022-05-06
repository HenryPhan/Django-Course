
from django.shortcuts import render, get_object_or_404
from sale_management.models import Order
from django.views import generic


def detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    context = {
        'order': order,
        'details': order.orderdetail_set.all()
    }
    return render(request, 'sale_management/order/detail.html', context)


# def listing(request):
#     orders = Order.objects.order_by('-created_at')[:3]
#     context = {
#         'orders': orders
#     }
#     return render(request, 'sale_management/order/index.html', context)

class ListingView(generic.ListView):
    template_name = 'sale_management/order/index.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.order_by('-created_at')[:3]
