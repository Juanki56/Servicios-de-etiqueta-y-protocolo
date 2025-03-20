from django.urls import path
from etiquetaYprotocolo.views import company_list, service_list, service_request_list

urlpatterns = [
    path("companies/", company_list, name="company_list"),
    path("services/", service_list, name="service_list"),
    path("service-requests/", service_request_list, name="service_request_list"),
]
