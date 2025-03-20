from django.contrib import admin
from .models import Company, Service, Protocol, Tag, ServiceRequest, Receipt

admin.site.register(Company)
admin.site.register(Service)
admin.site.register(Protocol)
admin.site.register(Tag)
admin.site.register(ServiceRequest)
admin.site.register(Receipt)
