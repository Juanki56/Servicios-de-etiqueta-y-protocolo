from django.shortcuts import render
from .models import Company, Service, ServiceRequest

# Vista para listar empresas
def company_list(request):
    companies = Company.objects.all()
    return render(request, "company_list.html", {"companies": companies})

# Vista para listar servicios
def service_list(request):
    services = Service.objects.all()
    return render(request, "service_list.html", {"services": services})

# Vista para listar solicitudes de servicio
def service_request_list(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, "service_request_list.html", {"service_requests": service_requests})
