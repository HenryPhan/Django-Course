
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from sale_management.models import Employee
from django.views import generic


# def detail(request, employee_id):
#     # try:
#     #     employee = Employee.objects.get(pk=employee_id)
#     # except Employee.DoesNotExist:
#     #     raise Http404("Employee does not exist")
#     # return HttpResponse(employee)
#     employee = get_object_or_404(Employee, pk=employee_id)
#     return render(request, 'sale_management/employee/detail.html', {'employee': employee})

class DetailView(generic.DetailView):
    model = Employee
    template_name = 'sale_management/employee/detail.html'


# def listing(request):
#     latest_employee_list = Employee.objects.order_by('-created_at')[:3]
#     context = {
#         'latest_employee_list': latest_employee_list,
#     }
#     # template = loader.get_template('sale_management/employee/index.html')
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'sale_management/employee/index.html', context)

class ListingView(generic.ListView):
    template_name = 'sale_management/employee/index.html'
    context_object_name = 'latest_employee_list'

    def get_queryset(self):
        return Employee.objects.order_by('-created_at')[:3]